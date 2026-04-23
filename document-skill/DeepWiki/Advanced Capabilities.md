# Advanced Capabilities - Devin Docs

Source: https://docs.devin.ai/work-with-devin/advanced-capabilities

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

- What Devin can do for you

- Managed Devins

- Analyzing sessions

- Creating and improving playbooks

- Managing knowledge

- Managing schedules

- Best practices

- Analyzing sessions effectively

- Creating useful playbooks

- Managing knowledge at scale

- Using these features via the Devin MCP

- Session management

- Playbook management

- Knowledge management

- Schedule management

- Integration management

- Repository documentation

- Permissions

# Advanced Capabilities

Devin can orchestrate managed sessions, analyze past work, create playbooks, and manage your knowledge base

## ​ What Devin can do for you

- Orchestrate managed Devins in parallel : Break down a large task and delegate pieces to a team of managed Devin sessions, each running in its own isolated VM

- Analyze session outcomes : Understand why a session succeeded or failed, identify patterns, and extract learnings

- Create and improve playbooks : Turn successful sessions into reusable playbooks, or refine existing ones based on feedback

- Manage knowledge : Deduplicate, consolidate, or create new knowledge entries from your codebase

- Manage schedules : Set up recurring or one-time automated Devin sessions

## ​ Managed Devins

- Spin up managed Devins — launch child sessions with specific prompts, playbooks, tags, and ACU limits

- Message child sessions — send follow-up instructions or clarifications to running sessions

- Monitor ACU consumption — track how much compute each child session is using

- Put child sessions to sleep or terminate them — pause or stop sessions that are stuck or no longer needed

- Schedule messages to itself — set reminders to check back on long-running child sessions

```
Analyze our codebase for all files using the legacy REST client. Group them into independent work packages that won't conflict, then start a parallel Devin session for each package to migrate to the new GraphQL client. Use the "REST to GraphQL Migration" playbook for each session.
```

```
Analyze our codebase for all files using the legacy REST client. Group them into independent work packages that won't conflict, then start a parallel Devin session for each package to migrate to the new GraphQL client. Use the "REST to GraphQL Migration" playbook for each session.
```

```
Run the test coverage report, find the 8 modules below 50% coverage, and start a parallel Devin session for each module using our test-writing playbook. Open a separate PR for each.
```

```
Run the test coverage report, find the 8 modules below 50% coverage, and start a parallel Devin session for each module using our test-writing playbook. Open a separate PR for each.
```

## ​ Analyzing sessions

- Understanding why a session didn’t complete as expected

- Identifying what worked well in a successful session

- Extracting patterns and insights from multiple sessions

```
This session used 42 ACUs to add pagination to GET /api/users. I expected ~12. Break down where Devin spent the most time, what dead ends it tried, and give me a revised prompt that would avoid these issues.
```

```
This session used 42 ACUs to add pagination to GET /api/users. I expected ~12. Break down where Devin spent the most time, what dead ends it tried, and give me a revised prompt that would avoid these issues.
```

## ​ Creating and improving playbooks

```
This session diagnosed and fixed a memory leak in our payments service. Create a reusable hotfix playbook for memory-leak incidents that any on-call engineer can attach to a new session.
```

```
This session diagnosed and fixed a memory leak in our payments service. Create a reusable hotfix playbook for memory-leak incidents that any on-call engineer can attach to a new session.
```

```
Our !db-migration playbook keeps failing on foreign key constraints. Here are 4 recent sessions — analyze the failures, compare them to the successes, and update the playbook to handle FK dependencies.
```

```
Our !db-migration playbook keeps failing on foreign key constraints. Here are 4 recent sessions — analyze the failures, compare them to the successes, and update the playbook to handle FK dependencies.
```

## ​ Managing knowledge

- Find and merge duplicate knowledge entries

- Resolve conflicting guidance

- Create new knowledge from codebase patterns

```
Review all knowledge entries and identify duplicates or highly similar entries. For each set of duplicates, propose a consolidated version.
```

```
Review all knowledge entries and identify duplicates or highly similar entries. For each set of duplicates, propose a consolidated version.
```

## ​ Managing schedules

```
Create a schedule that runs every Monday at 8 AM to review pending knowledge suggestions, deduplicate entries, and resolve conflicting guidance.
```

```
Create a schedule that runs every Monday at 8 AM to review pending knowledge suggestions, deduplicate entries, and resolve conflicting guidance.
```

## ​ Best practices

### ​ Analyzing sessions effectively

- “Why did Devin choose this approach instead of the alternative?”

- “What caused the test failures in this session?”

- “What patterns can we extract to create a playbook?”

### ​ Creating useful playbooks

- Provide multiple successful sessions if available to help Devin identify common patterns

- Describe the intended audience and use case for the playbook

- Specify any constraints or requirements that should be included

### ​ Managing knowledge at scale

- Start with deduplication to reduce noise

- Then resolve conflicts to ensure consistency

- Finally, fill gaps by creating knowledge from codebase analysis

## ​ Using these features via the Devin MCP

### ​ Session management

### ​ Playbook management

### ​ Knowledge management

### ​ Schedule management

### ​ Integration management

### ​ Repository documentation

## ​ Permissions

```
UseDevinExpert
```

```
org_member
```

```
org_admin
```
