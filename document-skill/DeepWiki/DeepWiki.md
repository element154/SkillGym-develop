# DeepWiki - Devin Docs

Source: https://docs.devin.ai/work-with-devin/deepwiki

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

- Overview

- For Public Repos

- Steering DeepWiki

- Configuration Format

- Configuration Options

- repo_notes (Array)

- pages (Array, optional)

- Validation Limits

- Practical Examples

- Example 1: Repo Notes to Guide Wiki Generation

- Example 2: Ensuring Specific Folders Are Documented

- Example 3: Addressing Missing Components

- Example 4: Hierarchical Documentation Structure

- Best Practices

- 1. Use Repo Notes Strategically

- 2. Organize Pages Logically

- 3. Be Specific in Page Purposes

- 4. Address Known Gaps

- Troubleshooting Common Issues

- ”Only certain folders are being documented”

- ”Important components are missing from the wiki”

- Getting Started

# DeepWiki

Architecture diagrams, documentation, links to sources, and more for all your repos

## ​ Overview

## ​ For Public Repos

## ​ Steering DeepWiki

```
.devin/wiki.json
```

```
.devin/wiki.json
```

```
repo_notes
```

```
pages
```

```
pages
```

## ​ Configuration Format

```
.devin/wiki.json
```

```
{ "repo_notes" : [ { "content" : "This repository contains the main UI components in the cui/ folder, which should be prioritized in documentation" , "author" : "Team Lead" } ], "pages" : [ { "title" : "CUI Components Overview" , "purpose" : "Document the cui/ folder structure and main UI components" , "parent" : null }, { "title" : "Authentication System" , "purpose" : "Document the authentication flow and related components" , "parent" : null }, { "title" : "Login Components" , "purpose" : "Detailed documentation of login-related UI components" , "parent" : "Authentication System" } ] }
```

```
{ "repo_notes" : [ { "content" : "This repository contains the main UI components in the cui/ folder, which should be prioritized in documentation" , "author" : "Team Lead" } ], "pages" : [ { "title" : "CUI Components Overview" , "purpose" : "Document the cui/ folder structure and main UI components" , "parent" : null }, { "title" : "Authentication System" , "purpose" : "Document the authentication flow and related components" , "parent" : null }, { "title" : "Login Components" , "purpose" : "Detailed documentation of login-related UI components" , "parent" : "Authentication System" } ] }
```

## ​ Configuration Options

### ​ repo_notes (Array)

- content (string, required): The note content (max 10,000 characters)

- author (string, optional): Who wrote the note

### ​ pages (Array, optional)

- title (string, required): The page title (must be unique and non-empty)

- purpose (string, required): What this page should document

- parent (string, optional): Title of the parent page for hierarchical organization

- page_notes (array, optional): Additional notes specific to this page

### ​ Validation Limits

- Maximum 30 pages (80 for enterprise)

- Maximum 100 total notes (repo_notes + all page_notes combined)

- Maximum 10,000 characters per note

- Page titles must be unique and non-empty

## ​ Practical Examples

### ​ Example 1: Repo Notes to Guide Wiki Generation

```
{ "repo_notes" : [ { "content" : "The repository contains three main areas: the frontend/ folder with React components, the backend/ folder with API services, and the infra/ folder with deployment scripts. Documentation should emphasize how these parts interact and highlight the backend API layer as the highest priority." } ] }
```

```
{ "repo_notes" : [ { "content" : "The repository contains three main areas: the frontend/ folder with React components, the backend/ folder with API services, and the infra/ folder with deployment scripts. Documentation should emphasize how these parts interact and highlight the backend API layer as the highest priority." } ] }
```

### ​ Example 2: Ensuring Specific Folders Are Documented

```
{ "repo_notes" : [ { "content" : "The cui/ folder contains critical UI components that must be documented. The backend/ folder contains the main API logic. The utils/ folder has shared utilities used throughout the codebase." } ] }
```

```
{ "repo_notes" : [ { "content" : "The cui/ folder contains critical UI components that must be documented. The backend/ folder contains the main API logic. The utils/ folder has shared utilities used throughout the codebase." } ] }
```

