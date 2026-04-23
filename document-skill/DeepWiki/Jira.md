# Jira - Devin Docs

Source: https://docs.devin.ai/integrations/jira

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

- How to trigger Devin from Jira

- Assign the ticket to Devin

- Add a playbook label

- Add the “devin” label

- @mention Devin in a comment

- Configuring the integration

- Session mode

- Playbook labels

- Automation triggers

- Enterprise: Jira project mapping

- Interacting with Devin in Jira

- Connecting a service account

# Jira

Assign Jira tickets to Devin and turn them into PRs

## ​ Setting up the integration

- In your Devin account at app.devin.ai, go to Settings > Integrations > Jira , and click “Connect”.

- You’ll be redirected to Jira to review permissions and grant Devin access.

- Once connected, configure your playbook labels and optionally set up automation triggers in the settings page.

## ​ How to trigger Devin from Jira

### ​ Assign the ticket to Devin

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

### ​ Add the “devin” label

```
devin
```

```
devin
```

```
Devin
```

```
devin-workshop
```

```
devin-task
```

```
devinworkshop
```

```
devin_workshop
```

### ​ @mention Devin in a comment

```
@Devin
```

## ​ Configuring the integration

### ​ Session mode

- Direct session creation (enabled by default): Devin creates a full session and works on the issue, posting updates back to Jira.

- Scoping only (disabled): Devin only analyzes the ticket and posts a scoping comment with a summary, implementation plan, and confidence estimate. You can then click the provided link to start a session manually.

### ​ Playbook labels

```
!plan
```

- Default playbook : One playbook is marked as the default. When a ticket is triggered without a specific playbook label (e.g. with just the devin label or by assigning the ticket to Devin), Devin uses this default playbook.

```
devin
```

- Adding playbooks : Click “Add playbook” to add additional playbooks. Only playbooks with a macro can be added.

- Removing playbooks : Remove a playbook to stop using its label as a trigger.

### ​ Automation triggers

- Projects : Only trigger for tickets in specific Jira projects.

- Labels : Only trigger when a ticket has specific labels.

- Statuses : Only trigger when a ticket reaches a specific status (e.g. “To Do”, “In Progress”).

- Playbook : Optionally specify which playbook Devin should use for the triggered session.

### ​ Enterprise: Jira project mapping

## ​ Interacting with Devin in Jira

- PR links : When Devin creates a pull request, the PR URL is automatically added as a remote link on the Jira issue and posted as a comment.

- Session link : A direct link to the Devin session in the web app is provided so you can follow progress in real time.

- Follow-up messages : Mention @Devin in a comment to give Devin additional instructions or ask questions.

```
@Devin
```

## ​ Connecting a service account

- In your Atlassian organization’s admin settings, create an OAuth 2.0 service account with the following Classic scopes : read:me read:jira-user read:jira-work write:jira-work

- read:me

```
read:me
```

- read:jira-user

```
read:jira-user
```

- read:jira-work

```
read:jira-work
```

- write:jira-work

```
write:jira-work
```

- In Settings > Integrations > Jira , click Connect service account and enter the client ID and client secret.
