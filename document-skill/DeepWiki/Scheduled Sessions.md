# Scheduled Sessions - Devin Docs

Source: https://docs.devin.ai/product-guides/scheduled-sessions

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

- Creating a Scheduled Session

- From the input box

- From the Schedules settings page

- Configuring a Schedule

- Name

- Schedule type

- Agent

- Playbook (optional)

- Repositories (optional)

- Frequency (recurring schedules)

- Run at (one-time schedules)

- Email notifications

- Slack notifications

- Run as

- Prompt

- Managing Schedules

- Status

- Editing a schedule

- Pausing and resuming

- Deleting a schedule

- Viewing Past Sessions

- Use Cases

# Scheduled Sessions

Automate recurring or one-time Devin sessions that run on a schedule

## ​ Creating a Scheduled Session

### ​ From the input box

- Type your prompt in the Devin input box

- Click the three-dot menu (⋯) on the right side of the input box

- Select Schedule Devin

- You’ll be taken to the schedule creation page with your prompt pre-filled

### ​ From the Schedules settings page

- Navigate to Settings > Schedules in the sidebar

- Click Create schedule

- Fill in the schedule details

## ​ Configuring a Schedule

### ​ Name

### ​ Schedule type

- Recurring — Runs repeatedly on a cron-based frequency (default)

- One-time — Runs once at a specific date and time, then automatically disables itself

### ​ Agent

- Devin — Standard AI software engineer (default)

- Data Analyst — Optimized for data analysis and queries

- Advanced — For playbooks and session analysis

### ​ Playbook (optional)

### ​ Repositories (optional)

### ​ Frequency (recurring schedules)

- Hourly — Run every N hours

- Daily — Run at a specific time every day

- Weekly — Run at a specific time on selected days of the week

```
0 9 * * 1-5
```

### ​ Run at (one-time schedules)

### ​ Email notifications

- Always — Get notified after every run

- On failure only — Only get notified when a scheduled session fails (default)

- Never — No notifications

### ​ Slack notifications

### ​ Run as

### ​ Prompt

## ​ Managing Schedules

### ​ Status

- Active — The schedule is enabled and will run at its next scheduled time

- Paused — The schedule is disabled and will not run until re-enabled. One-time schedules are automatically paused after execution.

- Error — The schedule encountered consecutive failures

### ​ Editing a schedule

### ​ Pausing and resuming

### ​ Deleting a schedule

## ​ Viewing Past Sessions

## ​ Use Cases

- Daily standup reports — Summarize recent PRs, issues, or commits every morning

- Periodic dependency updates — Check for and apply dependency updates on a weekly basis

- Recurring data analysis — Generate reports or dashboards from your data at regular intervals

- Routine code maintenance — Run lint fixes, dead code removal, or test coverage checks on a schedule

- Monitoring and alerting — Periodically check system health or review logs for anomalies
