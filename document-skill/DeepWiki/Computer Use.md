# Computer Use - Devin Docs

Source: https://docs.devin.ai/work-with-devin/computer-use

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

- What Is Computer Use?

- How to Enable It

- When Computer Use Runs

- After creating a PR

- On request during a session

- Autonomously when appropriate

- What Devin Can Do with Computer Use

- Test web applications end-to-end

- Test desktop applications

- Visual verification

- Interact with complex UI flows

- Record testing sessions

- How Computer Use Works

- Computer Use and Testing

- Tips for Getting the Best Results

- Pre-configure access

- Create testing skills

- Scripted Browser Use via Playwright

- How it works

- Example: connecting to Devin’s browser

- When to use this

- Tips

- Troubleshooting

- Devin can’t find a UI element

- The app doesn’t render on Devin’s desktop

- Devin is clicking the wrong things

# Computer Use

How Devin uses a full desktop environment to interact with GUIs, test applications, and visually verify changes

## ​ What Is Computer Use?

- Web applications in Chrome (clicking buttons, filling forms, navigating pages)

- Desktop applications that run on Linux (Electron apps, native GUIs, IDEs)

- Terminal-based UIs (TUI programs, interactive CLIs)

- Any visual interface that can be displayed on the desktop

## ​ How to Enable It

- Go to Settings > Customization

- Under the Browser interaction section, toggle Enable desktop mode on

- Devin will now use its desktop environment during sessions

## ​ When Computer Use Runs

### ​ After creating a PR

### ​ On request during a session

- “Test the changes you just made and send me a recording”

- “Open the app in the browser and verify the login page works”

- “Launch the desktop app and check that the new menu item appears”

### ​ Autonomously when appropriate

## ​ What Devin Can Do with Computer Use

### ​ Test web applications end-to-end

### ​ Test desktop applications

### ​ Visual verification

### ​ Interact with complex UI flows

### ​ Record testing sessions

## ​ How Computer Use Works

- Takes a screenshot of the current screen to understand what’s visible

- Identifies interactive elements — buttons, text fields, menus, links — and decides what to interact with

- Performs an action — clicks, types, scrolls, or uses keyboard shortcuts

- Waits and observes — takes another screenshot to see the result of the action

- Repeats until the task is complete

## ​ Computer Use and Testing

- Setup — Devin installs dependencies, starts your app, and prepares the environment

- Test planning — Devin reads the diff and creates a focused test plan

- Execution via Computer Use — Devin uses its desktop to interact with your app, following the test plan step by step

- Recording — The entire process is captured on video with annotations, then sent to you for review

## ​ Tips for Getting the Best Results

## Be specific about what to test

- “Open the app, click the Settings button in the top-right, toggle dark mode, and verify all text remains readable”

- “Launch the Electron app, create a new document, type some text, and verify it saves when you close the window”

## Tell Devin what success looks like

- “The dashboard should show three charts with no error messages”

- “After submitting the form, a green success banner should appear at the top of the page”

### ​ Pre-configure access

### ​ Create testing skills

## ​ Scripted Browser Use via Playwright

### ​ How it works

### ​ Example: connecting to Devin’s browser

```
from playwright.sync_api import sync_playwright with sync_playwright() as p: browser = p.chromium.connect_over_cdp( "http://localhost:29229" ) context = browser.contexts[ 0 ] page = context.pages[ 0 ] if context.pages else context.new_page() # Example: navigate and log in page.goto( "https://example.com/login" ) page.fill( 'input[name="email"]' , "user@example.com" ) page.fill( 'input[name="password"]' , "password" ) page.click( 'button[type="submit"]' ) page.wait_for_url( "**/dashboard" ) print ( "Login successful!" )
```

```
from playwright.sync_api import sync_playwright with sync_playwright() as p: browser = p.chromium.connect_over_cdp( "http://localhost:29229" ) context = browser.contexts[ 0 ] page = context.pages[ 0 ] if context.pages else context.new_page() # Example: navigate and log in page.goto( "https://example.com/login" ) page.fill( 'input[name="email"]' , "user@example.com" ) page.fill( 'input[name="password"]' , "password" ) page.click( 'button[type="submit"]' ) page.wait_for_url( "**/dashboard" ) print ( "Login successful!" )
```

### ​ When to use this

## SSO / OAuth flows

## Repo setup authentication

## Skills-based automation

## Systematic data entry

### ​ Tips

- Store login scripts in your repo’s .agents/skills/ directory so they persist across sessions

```
.agents/skills/
```

- Use Secrets to store credentials — reference them via environment variables in your scripts

- The CDP endpoint is always http://localhost:29229 — this is the same port whether Desktop mode is enabled or not

```
http://localhost:29229
```

- After the script runs, Devin can use either Computer Use or browser tools to interact with the authenticated session

## ​ Troubleshooting

### ​ Devin can’t find a UI element

### ​ The app doesn’t render on Devin’s desktop

### ​ Devin is clicking the wrong things
