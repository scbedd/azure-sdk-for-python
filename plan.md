# Keyvault Nightly Failure Investigation

## TL;DR

**Both failures are caused by `cryptography==47.0.0` being resolved from the auth-ed CI feed.** Locally, without the auth-ed feed, only `cryptography==46.0.3` is available, which is why these don't repro without explicitly configuring `UV_DEFAULT_INDEX`.

---

## Failure 1: `azure-keyvault-keys` — ALL platforms (pypy311, CPython 3.10/3.12/3.13/3.14)

### Error
```
TypeError: Can't instantiate abstract class KeyVaultRSAPublicKey with abstract method __deepcopy__
```

### Root Cause

`cryptography==47.0.0` added `__deepcopy__` as a new **abstract method** on `RSAPublicKey` and `RSAPrivateKey`. Our classes `KeyVaultRSAPublicKey` (line 121) and `KeyVaultRSAPrivateKey` (line 327) in `sdk/keyvault/azure-keyvault-keys/azure/keyvault/keys/crypto/_models.py` implement `__copy__` but NOT `__deepcopy__`. Python refuses to instantiate a class with unimplemented abstract methods.

### Evidence

| Version | `RSAPublicKey.__copy__` | `RSAPublicKey.__deepcopy__` |
|---------|------------------------|----------------------------|
| 46.0.3  | abstract=True          | **does not exist**         |
| 47.0.0  | abstract=True          | **abstract=True** (NEW)    |

Our code at `_models.py:312` defines `__copy__` (satisfying that requirement) but has no `__deepcopy__`, so instantiation fails with cryptography 47.

### Local Repro (CONFIRMED)

```bash
# Using dispatch_checks.py with the nightly artifact:
source ./venv_pypy/bin/activate
TF_BUILD=true python eng/scripts/dispatch_checks.py "azure-keyvault-keys" \
  --service keyvault -c whl \
  -w /home/semick/repo/azure-sdk-for-python/packages/packages_extended

# Result: 12 failed tests, all TypeError: Can't instantiate abstract class KeyVaultRSAPublicKey
```

The failing tests are all those that call `CryptographyClient.create_rsa_public_key()` or `create_rsa_private_key()`:
- `test_encrypt_and_decrypt_with_managed_key` (7.4, 7.5)
- `test_encrypt_and_decrypt_with_managed_key_no_get` (7.6)
- `test_sign_and_verify_with_managed_key` (7.4, 7.5)
- `test_rsa_public_key_*` unit tests
- `test_rsa_private_key_*` unit tests

### Fix (for when ready to implement)

Add `__deepcopy__` to both `KeyVaultRSAPublicKey` and `KeyVaultRSAPrivateKey`. Since these are treated as immutable (their `__copy__` returns `self`), `__deepcopy__` should do the same:

```python
def __deepcopy__(self, memo: dict) -> "KeyVaultRSAPublicKey":
    return self
```

---

## Failure 2: `azure-keyvault-certificates` — pypy311 ONLY

### Error
```
ImportError: .../cryptography/hazmat/bindings/_rust.pypy311-pp73-x86_64-linux-gnu.so: undefined symbol: PySlice_AdjustIndices
```

### Root Cause

The `cryptography==47.0.0` PyPy wheel served by the CI Azure DevOps feed references the CPython C-API symbol `PySlice_AdjustIndices`, which is NOT available in PyPy's C-API compatibility layer. This causes an `ImportError` when any code imports `cryptography`'s Rust-compiled bindings.

The certificate tests `test_merge_certificate.py` and `test_merge_certificate_async.py` import `from OpenSSL import crypto`, which triggers the `cryptography` Rust binding import, hitting this error during **test collection** (exit code 2 = collection error).

### Why it only affects certificates on pypy311

- On CPython: `cryptography 47.0.0` loads fine because `PySlice_AdjustIndices` exists in CPython's C-API. The certificates tests pass (they don't use `KeyVaultRSAPublicKey`).
- On PyPy: The `.so` references `PySlice_AdjustIndices` (CPython symbol) instead of `PyPySlice_AdjustIndices` (PyPy equivalent), so import fails entirely.
- The `keyvault-keys` tests also fail on pypy311, but with the `__deepcopy__` error (which happens later, after import succeeds for the non-OpenSSL tests).

### Local Repro (NOT REPRODUCIBLE)

On our local PyPy 7.3.20, `cryptography==47.0.0` imports successfully. Inspection of the local `.so` shows it correctly references `PyPySlice_AdjustIndices`:

```
$ nm -D _rust.pypy311-pp73-x86_64-linux-gnu.so | grep PySlice
                 U PyPySlice_AdjustIndices   <-- correct PyPy symbol
```

This suggests CI's Azure DevOps feed is serving a **different (broken) wheel** than what's currently available on PyPI. Possible explanations:
1. The `cryptography` 47.0.0 wheel for PyPy was initially published with a CPython-compiled binary and later replaced/yanked
2. The Azure DevOps feed cached the broken initial wheel
3. CI's PyPy runtime version differs slightly from ours in C-API availability

---

## Why This Doesn't Repro Locally (Without Auth-ed Feed)

The SKILL.md nails it:
> An issue may STEM FROM the fact that a newer version is available through upstream, so the issue only appears for CI (aka auth-ed) feed accessors.

- **Public PyPI** (locally): Only has `cryptography<=46.0.3` available (or the resolver pins to it)
- **Auth-ed Azure DevOps feed** (CI): Pulls through `cryptography==47.0.0` from upstream

The user previously ran `dispatch_checks.py` without setting `UV_DEFAULT_INDEX` or providing the wheel artifacts, so their environment resolved `cryptography<=46.x` and the tests passed.

---

## Summary of Affected Tests

| Package | Platform | Failure Count | Root Cause |
|---------|----------|---------------|------------|
| azure-keyvault-keys | ALL (pypy311 + CPython) | 5-12 per check | `__deepcopy__` abstract method missing |
| azure-keyvault-certificates | pypy311 ONLY | 2 (collection errors) | Broken `.so` binary for PyPy |

---

## Recommended Actions

1. **Immediate fix for keys**: Implement `__deepcopy__` on `KeyVaultRSAPublicKey` and `KeyVaultRSAPrivateKey` (same pattern as existing `__copy__` — return `self`).

2. **Immediate fix for certificates on pypy**: Pin `cryptography<47` in the keyvault-certificates dev_requirements.txt or the shared_requirements.txt. Alternatively, wait for PyPy to get a fixed wheel from upstream.

3. **Long-term**: Consider adding an upper bound on `cryptography` in `pyproject.toml` for keyvault-keys (`cryptography>=2.1.4,<48`), or better, implement the `__deepcopy__` fix so it's compatible with all versions.

4. **Feed investigation**: The PyPy wheel issue may indicate a stale/broken wheel in the Azure DevOps feed cache. Someone with feed admin access should check if the `cryptography==47.0.0` PyPy wheel in the feed matches what's currently on PyPI.
