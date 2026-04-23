# Linear - Devin Docs

Source: https://docs.devin.ai/integrations/linear

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

- Setting up the integration

- How to trigger Devin from Linear

- Assign Devin to a ticket

- Add a playbook label

- @mention Devin in a comment

- Configuring the integration

- Synced playbook labels

- Automation triggers

- Enterprise: Linear team mapping

- Interacting with Devin in Linear

- Connecting your Linear user account

# Linear

Assign Linear tickets to Devin and turn them into PRs

## ​ Setting up the integration

- In your Devin account at app.devin.ai, go to Settings > Integrations > Linear , and click “Connect”.

- You’ll be redirected to Linear to review permissions and grant Devin access. You can select which teams in Linear Devin will have access to. You can always change Devin’s access directly in the Linear Apps settings later.

- Once connected, configure your synced playbook labels and optionally set up automation triggers in the settings page.

## ​ How to trigger Devin from Linear

### ​ Assign Devin to a ticket

### ​ Add a playbook label

```
!plan
```

```
!implement
```

```
!triage
```

```
!review
```

### ​ @mention Devin in a comment

## ​ Configuring the integration

### ​ Synced playbook labels

```
!plan
```

- Default playbook : One playbook is marked as the default. When a ticket is assigned to Devin without a specific playbook label, Devin uses this default playbook. The !plan playbook is set as the default for new connections.

```
!plan
```

- Adding playbooks : Click “Add playbook” to sync additional playbooks. Only playbooks with a macro can be synced.

- Removing playbooks : Remove a playbook to stop syncing its label to Linear.

### ​ Automation triggers

- Teams : Only trigger for tickets in specific Linear teams.

- Labels : Only trigger when a ticket has specific labels.

- Statuses : Only trigger when a ticket reaches a specific status (e.g. “Todo”, “In Progress”).

- Playbook : Optionally specify which playbook Devin should use for the triggered session.

### ​ Enterprise: Linear team mapping

## ​ Interacting with Devin in Linear

- Activity feed : Devin posts real-time updates as it works, including commands run, files edited, and progress summaries.

- Plan tracking : Devin’s todo list syncs to Linear’s plan UI so you can see progress at a glance.

- Follow-up messages : Send messages in the agent session thread to give Devin additional instructions or ask questions.

- Stop Devin : Use the stop signal in Linear to put Devin to sleep on the current task.

- PR links : When Devin creates a pull request, the PR URL is automatically added to the agent session for easy access.

- Session link : A direct link to the Devin session in the web app is added to the agent session, along with a link to the playbook used (if applicable).

## ​ Connecting your Linear user account
