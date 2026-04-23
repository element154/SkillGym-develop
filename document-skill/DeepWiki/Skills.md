# Skills - Devin Docs

Source: https://docs.devin.ai/product-guides/skills

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

- What are Skills?

- Why Skills Matter

- Devin Suggests Skills Automatically

- Examples

- Testing before opening a PR

- Deploying to an environment

- Investigating a part of the codebase

- Skill Discovery

- Supported Skill File Locations

- What Devin Loads from a Skill File

- Dynamic content

- How Devin Uses Skills

- Automatic invocation

- Mention a skill in your prompt

- One active skill at a time

- Searching and listing

- Limitations

- Skills vs. Playbooks

- Learn More

# Skills

Teach Devin reusable procedures by committing SKILL.md files to your repos

## ​ What are Skills?

```
SKILL.md
```

```
.agents/skills/<skill-name>/SKILL.md
```

## ​ Why Skills Matter

- Should be done the same way every time — testing checklists, deployment steps, review procedures

- Requires repo-specific knowledge — which services to start, what ports to use, which commands to run

- Benefits from dynamic context — pulling in git diffs, branch names, or environment info at invocation time

## ​ Devin Suggests Skills Automatically

- A summary of what was learned (e.g. “how to start the backend with Docker”)

- The proposed SKILL.md file contents

```
SKILL.md
```

- A “Create PR” button to commit the skill to your repo

## ​ Examples

### ​ Testing before opening a PR

```
--- name : test-before-pr description : Run the local dev server and verify pages before opening any PR that touches frontend code. --- ## Setup 1. Install dependencies: `npm install` 2. Start the database: `docker-compose up -d postgres` 3. Run migrations: `npx prisma migrate dev` 4. Start the dev server: `npm run dev` 5. Wait for "Ready on http://localhost:3000" ## Verify 1. Read the git diff to identify which pages changed 2. Open each affected page in the browser 3. Check for: console errors, layout issues, broken links 4. Screenshot each page at desktop (1280px) and mobile (375px) widths ## Before Opening the PR 1. Run `npm run lint` and fix any issues 2. Run `npm test` and confirm all tests pass 3. Include screenshots in the PR description
```

```
--- name : test-before-pr description : Run the local dev server and verify pages before opening any PR that touches frontend code. --- ## Setup 1. Install dependencies: `npm install` 2. Start the database: `docker-compose up -d postgres` 3. Run migrations: `npx prisma migrate dev` 4. Start the dev server: `npm run dev` 5. Wait for "Ready on http://localhost:3000" ## Verify 1. Read the git diff to identify which pages changed 2. Open each affected page in the browser 3. Check for: console errors, layout issues, broken links 4. Screenshot each page at desktop (1280px) and mobile (375px) widths ## Before Opening the PR 1. Run `npm run lint` and fix any issues 2. Run `npm test` and confirm all tests pass 3. Include screenshots in the PR description
```

### ​ Deploying to an environment

