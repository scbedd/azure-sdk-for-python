# Retrieving ADO Build Logs from a Pull Request

This document describes how to go from a GitHub pull request number to the relevant Azure DevOps build logs, specifically for diagnosing failures in the `python - pullrequest` pipeline.

All examples target the **public** Azure DevOps project: `https://dev.azure.com/azure-sdk/public`.

## Step 1: Get the Build ID from a Pull Request

### Option A: GitHub CLI (`gh`)

Given a PR number, use the GitHub CLI to list the check runs reported on the PR:

```bash
gh pr checks <PR_NUMBER> --repo Azure/azure-sdk-for-python
```

This outputs a table of check names, statuses, and links. Each Azure Pipelines check will include a **detail URL** that contains the `buildId`. The URL format is:

```
https://dev.azure.com/azure-sdk/public/_build/results?buildId=<BUILD_ID>&view=...
```

Extract the `buildId` from the URL of the check you're interested in.

You can also get the head SHA and check runs programmatically with `gh`:

```bash
# Get the head SHA of the PR
HEAD_SHA=$(gh pr view <PR_NUMBER> --repo Azure/azure-sdk-for-python --json headRefOid -q .headRefOid)

# List check runs for that commit
gh api repos/Azure/azure-sdk-for-python/commits/$HEAD_SHA/check-runs --jq '.check_runs[] | {name, status, conclusion, details_url}'
```

### Option B: Raw GitHub REST API (no `gh` required)

If the `gh` CLI is not available, you can use `curl` against the GitHub REST API directly.

**Step 1a: Get the head SHA of the PR:**

```bash
HEAD_SHA=$(curl -s "https://api.github.com/repos/Azure/azure-sdk-for-python/pulls/<PR_NUMBER>" \
  | jq -r '.head.sha')
```

> **Note:** For private repos or to avoid rate limits, add `-H "Authorization: token $GITHUB_TOKEN"`.

**Step 1b: List check runs for that commit:**

```bash
curl -s "https://api.github.com/repos/Azure/azure-sdk-for-python/commits/$HEAD_SHA/check-runs" \
  | jq '[.check_runs[] | {name, status, conclusion, details_url}]'
```

The `details_url` field on each check run contains the ADO build link. Extract the `buildId` from the URL query parameter:

```bash
# Extract buildId from the details_url of a specific check run
curl -s "https://api.github.com/repos/Azure/azure-sdk-for-python/commits/$HEAD_SHA/check-runs" \
  | jq -r '.check_runs[] | select(.conclusion == "failure") | .details_url' \
  | grep -oP 'buildId=\K[0-9]+'
```

## Step 2: Get the Build Timeline (Find Failed Tasks)

Once you have a `buildId`, query the Azure DevOps Build Timeline API to get all tasks/steps in the build:

```bash
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/<BUILD_ID>/timeline?api-version=6.0"
```

The response contains a `records` array. Each record represents a stage, job, or task in the pipeline. The key fields are:

| Field        | Description                                               |
| ------------ | --------------------------------------------------------- |
| `name`       | Name of the task/job/stage                                |
| `type`       | One of `Stage`, `Job`, `Task`                             |
| `state`      | `completed`, `inProgress`, `pending`                      |
| `result`     | `succeeded`, `failed`, `canceled`, `skipped`, etc.        |
| `log.id`     | Log ID (used to fetch task logs)                          |
| `log.url`    | Direct API URL to the task's log                          |
| `parentId`   | ID of the parent record (to trace task → job → stage)     |

### Filter to Failed Tasks

To find only failed tasks:

```bash
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/<BUILD_ID>/timeline?api-version=6.0" \
  | jq '[.records[] | select(.result == "failed" and .type == "Task") | {name, id, logId: .log.id, logUrl: .log.url}]'
```

## Step 3: Get the Logs for a Failed Task

Each task's log can be fetched using the log ID from the timeline:

```bash
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/<BUILD_ID>/logs/<LOG_ID>?api-version=6.0"
```

Or use the `log.url` directly from the timeline record (it already includes the full URL).

### Get Only the Tail (Last ~100 Lines)

To get just the summary/tail of the log output:

```bash
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/<BUILD_ID>/logs/<LOG_ID>?api-version=6.0" \
  | tail -n 100
```

The tail of a failed task's log typically contains:
- The `=== SUMMARY ===` table (for `dispatch_checks.py` tasks)
- Error messages and stack traces
- The final exit code

## Full Example: End-to-End

### Using `gh` CLI

```bash
# 1. Get the build ID from PR checks
gh pr checks 12345 --repo Azure/azure-sdk-for-python
# → Find the failing check, note the buildId from its URL

# 2. Get failed tasks from the build timeline
BUILD_ID=9876543
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/$BUILD_ID/timeline?api-version=6.0" \
  | jq '[.records[] | select(.result == "failed" and .type == "Task") | {name, logId: .log.id}]'

# 3. Grab the tail of the failed task's log
LOG_ID=42
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/$BUILD_ID/logs/$LOG_ID?api-version=6.0" \
  | tail -n 100
```

### Using raw `curl` only (no `gh`)

```bash
PR_NUMBER=12345

# 1. Get head SHA from the PR
HEAD_SHA=$(curl -s "https://api.github.com/repos/Azure/azure-sdk-for-python/pulls/$PR_NUMBER" \
  | jq -r '.head.sha')

# 2. Get the buildId from the first failing check run
BUILD_ID=$(curl -s "https://api.github.com/repos/Azure/azure-sdk-for-python/commits/$HEAD_SHA/check-runs" \
  | jq -r '.check_runs[] | select(.conclusion == "failure") | .details_url' \
  | head -1 \
  | grep -oP 'buildId=\K[0-9]+')

# 3. Get failed tasks from the build timeline
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/$BUILD_ID/timeline?api-version=6.0" \
  | jq '[.records[] | select(.result == "failed" and .type == "Task") | {name, logId: .log.id}]'

# 4. Grab the tail of the failed task's log
LOG_ID=42
curl -s "https://dev.azure.com/azure-sdk/public/_apis/build/builds/$BUILD_ID/logs/$LOG_ID?api-version=6.0" \
  | tail -n 100
```

## Authentication

- **Public project**: Read access to build logs does not require authentication.
- **Internal project**: Requires a PAT or Bearer token. See the main SKILL.md for instructions on setting `ADO_TOKEN`.

When authentication is needed, add the header:

```bash
# PAT (Personal Access Token) - use Basic auth
curl -s -u ":$ADO_TOKEN" "https://dev.azure.com/azure-sdk/internal/_apis/build/builds/<BUILD_ID>/timeline?api-version=6.0"

# Bearer token
curl -s -H "Authorization: Bearer $ADO_TOKEN" "https://dev.azure.com/azure-sdk/internal/_apis/build/builds/<BUILD_ID>/timeline?api-version=6.0"
```
