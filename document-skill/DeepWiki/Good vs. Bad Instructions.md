# Good vs. Bad Instructions - Devin Docs

Source: https://docs.devin.ai/essential-guidelines/good-vs-bad-instructions

- Support

- Devin

- Devin

- Introducing Devin

- Your First Session

- Tutorial Library

- When to Use Devin

- Instructing Devin Effectively

- Good vs. Bad Instructions

- Prompt Templates Cheat Sheet

- How does Devin fit into my existing SDLC?

- Environment configuration

- Index a Repository

- VPN Configuration

- Knowledge Onboarding

- AGENTS.md

- Devin Review

- Devin Session Tools

- Computer Use

- Testing & Video Recordings

- Slash Commands

- Ask Devin

- Data Analyst Agent

- DeepWiki

- MCP (Model Context Protocol) Marketplace

- DeepWiki MCP

- Devin MCP

- Advanced Capabilities

- Knowledge

- Skills

- Session Insights

- Secrets & Site Cookies

- Creating Playbooks

- Using Playbooks

- Scheduled Sessions

- Deployments

- Autofix Settings - Bot Comments

- Invite your Team

- Importing Code Settings

- Integrations Overview

- Slack

- Microsoft Teams

- GitHub

- GitLab

- Bitbucket

- Linear

- Jira

- GitHub Pull Request Templates

- Self-Hosted SCM & Artifacts

- Security at Cognition

- Billing

- Common Issues

- More Examples

- Good

- Bad

# Good vs. Bad Instructions

What works and what doesn’t

## Adding a New API Endpoint

```
/users/stats
```

```
/orders/stats
```

```
statsController.js
```

```
StatsController.test.js
```

- Clearly specifies the route and expected response format

- References existing code as a template

- Defines data source (users table)

- Includes test coverage requirements

- Unspecific about what stats to include

- No mention of data sources

- No reference to existing patterns

- Missing test requirements

## Frontend Feature for Displaying Data

```
UserProfileComponent
```

```
DropdownBase
```

- Names specific components

- Lists exact roles to include

- References existing styling component

- Defines the user interaction flow

- Includes validation steps

- “User-friendly” is subjective

- No specific UI components mentioned

- Unclear user interaction flow

- Vague validation criteria

## ​ More Examples

### ​ Good

## Writing Unit Tests

```
UserService.test.js
```

```
npm test -- --coverage
```

```
UserService.test.js
```

## Migrating or Refactoring Existing Code

```
logger.js
```

```
tsconfig.json
```

```
LoggerTest.test.js
```

```
tsc
```

```
npm test LoggerTest.test.js
```

```
tsconfig.json
```

## Updating APIs or Database Queries

```
OrderModel
```

```
npm run test:integration UserModel.test.js
```

```
npm run test:e2e user-flows.test.js
```

```
OrderModel.js
```

## Implementing a Feature from a Design

## Investigating a Production Bug

### ​ Bad

## Open-Ended Code Review

```
oldLogger
```

```
src/services/
```

## Purely Subjective Visual Requests

```
indigo-500
```

## Highly Complex, Vague Projects

- Use Ask Devin to investigate your codebase and map dependencies

- Ask Devin to propose specific architectures with trade-offs

- Create separate sessions for implementing each service — run them in parallel with managed Devins
