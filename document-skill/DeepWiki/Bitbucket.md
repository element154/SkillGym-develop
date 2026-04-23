# Bitbucket - Devin Docs

Source: https://docs.devin.ai/integrations/bitbucket

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

- Why integrate Devin with Bitbucket?

- Prerequisites

- Setting up the Integration

- Bitbucket Cloud

- Bitbucket Data Center

- Using Devin with the Bitbucket Integration

- Best Practices

# Bitbucket

Work with Devin directly in your Bitbucket repositories

## ​ Why integrate Devin with Bitbucket?

## ​ Prerequisites

- Dedicated service account - Create a new Bitbucket account specifically for Devin (e.g., devin@yourcompany.com ) rather than using an existing user account for cleaner access management and audit trails

```
devin@yourcompany.com
```

## ​ Setting up the Integration

### ​ Bitbucket Cloud

- Create a new Bitbucket account specifically for Devin (just like you’d create a personal account). You’ll use this account, not your personal one, during the integration process.

- In your Devin account, go to Settings > Integrations > Bitbucket and click “Connect”.

- You’ll be redirected to Bitbucket where you should: Log in with the Bitbucket account you created for Devin (not your personal account) Grant the necessary permissions for Devin to work with your repositories

- Log in with the Bitbucket account you created for Devin (not your personal account)

- Grant the necessary permissions for Devin to work with your repositories

- Once completed, you’ll return to the Devin settings page where you can confirm the integration is active.

### ​ Bitbucket Data Center

- Create a dedicated service account in your Bitbucket Data Center instance for Devin.

- In your Devin account, go to Settings > Integrations > Bitbucket and select “Bitbucket Data Center”.

- Configure the connection by providing: Your Bitbucket Data Center URL Authentication credentials for the service account

- Your Bitbucket Data Center URL

- Authentication credentials for the service account

- Grant the service account appropriate project and repository permissions in your Bitbucket Data Center instance.

- Once configured, you’ll see the integration status confirmed in your Devin settings.

## ​ Using Devin with the Bitbucket Integration

## ​ Best Practices

- Create a dedicated Bitbucket account for Devin

- Enable branch protections on main/master branches

- Grant the service account appropriate workspace and repository permissions
