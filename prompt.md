# wtf is up with keyvault

I have set PIP_INDEX_URL, UV_DEFAULT_INDEX, have been set with a collaborator accessing key. I have verified using a uv pip install that UV_DEFAULT_INDEX is definitely set to allow pulling new package versions through from upstream (as CI is). ADO_TOKEN has `build: read` as necessary. Do not access them to check just use them.

I have created two venvs for you at repo root. `./venv_pypy` and `./venv_313`. Former is for `pypy311` repro, latter is for `any other platform` repros. Activate these before calling `dispatch_checks.py`.

I have two categories of failures around the packages `azure-keyvault-certificates` and `azure-keyvault-keys` are all failing for very weird reasons that don't repro locally for me.

## Nightly build failures

Build Link: https://dev.azure.com/azure-sdk/internal/_build/results?buildId=6226335&view=results
Summary of failed tests. `pypy311` has failures on `azure-keyvault-certificates` AND `azure-keyvault-keys`. Just `azure-keyvault-keys` only otherwise.

```
# pypy311 test result summary (only failed)
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates    latestdependency  FAIL(2)        16.32
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates    mindependency     FAIL(2)        16.62
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates    sdist             FAIL(2)        34.44
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates    whl               FAIL(2)        58.24
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates    whl_no_aio        FAIL(2)        14.62
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-keys            latestdependency  FAIL(1)       186.63
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-keys            sdist             FAIL(1)       187.50
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-keys            whl               FAIL(1)       183.62
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-keys            whl_no_aio        FAIL(1)       166.25
# any platform not pypy311 has only azure-keyvault-keys
D:\a\_work\1\s\sdk\keyvault\azure-keyvault-keys            latestdependency  FAIL(1)       143.49
D:\a\_work\1\s\sdk\keyvault\azure-keyvault-keys            sdist             FAIL(1)       145.72
D:\a\_work\1\s\sdk\keyvault\azure-keyvault-keys            whl               FAIL(1)       139.48
D:\a\_work\1\s\sdk\keyvault\azure-keyvault-keys            whl_no_aio        FAIL(1)       135.46
```

Then, this PR had issues with `azure-keyvault-certificates` only in a PR build: https://dev.azure.com/azure-sdk/public/_build/results?buildId=6224978&view=logs&jobId=d049a9a1-4a4a-5c37-2173-6c4a695afdc9

Summary of failed tests, only pypy311:

```
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates :: mindependency :: 2
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates :: sdist :: 2
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates :: whl :: 2

=== SUMMARY ===
PACKAGE                                                      CHECK          STATUS  DURATION(s)
-----------------------------------------------------------------------------------------------
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates  mindependency  FAIL(2)        54.09
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates  sdist          FAIL(2)        55.15
/mnt/vss/_work/1/s/sdk/keyvault/azure-keyvault-certificates  whl            FAIL(2)        56.06
```

Which ALSO doesn't repro locally for me. You're running on a WSL instance, so only attempt to repro `ubuntu` based errors.

Please use the skill `.github/skills/eng/local-repro/SKILL.md` to investigate this.

Make certain to use the skill to get the artifacts as necessary etc etc. Enhance the `SKILL.md` for script used to download the artifact if that will help later on.

I want you to build an EXPLANATION for why this is failing, output that to `plan.md` at repo root. Make no code changes until we interact again.