### ​ Example 3: Addressing Missing Components

```
{ "repo_notes" : [ { "content" : "The testing/ directory contains important test utilities and patterns that developers need to understand. The scripts/ directory has deployment and maintenance scripts that are crucial for operations." } ] }
```

```
{ "repo_notes" : [ { "content" : "The testing/ directory contains important test utilities and patterns that developers need to understand. The scripts/ directory has deployment and maintenance scripts that are crucial for operations." } ] }
```

### ​ Example 4: Hierarchical Documentation Structure

```
{ "repo_notes" : [ { "content" : "This is a full-stack application with distinct frontend, backend, and shared components that should be documented separately but with clear relationships." } ], "pages" : [ { "title" : "Architecture Overview" , "purpose" : "High-level overview of the application architecture and how components interact" }, { "title" : "Frontend" , "purpose" : "Frontend application structure and components" , "parent" : "Architecture Overview" }, { "title" : "React Components" , "purpose" : "Detailed documentation of React components, their props, and usage" , "parent" : "Frontend" }, { "title" : "State Management" , "purpose" : "How application state is managed, including stores and data flow" , "parent" : "Frontend" }, { "title" : "Backend" , "purpose" : "Backend services, APIs, and data layer" , "parent" : "Architecture Overview" }, { "title" : "API Endpoints" , "purpose" : "REST API documentation including endpoints, request/response formats" , "parent" : "Backend" } ] }
```

```
{ "repo_notes" : [ { "content" : "This is a full-stack application with distinct frontend, backend, and shared components that should be documented separately but with clear relationships." } ], "pages" : [ { "title" : "Architecture Overview" , "purpose" : "High-level overview of the application architecture and how components interact" }, { "title" : "Frontend" , "purpose" : "Frontend application structure and components" , "parent" : "Architecture Overview" }, { "title" : "React Components" , "purpose" : "Detailed documentation of React components, their props, and usage" , "parent" : "Frontend" }, { "title" : "State Management" , "purpose" : "How application state is managed, including stores and data flow" , "parent" : "Frontend" }, { "title" : "Backend" , "purpose" : "Backend services, APIs, and data layer" , "parent" : "Architecture Overview" }, { "title" : "API Endpoints" , "purpose" : "REST API documentation including endpoints, request/response formats" , "parent" : "Backend" } ] }
```

## ​ Best Practices

### ​ 1. Use Repo Notes Strategically

- Provide context about which parts of your codebase are most important

- Mention specific folders or components that should be prioritized

- Explain relationships between different parts of your system

### ​ 2. Organize Pages Logically

- Start with high-level overview pages

- Use parent-child relationships to create clear hierarchies

- Group related functionality together

### ​ 3. Be Specific in Page Purposes

- Clearly state what each page should document

- Mention specific directories, files, or concepts to focus on

- Provide enough detail for the system to understand your intent

### ​ 4. Address Known Gaps

- If you know certain parts of your codebase are being missed, explicitly include them

- Use descriptive titles that make it clear what should be covered

## ​ Troubleshooting Common Issues

### ​ ”Only certain folders are being documented”

```
.devin/wiki.json
```

### ​ ”Important components are missing from the wiki”

```
{ "repo_notes" : [ { "content" : "The [missing-component] directory is critical to the application and must be documented thoroughly." } ], "pages" : [ { "title" : "Critical Component Name" , "purpose" : "Document the [missing-component] directory and its functionality" } ] }
```

```
{ "repo_notes" : [ { "content" : "The [missing-component] directory is critical to the application and must be documented thoroughly." } ], "pages" : [ { "title" : "Critical Component Name" , "purpose" : "Document the [missing-component] directory and its functionality" } ] }
```

## ​ Getting Started

- Create .devin/wiki.json in your repository root

```
.devin/wiki.json
```

- Add repo_notes explaining your codebase structure and priorities

- If necessary, specify all pages you want created with clear titles and purposes

- Commit the file and regenerate your wiki
