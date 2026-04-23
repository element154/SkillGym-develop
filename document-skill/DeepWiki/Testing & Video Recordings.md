# Testing & Video Recordings - Devin Docs

Source: https://docs.devin.ai/work-with-devin/testing-and-recordings

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

- How It Works

- Triggering a Test

- The Testing Workflow

- Phase 1: Setup

- Phase 2: Test planning

- Phase 3: Recording and execution

- Video Recording Details

- Skill Suggestions

- Troubleshooting

- Devin didn’t offer to test

- Recording failed

- Devin can’t access the app

# Testing & Video Recordings

How Devin tests your changes end-to-end and sends you video recordings as proof

## ​ How It Works

- Sets up the environment — installs dependencies, starts services, logs into required accounts

- Plans the test — reads the diff and codebase to create a minimal, focused test plan

- Records a video — starts a screen recording, executes the test plan in the desktop, and annotates key moments

- Sends you the result — stops the recording, processes the video, and sends it to you as a message attachment

## ​ Triggering a Test

## ​ The Testing Workflow

### ​ Phase 1: Setup

- Reads the PR and codebase to understand what needs testing

- Checks for relevant skills in the repo (under .agents/skills/ ) and follows them if found

```
.agents/skills/
```

- Logs into required services and resolves access issues

- Checks available environments (staging, dev, local) and verifies connectivity

- Requests missing secrets from you if needed — Devin will ask for credentials up front and save them for future sessions

### ​ Phase 2: Test planning

- Identifies the single most important end-to-end flow that proves the feature works

- Writes concrete, unambiguous steps (e.g., “click the button labeled Save at the top right” — not “find the save option”)

- Grounds the plan in actual code — traces through the frontend to find the exact UI path to the feature

- Only adds additional test flows if there’s a genuinely critical edge case

### ​ Phase 3: Recording and execution

- Starts recording — captures the full screen

- Annotates key moments — adds text labels at important points (e.g., “Testing login flow”, “Feature confirmed working”) that appear in the final video

- Executes the test plan — interacts with the app through the browser, following each step

- Stops recording — the video is automatically processed with annotations and speed adjustments around key moments

- Sends the video — attaches the recording to a message so you can watch it directly

## ​ Video Recording Details

- Annotations — Text labels appear at key moments in the video, marking what Devin is testing. The video slows down around annotated points so you can see the details.

- Auto-zoom — The video automatically zooms into where Devin clicks and interacts, smoothly panning to follow the cursor and easing back out during idle moments.

- Automatic processing — Raw recordings are processed to highlight important actions and compress idle time

- Sent as attachments — Videos are attached to messages in your session, viewable directly in the Devin webapp or Slack

## ​ Skill Suggestions

```
--- name : test-before-pr description : Run the local dev server and verify pages before opening any PR that touches frontend code. --- ## Setup 1. Install dependencies: `npm install` 2. Start the database: `docker-compose up -d postgres` 3. Run migrations: `npx prisma migrate dev` 4. Start the dev server: `npm run dev` 5. Wait for "Ready on http://localhost:3000" ## Verify 1. Read the git diff to identify which pages changed 2. Open each affected page in the browser 3. Check for: console errors, layout issues, broken links 4. Screenshot each page at desktop (1280px) and mobile (375px) widths ## Before Opening the PR 1. Run `npm run lint` and fix any issues 2. Run `npm test` and confirm all tests pass 3. Include screenshots in the PR description
```

```
--- name : test-before-pr description : Run the local dev server and verify pages before opening any PR that touches frontend code. --- ## Setup 1. Install dependencies: `npm install` 2. Start the database: `docker-compose up -d postgres` 3. Run migrations: `npx prisma migrate dev` 4. Start the dev server: `npm run dev` 5. Wait for "Ready on http://localhost:3000" ## Verify 1. Read the git diff to identify which pages changed 2. Open each affected page in the browser 3. Check for: console errors, layout issues, broken links 4. Screenshot each page at desktop (1280px) and mobile (375px) widths ## Before Opening the PR 1. Run `npm run lint` and fix any issues 2. Run `npm test` and confirm all tests pass 3. Include screenshots in the PR description
```

## Good instructions

- “Test the checkout flow: add an item to cart, go to checkout, fill in the form, and verify the order confirmation page shows the correct total”

- “Verify the dark mode toggle works on the settings page — text should be readable and no elements should disappear”

- “Test that the CSV export downloads a file with the correct headers”

## Vague instructions

- “Test everything”

- “Make sure the app works”

- “Check that nothing is broken”

## ​ Troubleshooting

### ​ Devin didn’t offer to test

### ​ Recording failed

### ​ Devin can’t access the app
