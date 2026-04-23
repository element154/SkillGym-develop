# Devin Session Tools - Devin Docs

Source: https://docs.devin.ai/work-with-devin/devin-session-tools

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

- Progress Tab

- Shell & Terminal

- Command history features

- View shell updates

- Shell command history

- Running your own commands

- Devin IDE

- Reviewing Devin’s work in real-time

- Taking over Devin’s task

- IDE best practices

- Interactive Browser

- Browser use cases

- Cookie persistence

- Integration & Workflow

- Typical workflow

- Best Practices

- When to use each tool

- Tips for effective collaboration

# Devin Session Tools

Complete guide to Devin’s IDE, Browser, and Shell tools

## ​ Progress Tab

## ​ Shell & Terminal

### ​ Command history features

- Full command list : View every command Devin has executed during the session

- Output preview : See the output of each command without switching contexts

- Copy functionality : Quickly copy commands and outputs to your clipboard

- Time navigation : Jump to different points in the session by clicking on commands

- Integration with progress updates : Shell commands are linked to Devin’s progress updates for context

### ​ View shell updates

### ​ Shell command history

### ​ Running your own commands

- Open a terminal in VSCode to run commands directly

- Toggle terminals from read-only to writable mode

- Run any commands you need to debug, test, or configure the environment

## ​ Devin IDE

### ​ Reviewing Devin’s work in real-time

### ​ Taking over Devin’s task

- Cmd/Ctrl+K to generate terminal commands from natural language

- Cmd/Ctrl+I for rapid responses to questions or rapid file edits

- Tab autocomplete for code completion

### ​ IDE best practices

- Let Devin know about the changes you’ve made when you resume the session

- Make sure that Devin is paused before taking over the IDE to avoid simultaneous, conflicting changes

- Use Devin’s browser to test the local build yourself, without leaving the webapp

## ​ Interactive Browser

### ​ Browser use cases

- Testing local applications : Test your application running on Devin’s machine directly in the browser

- Visual verification : Verify that UI changes look correct in the browser

- Screenshots and recordings : Devin can capture screenshots and videos of the browser and submit them back to you as proof of testing or to show results

- Authentication flows : Complete login steps, MFA challenges, or OAuth flows that Devin cannot handle automatically

- CAPTCHA solving : Manually solve CAPTCHAs when Devin encounters them

- Complex navigation : Help Devin navigate through complex web interfaces or multi-step forms

### ​ Cookie persistence

## ​ Integration & Workflow

### ​ Typical workflow

- Start a session and let Devin begin working

- Monitor progress using progress updates

- Check shell commands to understand what Devin is executing

- Review quick code changes in the IDE using the diff view

- Functional testing prototypes (for frontend development)

- Take over if needed by stopping Devin and using the IDE directly

- Resume Devin after making your changes and informing Devin what you did

## ​ Best Practices

### ​ When to use each tool

### ​ Tips for effective collaboration

- Intervene early : If you see Devin going in the wrong direction, stop and redirect early

- Leverage command history : Use shell command history to understand what Devin has tried and what worked

- Communicate changes : If resuming the session, always tell Devin about any changes you made when taking over
