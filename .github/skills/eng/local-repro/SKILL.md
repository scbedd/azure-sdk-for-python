---
name: local-repro
description: Assist developers in reproducing issues seen in CI locally.
---

<!-- cspell:words pylintrc vnext -->

# Local Repro

## Reproing a pullrequest failure

The `python - pullrequest` pipeline is a dynamically expanding and contracting build. Given a set of changed files, it will determine which packages need to be build and tested. If a pullrequest fails, the first step is to determine which package(s) failed. This can be done by looking at the logs of the failed pipeline run.

The pipeline is present on a `public` Azure DevOps project, so any user can view the logs. The URL to query using the Azure DevOps API is:

```bash
https://dev.azure.com/azure-sdk/public/_build?definitionId=7050
```

You can use the checks reported on the pullrequest to determine which buildId should be queried for logs.

## Reproing `internal` Release or Nightly Alpha builds

`internal` builds are not publically accessible, so the user must follow the `CONTRIBUTING.md` and get a token with the appropriate permissions to access the logs. That is `Build: read` permissions on the `azure-sdk` organization.

Once the user has the appropriate permissions, they should set it as an environment variable:

```bash
export ADO_TOKEN=$TOKEN
```

Then, any agent with knowledge of the devops REST api can query the logs of the build using the same URL as above, but with Bearer token authentication leveraging your `ADO_TOKEN`.
