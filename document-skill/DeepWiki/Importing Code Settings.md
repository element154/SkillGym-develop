# Importing Code Settings - Devin Docs

Source: https://docs.devin.ai/collaborate-with-devin/vscode-profiles

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

- Auto-Import Settings

- Exporting Your Local Profile Manually

- Importing Your .code-profile File Manually

- Verifying that your upload worked

- Settings Sync

# Importing Code Settings

Use your local settings and extensions while working in Devin’s IDE

## ​ Auto-Import Settings

- Open any Devin session that you started

- You should be greeted by the Welcome page. (If this page does not appear, you can always reopen it with Cmd+Shift+P on Mac or Ctrl+Shift+P on Windows/Linux and search for “Help: Welcome”.)

```
Cmd+Shift+P
```

```
Ctrl+Shift+P
```

- Click the button to start the import flow.

- Follow the steps on the screen. You will copy paste a Python script to your local computer’s terminal to upload your profile. (PowerShell for Windows)

- The script will prompt you to confirm your settings by visiting the app.devin.ai URL.

- Once confirmed, your settings will be synced automatically to your Devin session and for all future Devin sessions!

## ​ Exporting Your Local Profile Manually

- Go to VS Code, Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux) -> Preferences: Open Profiles (UI)

```
Cmd+Shift+P
```

```
Ctrl+Shift+P
```

- Right click your profile (usually Default).

- Click Export and choose File in the quick pick that appears.

- Save the file to disk. This will get saved to a .code-profile file.

```
.code-profile
```

## ​ Importing Your .code-profile File Manually

```
.code-profile
```

- Open any Devin session that you started

- Open the command palette with Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux) and search for “Preferences: Devin: Import Profile (Manual)”.

```
Cmd+Shift+P
```

```
Ctrl+Shift+P
```

- Select the file you uploaded. This will upload your profile to the machine. All your extensions and settings should then be auto-installed.

## ​ Verifying that your upload worked

- Settings: open the command palette ( Cmd+Shift+P on Mac / Ctrl+Shift+P on Windows/Linux) and search for “Preferences: Open User Settings (JSON)”. Check that it matches your local editor’s.

```
Cmd+Shift+P
```

```
Ctrl+Shift+P
```

- Keyboard Shortcuts: open the command palette and search for “Preferences: Open Keyboard Shortcuts (JSON)”. Check that it matches your local editor’s.

- Extensions: Click the extensions icon in the sidebar on the right (or press Cmd+Shift+X on Mac / Ctrl+Shift+X on Windows/Linux). Search for the Extensions you have installed locally.

```
Cmd+Shift+X
```

```
Ctrl+Shift+X
```

## ​ Settings Sync
