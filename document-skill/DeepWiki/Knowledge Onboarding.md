# Knowledge Onboarding - Devin Docs

Source: https://docs.devin.ai/onboard-devin/knowledge-onboarding

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

- Knowledge 101

- Knowledge Onboarding Best Practices

# Knowledge Onboarding

Knowledge is a collection of instructions and advice that Devin can reference in all sessions. Think of it as onboarding a new employee with the relevant organizational context.

## ​ Knowledge 101

- Devin will automatically generate repo knowledge based on the existing READMEs, file structure and contents of the connected repositories. Note that if you don’t give Devin access to the repo, it won’t generate any associated Knowledge.

- Knowledge is retrieved based on the Trigger you set. The more specific the trigger (e.g. which file, repo or type of task the Knowledge applies to) the better the retrieval. You can find more details here .

- Devin will tell you in a session what Knowledge it used, you can see this under “Accessed Knowledge” in the session chat.

- Devin will automatically pull and update Knowledge based on specialized files in your codebase including .rules , .mdc , .cursorrules , .windsurf , CLAUDE.md , and AGENTS.md . Note that Devin won’t automatically pull in more general file types like .md .

```
.rules
```

```
.mdc
```

```
.cursorrules
```

```
.windsurf
```

```
CLAUDE.md
```

```
AGENTS.md
```

```
.md
```

## ​ Knowledge Onboarding Best Practices

- Review any auto-generated Knowledge and verify for (a) completeness and (b) accuracy.

- If you want Devin to retrieve the Knowledge note anytime it’s working on a session, make sure to pin it to all repositories. Otherwise, you can pin it to a specific repo if the information is only relevant in that context. If Knowledge isn’t pinned, it will only be used when triggered so make sure your Trigger Description is clear.

- If you don’t have a centralized specialized documentation file in your codebase, we definitely recommend setting one up with a specialized file extension.
