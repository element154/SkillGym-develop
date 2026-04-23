# When to Use Devin - Devin Docs

Source: https://docs.devin.ai/essential-guidelines/when-to-use-devin

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

- Best Practices

- Evaluating Tasks for Devin

- Pre-Task Checklist

- Post-Task Review

# When to Use Devin

## ​ Best Practices

- Explore your codebase with Ask Devin’s advanced code search, scope the approach, and let Devin auto-generate a high-context prompt, all before a single line of code is written.

- Carve out independent tasks and run them simultaneously. Ask Devin to delegate to managed Devins to launch many sessions at once, or the Devin API for programmatic orchestration.

- Return to draft PRs waiting for review.

- Start sessions directly from conversations about bugs, feature requests, or questions. Devin responds in-thread with updates.

- Enable Devin Review with Auto-Fix so Devin automatically responds to code review comments, fixes flagged bugs, and iterates on CI failures — without you needing to be in the loop. The result: PRs that are ready to merge by the time you look at them.

- Connect Devin to Datadog, Sentry, databases, Figma, Notion, Stripe, and hundreds of other tools via the MCP Marketplace. Devin can investigate production issues, query data, read designs, and more — all within a single session.

- Devin has a full desktop environment with a shell, IDE, and browser. It can spin up your app locally, click through the UI, take screenshots, record screen recordings, and QA its own changes before opening a PR.

- Set up daily or weekly sessions to triage Sentry errors, update dependencies, generate reports, or any other repeatable work.

## ​ Evaluating Tasks for Devin

- Can I describe clear success criteria? Tasks with test suites, CI checks, or verifiable outcomes yield the best results.

- Is there enough context? Provide relevant files, patterns, docs, or examples. The more context, the better.

- Would breaking this down help? For very large projects, split the work into focused sessions that build on each other. You can run them in parallel with managed Devins .

## ​ Pre-Task Checklist

- Good tasks have a clear start and end, plus explicit success criteria (e.g., passing tests, matching an existing pattern, CI green)

- For complex tasks, use Ask Devin to collaboratively scope the work before starting a session. Ask Devin can help you investigate the codebase and outline your approach.

- Are there examples or patterns for Devin to follow?

- Can you provide prototypes, partial code, or existing patterns from the codebase or docs?

- Are there links, filenames, or design files for Devin to reference?

- Have you connected relevant MCP integrations (databases, monitoring, design tools)?

- Tasks with test suites, lint checks, or compilation steps yield better results

- Devin can test its own work by launching your app and verifying behavior in the browser

- Enable Devin Review to catch bugs before you even look at the PR

- With Auto-Fix enabled, Devin responds to review comments and CI failures automatically

- Ideally, you just need to see that CI passes and the PR is approved

- For large tasks, consider breaking them down into sub-tasks or asking Devin to run them in parallel

- Splitting large requests into smaller, manageable chunks helps Devin stay on track

- Try to keep sessions focused (XS, S, or M as measured by Session Insights )

## ​ Post-Task Review

- Leverage Session Insights to investigate the session timeline and identify actionable feedback for future sessions

- If Devin repeatedly encounters session usage limits, the task assigned to it might be too complex

- If Devin is struggling with its dev environment, revisit the Workspace setup

- In your future sessions, provide more context or instructions to help Devin get past previous obstacles

- Consider adding or approving Knowledge so Devin remembers things it learned from previous sessions

- Use the improved prompt suggested by Session Insights as a starting point for similar future tasks
