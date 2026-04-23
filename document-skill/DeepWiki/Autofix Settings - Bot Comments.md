# Autofix Settings - Bot Comments - Devin Docs

Source: https://docs.devin.ai/product-guides/bot-comment-settings

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

- Overview

- Where to find it

- Available modes

- Don’t respond to bot comments (default)

- Respond to all bot comments

- Respond to specific bots only

- How it works at runtime

- Common use cases

- Interaction with Devin Review

- Interaction with mention-only mode

- Tips

# Autofix Settings - Bot Comments

Control which bots Devin responds to on pull requests

## ​ Overview

```
github-actions[bot]
```

```
dependabot[bot]
```

## ​ Where to find it

## ​ Available modes

### ​ Don’t respond to bot comments (default)

### ​ Respond to all bot comments

### ​ Respond to specific bots only

- Select Respond to specific bots only from the dropdown.

- Enter the bot’s GitHub username in the input field (e.g., github-actions[bot] ).

```
github-actions[bot]
```

- Click Add .

```
[bot]
```

```
GitHub-Actions[bot]
```

```
github-actions[bot]
```

## ​ How it works at runtime

- Mode is “none” — the comment is ignored.

- Mode is “allowlist” — the bot’s username is checked against your allowlist. If it matches, Devin processes the comment. Otherwise, it is ignored.

- Mode is “all” — the comment is processed.

## ​ Common use cases

- CI bots : Allow your CI bot so Devin can automatically fix lint errors, test failures, or build issues flagged by your pipeline.

- Security scanners : Allow your security scanning bot so Devin can address vulnerability reports directly.

- Code quality tools : Allow bots like SonarQube or Codacy so Devin can respond to code quality feedback.

## ​ Interaction with Devin Review

```
devin-ai-integration[bot]
```

- Set the mode to “Respond to specific bots only” and add devin-ai-integration[bot] to the allowlist.

```
devin-ai-integration[bot]
```

- Set the mode to “Respond to all bot comments” .

## ​ Interaction with mention-only mode

```
DevinAI
```

```
@devin
```

## ​ Tips

- Start with “Respond to specific bots only” and add bots one at a time. This lets you verify that each bot interacts well with Devin before adding more.

- If you notice unexpected loops, switch back to “Don’t respond to bot comments” to stop them immediately.

- Bot users are identified by their GitHub user type ( Bot ), not by their username. Human users with [bot] in their name are not affected by this setting.

```
Bot
```

```
[bot]
```
