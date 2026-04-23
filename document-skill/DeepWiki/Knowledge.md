# Knowledge - Devin Docs

Source: https://docs.devin.ai/product-guides/knowledge

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

- What is Knowledge?

- How do I create Knowledge?

- Macros

- Enabling and disabling Knowledge

- Knowledge Suggestions

- What belongs in Knowledge?

- Organizing Knowledge with Folders

- Tips and tricks

- Organization and Enterprise Knowledge

- Promoting Organization Knowledge to Enterprise

- Pinning Knowledge to Repos

# Knowledge

Share important context and knowledge to help Devin get onboarded

## ​ What is Knowledge?

## ​ How do I create Knowledge?

### ​ Macros

```
!
```

```
!deploy-checklist
```

### ​ Enabling and disabling Knowledge

## ​ Knowledge Suggestions

## ​ What belongs in Knowledge?

## ​ Organizing Knowledge with Folders

- Nested hierarchy — Create sub-folders to build a structured knowledge tree.

- Bulk enable/disable — Toggle an entire folder on or off. When a folder is disabled, all knowledge items inside it are disabled for your sessions.

- Move items — Drag knowledge items between folders, or use the move action to reorganize.

- Auto-organize — Select multiple knowledge items and let Devin automatically sort them into logical folders.

## ​ Tips and tricks

- Create specific Knowledge that is targeted at one workflow or action. Devin will read the entire Knowledge contents, so keep it all relevant and up-to-date! Split up your Knowledge into smaller ones where possible. Devin is capable of accessing multiple Knowledge “items” at once.

- Split up your Knowledge into smaller ones where possible. Devin is capable of accessing multiple Knowledge “items” at once.

- Make a habit of adding and updating Knowledge. These are shared across your organization, and will continually improve Devin for your team over time.

- Devin retrieves Knowledge when relevant, not all at once or all at the beginning. Be sure to make your retrieval trigger highly relevant to the contents.

- Use folders to group related knowledge (e.g., by project, team, or workflow) so you can quickly enable or disable sets of knowledge as your focus changes.

## ​ Organization and Enterprise Knowledge

- Organization Knowledge — Knowledge items scoped to your current organization. These are visible to all members of the organization and are the default scope for new knowledge items.

- Suggestions — AI-generated knowledge suggestions based on your session interactions (shown for non-primary organizations).

- Enterprise Knowledge — Knowledge items that apply across all organizations in your enterprise. Only visible when you belong to an enterprise account. Enterprise admins can create and manage enterprise-level knowledge from this tab.

### ​ Promoting Organization Knowledge to Enterprise

## ​ Pinning Knowledge to Repos

- Pinning to no repo : The Knowledge is only retrieved when Devin decides it’s relevant to your current context.

- Pinning to a specific repo : The Knowledge is always used whenever Devin is working in that specific repo.

- Pinning to all repos : The Knowledge automatically applies to every repo that Devin is working on in any session.
