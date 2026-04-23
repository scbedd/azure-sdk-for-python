---
name: local-repro
description: Assist developers in reproducing issues seen in CI locally. Use this if the user is asking to reproduce and issue given a devops build URL or github PR.
---

<!-- cspell:words pylintrc vnext -->

# Local Repro

## Checking out the correct code

Before attempting to reproduce any CI failure, you **must** ensure your local checkout matches the exact code that CI ran against. A mismatch between your local state and the CI commit will produce misleading results.

Given a pull request, fetch and checkout the PR branch at the same HEAD SHA that CI used:

```bash
# Fetch the PR branch and check it out
gh pr checkout <PR_NUMBER> --repo Azure/azure-sdk-for-python
```

Or without `gh`:

```bash
git fetch origin pull/<PR_NUMBER>/head:pr-<PR_NUMBER>
git checkout pr-<PR_NUMBER>
```

If the PR has been updated since the failing CI run, you may need to reset to the specific commit SHA that triggered the build. The head SHA is available from the PR details or from the check run metadata (see [Retrieving ADO Build Logs](references/ado-pr-build-logs.md)):

```bash
# Checkout the exact SHA that CI ran against
git checkout <HEAD_SHA>
```

**Do not skip this step.** Running checks against a different commit than what CI used is the most common reason a local repro does not match CI results.

## Reproing a pullrequest failure

For detailed steps on retrieving build IDs from PR checks, finding failed tasks, and fetching log output, see [Retrieving ADO Build Logs from a Pull Request](references/ado-pr-build-logs.md).

The `python - pullrequest` pipeline is a dynamically expanding and contracting build. Given a set of changed files, it will determine which packages need to be build and tested. If a pullrequest fails, the first step is to determine which package(s) failed. This can be done by looking at the logs of the failed pipeline run.

The pipeline is present on a `public` Azure DevOps project, so any user can view the logs. The URL to query using the Azure DevOps API is:

```bash
https://dev.azure.com/azure-sdk/public/_build?definitionId=7050
```

You can use the checks reported on the pullrequest to determine which buildId should be queried for logs. In _every_ check that originates from `dispatch_checks.py`, there will be a final summary of whichever checks are being invoked.

This summary looks similar to the following:

```
=== SUMMARY ===
PACKAGE                                              CHECK   STATUS  DURATION(s)
--------------------------------------------------------------------------------
/mnt/vss/_work/1/s/sdk/agrifood/azure-mgmt-agrifood  bandit  OK              3.97

Total checks: 1 | Failed: 0 | Worst exit code: 0

Finishing: Run Bandit
```

So below the `=== SUMMARY ===` line, there is a table of all the checks that were run, their status, and duration. The `PACKAGE` column will indicate which package was being checked. In this example, the package is `azure-mgmt-agrifood`. If there were any failures, they would be indicated in the `STATUS` column. Once the package(s) that failed are identified, the user can then attempt to reproduce the failure locally by running the same check that failed. In this example, the check that was run was `bandit`, so the user would run `invoke bandit` in the `azure-mgmt-agrifood` package to attempt to reproduce the failure locally.

```
# use existing or create and activate a venvironment
cd sdk/agrifood/azure-mgmt-agrifood
uv pip install dev_requirements.txt
azpysdk pylint .
```

When there are **MULTIPLE** checks failed across many checks and packages, offer the user the list of failed checks and ask them which one they want to attempt to reproduce first. For example:

```The following checks failed:
1. bandit check in azure-mgmt-agrifood
2. pylint check in azure-mgmt-agrifood
3. bandit check in azure-mgmt-agrifood-file-datalake

Which check would you like to attempt to reproduce first? (enter the number)
```

## Reproing `internal` Release or Nightly Alpha builds

`internal` builds are not publically accessible, so the user must follow the `CONTRIBUTING.md` and get a token with the appropriate permissions to access the logs. That is `Build: read` permissions on the `azure-sdk` organization.

Once the user has the appropriate permissions, they should set it as an environment variable:

```bash
export ADO_TOKEN=$TOKEN
```

Then, any agent with knowledge of the devops REST api can query the logs of the build using the same URL as above, but with Bearer token authentication leveraging your `ADO_TOKEN`.
