# Devin MCP - Devin Docs

Source: https://docs.devin.ai/work-with-devin/devin-mcp

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

- What is MCP?

- Devin MCP Server

- Authentication Required

- Available Tools

- Repository Documentation

- Session Management

- Playbook Management

- Knowledge Management

- Schedule Management

- Integration Management

- Wire Protocols

- Key Differences from DeepWiki MCP

- Setup Instructions

- For most clients (e.g. Windsurf):

- For Claude Code:

- Related Resources

# Devin MCP

How to use the official Devin MCP server for private and public repositories

## ​ What is MCP?

## ​ Devin MCP Server

```
https://mcp.devin.ai/
```

### ​ Authentication Required

- Sign up for a Devin account at Devin.ai

- Generate an API key from your account settings

- Include the API key in your MCP client configuration

## ​ Available Tools

### ​ Repository Documentation

```
read_wiki_structure
```

```
read_wiki_contents
```

```
ask_question
```

```
list_available_repos
```

### ​ Session Management

```
devin_session_create
```

```
devin_session_search
```

```
devin_session_interact
```

```
devin_session_events
```

```
devin_session_gather
```

### ​ Playbook Management

```
devin_playbook_manage
```

```
!my_macro
```

### ​ Knowledge Management

```
devin_knowledge_manage
```

### ​ Schedule Management

```
devin_schedule_manage
```

### ​ Integration Management

```
list_integrations
```

## ​ Wire Protocols

- URL: https://mcp.devin.ai/mcp

```
https://mcp.devin.ai/mcp
```

- Works with HTTP-compatible clients

- Recommended for all integrations

```
/sse
```

```
/mcp
```

## ​ Key Differences from DeepWiki MCP

```
https://mcp.deepwiki.com/
```

```
https://mcp.devin.ai/
```

## ​ Setup Instructions

### ​ For most clients (e.g. Windsurf):

```
{ "mcpServers" : { "devin" : { "serverUrl" : "https://mcp.devin.ai/mcp" , "headers" : { "Authorization" : "Bearer <API_KEY>" } } } }
```

```
{ "mcpServers" : { "devin" : { "serverUrl" : "https://mcp.devin.ai/mcp" , "headers" : { "Authorization" : "Bearer <API_KEY>" } } } }
```

### ​ For Claude Code:

```
claude mcp add -s user -t http devin https://mcp.devin.ai/mcp -H "Authorization: Bearer <API_KEY>"
```

```
claude mcp add -s user -t http devin https://mcp.devin.ai/mcp -H "Authorization: Bearer <API_KEY>"
```

## ​ Related Resources

- Advanced Capabilities — Overview of Devin’s advanced features

- Devin’s MCP Marketplace

- Connecting remote MCP servers to Claude

- OpenAI’s docs for using MCP servers

- DeepWiki MCP — For public repositories only

- DeepWiki

- Ask Devin
