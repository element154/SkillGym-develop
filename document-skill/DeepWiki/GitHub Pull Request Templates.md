# GitHub Pull Request Templates - Devin Docs

Source: https://docs.devin.ai/integrations/pr-templates

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

- Pull Request Templates

- 1. Discovery Order

- 2. Custom Devin Template (optional)

- 3. Built‑in Default (if no file found)

- 4. GitHub Reference

# GitHub Pull Request Templates

How Devin discovers and uses GitHub-style pull request templates, including the custom Devin template filename.

# ​ Pull Request Templates

## ​ 1. Discovery Order

```
PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md docs/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md PULL_REQUEST_TEMPLATE/devin_pr_template.md docs/PULL_REQUEST_TEMPLATE/devin_pr_template.md .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md PULL_REQUEST_TEMPLATE.md pull_request_template.md docs/PULL_REQUEST_TEMPLATE.md docs/pull_request_template.md .github/PULL_REQUEST_TEMPLATE.md .github/pull_request_template.md
```

```
PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md docs/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md PULL_REQUEST_TEMPLATE/devin_pr_template.md docs/PULL_REQUEST_TEMPLATE/devin_pr_template.md .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md PULL_REQUEST_TEMPLATE.md pull_request_template.md docs/PULL_REQUEST_TEMPLATE.md docs/pull_request_template.md .github/PULL_REQUEST_TEMPLATE.md .github/pull_request_template.md
```

```
DEVIN_PR_TEMPLATE.md
```

```
devin_pr_template.md
```

```
PULL_REQUEST_TEMPLATE.md
```

```
pull_request_template.md
```

## ​ 2. Custom Devin Template (optional)

```
.github/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md docs/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md docs/PULL_REQUEST_TEMPLATE/devin_pr_template.md PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md PULL_REQUEST_TEMPLATE/devin_pr_template.md
```

```
.github/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md docs/PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md docs/PULL_REQUEST_TEMPLATE/devin_pr_template.md PULL_REQUEST_TEMPLATE/DEVIN_PR_TEMPLATE.md PULL_REQUEST_TEMPLATE/devin_pr_template.md
```

```
PULL_REQUEST_TEMPLATE.md
```

```
pull_request_template.md
```

```
.github/pull_request_template.md
```

```
.github/pull_request_template.md
```

## ​ 3. Built‑in Default (if no file found)

- Summary

- Review & Testing Checklist

- (Optional) Mermaid diagram

- Notes

## ​ 4. GitHub Reference

```
mkdir -p .github/PULL_REQUEST_TEMPLATE echo "# [title]\n\n## Summary\n...\n" > .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md
```

```
mkdir -p .github/PULL_REQUEST_TEMPLATE echo "# [title]\n\n## Summary\n...\n" > .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md
```