```
--- name : deploy description : Deploy the app to a target environment and run smoke tests. argument-hint : <environment> triggers : [ "user" ] --- ## Deploy 1. Make sure you are on the correct branch for this deploy 2. Run `./scripts/deploy.sh $0` 3. Wait for the deploy script to complete successfully ## Verify 1. Curl `https://$0.example.com/health` and confirm a 200 response 2. Run the smoke test suite: `npm run test:smoke -- --env=$0` 3. Report the deployment URL and test results ## Current context - Branch: ! `git branch --show-current` - Last commit: ! `git log --oneline -1`
```

```
--- name : deploy description : Deploy the app to a target environment and run smoke tests. argument-hint : <environment> triggers : [ "user" ] --- ## Deploy 1. Make sure you are on the correct branch for this deploy 2. Run `./scripts/deploy.sh $0` 3. Wait for the deploy script to complete successfully ## Verify 1. Curl `https://$0.example.com/health` and confirm a 200 response 2. Run the smoke test suite: `npm run test:smoke -- --env=$0` 3. Report the deployment URL and test results ## Current context - Branch: ! `git branch --show-current` - Last commit: ! `git log --oneline -1`
```

```
@skills:deploy staging
```

```
staging
```

```
$ARGUMENTS
```

```
$0
```

```
!`command`
```

```
triggers: ["user"]
```

### ​ Investigating a part of the codebase

```
--- name : investigate description : Research a part of the codebase and produce a written summary with file references. allowed-tools : Read, Grep, ListDir argument-hint : <topic or area to investigate> --- ## Research 1. Search the codebase for files related to: $ARGUMENTS 2. Read the most relevant files thoroughly 3. Trace the call chain and data flow ## Summarize 1. Write a summary of how $ARGUMENTS works 2. Include specific file paths and line numbers for every claim 3. Note any concerns, edge cases, or areas that need attention
```

```
--- name : investigate description : Research a part of the codebase and produce a written summary with file references. allowed-tools : Read, Grep, ListDir argument-hint : <topic or area to investigate> --- ## Research 1. Search the codebase for files related to: $ARGUMENTS 2. Read the most relevant files thoroughly 3. Trace the call chain and data flow ## Summarize 1. Write a summary of how $ARGUMENTS works 2. Include specific file paths and line numbers for every claim 3. Note any concerns, edge cases, or areas that need attention
```

```
allowed-tools
```

## ​ Skill Discovery

- Indexed repos — Devin’s backend indexes SKILL.md files across all repositories connected to your organization. These are available immediately when a session starts, before any repos are cloned.

```
SKILL.md
```

- Cloned repos — As repositories are cloned onto the session’s machine, Devin scans them for SKILL.md files on disk. Disk-scanned skills update or override any matching indexed skill from the same repo, ensuring Devin always uses the latest version on the branch being worked on.

```
SKILL.md
```

### ​ Supported Skill File Locations

```
SKILL.md
```

- .agents/skills/<skill-name>/SKILL.md (recommended)

```
.agents/skills/<skill-name>/SKILL.md
```

- .github/skills/<skill-name>/SKILL.md

```
.github/skills/<skill-name>/SKILL.md
```

- .claude/skills/<skill-name>/SKILL.md

```
.claude/skills/<skill-name>/SKILL.md
```

- .cursor/skills/<skill-name>/SKILL.md

```
.cursor/skills/<skill-name>/SKILL.md
```

- .codex/skills/<skill-name>/SKILL.md

```
.codex/skills/<skill-name>/SKILL.md
```

- .cognition/skills/<skill-name>/SKILL.md

```
.cognition/skills/<skill-name>/SKILL.md
```

- .windsurf/skills/<skill-name>/SKILL.md

```
.windsurf/skills/<skill-name>/SKILL.md
```

### ​ What Devin Loads from a Skill File

```
---
```

```
name
```

```
description
```

```
allowed-tools
```

```
argument-hint
```

```
triggers
```

```
["user", "model"]
```

```
["user"]
```

### ​ Dynamic content

- $ARGUMENTS — replaced with the full arguments string passed when the skill is invoked (e.g. via @skills:deploy staging prod ). You can also access individual arguments by index: $ARGUMENTS[0] or $0 for the first, $ARGUMENTS[1] or $1 for the second, etc. Arguments are split by whitespace.

```
$ARGUMENTS
```

```
@skills:deploy staging prod
```

```
$ARGUMENTS[0]
```

```
$0
```

```
$ARGUMENTS[1]
```

```
$1
```

- !`command` — the command is executed in the repo root and replaced with its stdout, letting skills include dynamic values like branch names or port numbers.

```
!`command`
```

## ​ How Devin Uses Skills

```
SKILL.md
```

### ​ Automatic invocation

```
test-before-pr
```

```
triggers: ["user"]
```

### ​ Mention a skill in your prompt

```
@skills:skill-name
```

```
Fix the login bug on the /auth page @skills:test-before-pr
```

```
Fix the login bug on the /auth page @skills:test-before-pr
```

```
@skills:deploy staging
```

```
@skills:deploy staging
```

```
$ARGUMENTS
```

```
$ARGUMENTS[0]
```

```
$1
```

### ​ One active skill at a time

### ​ Searching and listing

## ​ Limitations

- Global / org-level skills — Today, skills live inside repositories. For org-wide skills, you can create a dedicated “skills” repo as a workaround. We’re exploring first-class support for org-level skills that apply across all repos.

- Composing multiple skills — Currently only one skill can be active at a time. We’re working on support for chaining and composing workflows.

## ​ Skills vs. Playbooks

```
SKILL.md
```

```
@skills:name
```

## ​ Learn More

- Agent Skills specification — the open standard for SKILL.md file format, frontmatter fields, and directory structure

```
SKILL.md
```

- Knowledge — for contextual tips and facts (not step-by-step procedures)

- Playbooks — for reusable prompt templates attached to sessions
