# AI-Powered Content Automation Platform

> A serverless AWS platform for planning, queueing, scheduling, publishing, and monitoring content across multiple X accounts.

**Repository:** <https://github.com/AZ1600/AI-Powered-Content-Automation-Platform>  
**Last verified:** 2026-07-11 against the repository README

## Problem and Solution

Manual multi-account publishing is repetitive and difficult to govern. This platform creates an operational workflow with daily plans, a draft queue, scheduled and manual publishing, publish-state tracking, and recent activity in one browser control panel.

## Verified Architecture

```text
Browser control panel -> API Gateway -> Lambda service layer
                                      |-> DynamoDB
                                      |-> Secrets Manager
                                      `-> EventBridge scheduler -> X API
```

## Engineering Areas Demonstrated

- Event-driven serverless design.
- AWS SAM infrastructure as code.
- OAuth-based external API connection.
- Secrets Manager credential and token storage.
- DynamoDB-backed plans, queue state, and activity.
- EventBridge scheduled execution.
- Manual controls, outcome tracking, and failed-state visibility.
- Screenshots providing end-to-end publishing evidence.

## Production Questions

- How are retries, rate limits, duplicate publishing, and dead-letter handling managed?
- How are OAuth tokens refreshed and access separated by account?
- What alarms identify repeated failures?
- How are API and AWS costs bounded?
