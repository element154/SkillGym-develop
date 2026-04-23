# Session Insights - Devin Docs

Source: https://docs.devin.ai/product-guides/session-insights

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

- What is Session Insights?

- How to Access Session Insights

- Step 1: Complete a Session

- Step 2: Open the Insights Modal

- Step 3: Generate or View Analysis

- Session Overview Metrics

- ACU Usage

- User Messages

- Session Size

- Category

- Analysis Tabs

- Issue Timeline

- Actionable Feedback

- Knowledge Usage

- Interpreting Common Insight Patterns

- High ACU Usage with Few User Messages

- Many User Messages with Low ACU Usage

- Misleading Knowledge Flagged

- Session Classified as Wrong Category

- Timeline Shows Repeated Issues

- Best Practices

- Review Insights After Complex Sessions

- Apply Prompt Improvements Iteratively

- Maintain Your Knowledge Base

- Address Recurring Issues via Machine Setup

- Share Insights with Your Team

- Keep Sessions Focused

- Troubleshooting

- No Insights Available

- Analysis Takes Too Long

- Investigate with Devin

# Session Insights

Analyze your Devin sessions and get actionable feedback to improve future interactions

## ​ What is Session Insights?

## ​ How to Access Session Insights

### ​ Step 1: Complete a Session

### ​ Step 2: Open the Insights Modal

### ​ Step 3: Generate or View Analysis

## ​ Session Overview Metrics

### ​ ACU Usage

### ​ User Messages

### ​ Session Size

### ​ Category

- Feature Development — building new functionality

- Bug Fixing — diagnosing and resolving bugs

- Code Review & Analysis — reviewing or analyzing existing code

- Refactoring & Optimization — improving code structure or performance

- Test Generation — creating unit tests or test suites

- Migrations & Upgrades — upgrading dependencies or migrating systems

- CI/CD & DevOps — working with pipelines, deployment, or infrastructure

- Code Quality & Security — addressing linting, security, or quality issues

- Data & Automation — data processing or automation scripts

## ​ Analysis Tabs

### ​ Issue Timeline

- A label describing the issue category

- An impact rating (high, medium, or low)

- A description explaining what went wrong

### ​ Actionable Feedback

- Added context or constraints that were missing from the original

- Clarified ambiguous instructions

- Included success criteria or specific requirements

- Frontloaded important information that Devin needed earlier

- Machine setup — environment or tooling changes (e.g., installing missing dependencies, configuring access)

- Repo config — repository-level changes (e.g., adding build scripts, updating configuration files)

### ​ Knowledge Usage

## ​ Interpreting Common Insight Patterns

### ​ High ACU Usage with Few User Messages

- Missing environment setup (dependencies, API keys, access credentials)

- Ambiguous requirements that led to trial-and-error approaches

- Complex tasks that would benefit from being broken into subtasks

### ​ Many User Messages with Low ACU Usage

- Underspecified initial prompt

- Devin misunderstood the task scope or requirements

- The task required domain-specific knowledge not available to Devin

### ​ Misleading Knowledge Flagged

- Knowledge was written for a previous version of your codebase

- Knowledge is too general and gets retrieved in irrelevant contexts

- Knowledge conflicts with other knowledge items

### ​ Session Classified as Wrong Category

- The prompt was ambiguous about the goal

- The task description focused on one aspect but the intent was different (e.g., describing a bug when you wanted a feature)

### ​ Timeline Shows Repeated Issues

- A persistent build or test failure that Devin could not resolve

- An environment issue (missing tool, wrong version, permission error)

- A fundamental misunderstanding of the approach needed

## ​ Best Practices

### ​ Review Insights After Complex Sessions

### ​ Apply Prompt Improvements Iteratively

### ​ Maintain Your Knowledge Base

### ​ Address Recurring Issues via Machine Setup

### ​ Share Insights with Your Team

### ​ Keep Sessions Focused

## ​ Troubleshooting

### ​ No Insights Available

- Analysis has not been triggered yet — click Generate Analysis in the Session Insights modal or use the generate API endpoint

- The session is still in progress

- The session was too short to generate meaningful analysis (fewer than one Devin message)

- There was an error during the analysis process — try clicking Regenerate

### ​ Analysis Takes Too Long

### ​ Investigate with Devin
