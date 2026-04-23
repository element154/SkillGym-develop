# DeepWiki MCP - Devin Docs

Source: https://docs.devin.ai/work-with-devin/deepwiki-mcp

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

- DeepWiki MCP Server

- Available Tools

- Wire Protocols

- Streamable HTTP - /mcp

- SSE (Server-Sent Events) - /sse

- Setup Instructions

- For most clients (e.g. Windsurf, Cursor):

- For Claude Code:

- Related Resources

# DeepWiki MCP

How to use the official DeepWiki MCP server

## ​ What is MCP?

## ​ DeepWiki MCP Server

```
https://mcp.deepwiki.com/
```

### ​ Available Tools

- read_wiki_structure - Get a list of documentation topics for a GitHub repository

```
read_wiki_structure
```

- read_wiki_contents - View documentation about a GitHub repository

```
read_wiki_contents
```

- ask_question - Ask any question about a GitHub repository and get an AI-powered, context-grounded response

```
ask_question
```

### ​ Wire Protocols

#### ​ Streamable HTTP - /mcp

```
/mcp
```

- URL: https://mcp.deepwiki.com/mcp

```
https://mcp.deepwiki.com/mcp
```

- Works with Cloudflare, OpenAI, and Claude

- Recommended for most integrations

#### ​ SSE (Server-Sent Events) - /sse

```
/sse
```

- URL: https://mcp.deepwiki.com/sse

```
https://mcp.deepwiki.com/sse
```

- Legacy protocol, being deprecated

```
/mcp
```

## ​ Setup Instructions

### ​ For most clients (e.g. Windsurf, Cursor):

```
{ "mcpServers" : { "deepwiki" : { "serverUrl" : "https://mcp.deepwiki.com/mcp" } } }
```

```
{ "mcpServers" : { "deepwiki" : { "serverUrl" : "https://mcp.deepwiki.com/mcp" } } }
```

### ​ For Claude Code:

```
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
```

```
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
```

## ​ Related Resources

- Devin’s MCP Marketplace

- Connecting remote MCP servers to Claude

- OpenAI’s docs for using the DeepWiki MCP server

- DeepWiki

- Ask Devin
