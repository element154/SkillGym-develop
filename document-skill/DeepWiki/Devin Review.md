# Devin Review - Devin Docs

Source: https://docs.devin.ai/work-with-devin/devin-review

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

- Features

- Getting Started

- Supported Git Providers

- PR Workflow Actions

- Auto-Review

- When Does Auto-Review Run?

- Self-Enrollment (All Users)

- Admin Configuration

- Bug Catcher

- Bugs

- Flags

- Resolving Findings

- Review Actions

- Starting a Review

- Resolving Comments

- Code Owner Indicators

- Auto-Fix

- How to Enable It

- Permissions & Constraints

- CLI

- Installation & Usage

- Privacy & Access Control

- Commit & Comment Attribution

- AGENTS.md / Instruction Files

- Custom Review Rules

- REVIEW.md

# Devin Review

A new way to quickly review and understand complex PRs.

## ​ Features

## Smart diff organization

## Copy and move detection

## Bug catcher

## GitHub compatibility

## Codebase-aware chat

## PR workflow actions

## Code changes from chat

## ​ Getting Started

- Devin webapp — Head to app.devin.ai/review to see your open PRs organized by category (assigned to you, authored by you, review requested). When Devin makes PRs, you’ll see an orange “Review” button in the chat.

- URL shortcut — For any GitHub.com PR link, replace github.com with devinreview.com in the URL. For private PRs, sign in to Devin first or use the CLI.

```
github.com
```

```
devinreview.com
```

- GitHub Enterprise — Paste the full PR URL into the Devin Review page at app.devin.ai/review . All GitHub offerings (GitHub.com, Enterprise Server, Enterprise Cloud) have the same capabilities.

- GitLab — Paste the full merge request URL into the Devin Review page at app.devin.ai/review . GitLab is supported in read-only mode.

- CLI — Run npx devin-review {pr-url} from within a local clone. See CLI below for details.

```
npx devin-review {pr-url}
```

## ​ Supported Git Providers

## ​ PR Workflow Actions

- Merge — Merge the PR using the repository’s configured merge strategy (merge commit, squash, or rebase). The merge button reflects the PR’s current mergeability status and required checks.

- Close — Close the PR without merging. Available from the dropdown menu next to the merge button.

- Convert to draft — Convert an open PR to draft status. Available from the dropdown menu when the PR is open and not already a draft.

- Mark ready for review — Mark a draft PR as ready for review. A “Ready for review” button appears in the merge bar for draft PRs.

- Auto-merge — Enable or disable GitHub auto-merge from the merge button dropdown. When enabled, the PR will merge automatically once all required checks pass. The merge bar shows the current auto-merge status, including who enabled it.

## ​ Auto-Review

### ​ When Does Auto-Review Run?

- A PR is opened (non-draft)

- New commits are pushed to a PR

- A draft PR is marked as ready for review

- An enrolled user is added as a reviewer or assignee

### ​ Self-Enrollment (All Users)

- Go to Settings > Review

- Click “Add myself (@yourusername)” to enroll

### ​ Admin Configuration

- Repositories — Add repositories to auto-review ALL PRs on that repo. Use the dropdown to search and select from connected repositories.

- Users — View and manage all enrolled users across the organization. Add any GitHub username to the auto-review list.

- Insert link in PR description — When enabled (default), Devin adds a link to the review in the PR description.

## ​ Bug Catcher

### ​ Bugs

- Severe — High-confidence
issues that require immediate attention

- Non-severe — Lower severity issues that should still be reviewed

### ​ Flags

- Investigate — Flags that warrant further investigation. You should review the flagged code yourself and verify whether there is an actual bug or issue.

- Informational — The Bug
Catcher has either concluded correctness or is explaining how something works.
These help you understand the code changes without requiring action.

### ​ Resolving Findings

## ​ Review Actions

### ​ Starting a Review

### ​ Resolving Comments

### ​ Code Owner Indicators

## ​ Auto-Fix

### ​ How to Enable It

- From the PR review settings popover — On any Devin Review page, click the settings icon (three dots) and toggle Enable Autofix . This toggle appears for Devin-authored PRs.

- From the embedded PR review settings — In the embedded Devin Review view inside a Devin session, open the settings popover and toggle Enable Autofix .

- From global Customization settings — Go to Settings > Customization > Pull request settings > Autofix settings - bot comments , then either: Set mode to Respond to specific bots only and add devin-ai-integration[bot] to the allowlist, or Set mode to Respond to all bot comments .

- Set mode to Respond to specific bots only and add devin-ai-integration[bot] to the allowlist, or

```
devin-ai-integration[bot]
```

- Set mode to Respond to all bot comments .

### ​ Permissions & Constraints

- Only organization admins can change this setting.

- If bot comment mode is set to Respond to all bot comments , the Auto-Fix toggle appears enabled but cannot be changed from PR review settings. Use Customization settings to modify bot comment mode.

- Devin Review’s No Issues Found summary comments are always ignored. Only comments with actual findings trigger Auto-Fix.

## ​ CLI

### ​ Installation & Usage

```
cd path/to/repo npx devin-review https://github.com/owner/repo/pull/123
```

```
cd path/to/repo npx devin-review https://github.com/owner/repo/pull/123
```

- Git-based diff extraction — The CLI uses your local git access to fetch the PR branch and compute the diff. This means you need read access to the repository on your machine.

- Isolated worktree checkout — The CLI creates a git worktree in a cached directory to check out the PR branch. This keeps your working directory untouched — no stashing, no branch switching. The worktree is automatically cleaned up after the review completes.

- Diff sent to Devin servers — The computed diff and file contents are sent to Devin’s servers for analysis.

### ​ Privacy & Access Control

- Local-only access by default — When you run devin-review , it starts a localhost server on your machine that serves a secure token. Only processes on your local machine can access this token, meaning only you can view the review page while logged out.

```
devin-review
```

- Transfer to your Devin account — If you log in to a Devin account that has access to the GitHub organization, the review session is transferred to your account. This lets you access the review from other devices and share it with teammates.

```
devin-review
```

- File reading — Read file contents within the repository

- Search — Grep for patterns and glob for file names

- Bash commands — Only read-only commands like ls , cat , pwd , file , head , tail , wc , find , tree , stat , and du

```
ls
```

```
cat
```

```
pwd
```

```
file
```

```
head
```

```
tail
```

```
wc
```

```
find
```

```
tree
```

```
stat
```

```
du
```

## ​ Commit & Comment Attribution

- Bug findings, flags, and automated annotations always appear as the Devin bot .

- When a user writes a comment or review through Devin Review, it appears under the user’s GitHub identity.

- When a user asks the chat agent to make a code change, the resulting commit is made as the Devin bot .

- GitHub Suggested Changes follow standard GitHub behavior: any reviewer (including Devin) can leave a suggested edit in a review comment. When a user clicks “Apply suggestion,” the commit is authored by that user, in the same way as GitHub.

- Devin will never create commits or comments on behalf of a user without the user explicitly initiating the action.

## ​ AGENTS.md / Instruction Files

- **/REVIEW.md

```
**/REVIEW.md
```

- **/AGENTS.md

```
**/AGENTS.md
```

- **/CLAUDE.md (case-insensitive)

```
**/CLAUDE.md
```

- **/CONTRIBUTING.md (case-insensitive)

```
**/CONTRIBUTING.md
```

- .cursorrules

```
.cursorrules
```

- .windsurfrules

```
.windsurfrules
```

- .cursor/rules

```
.cursor/rules
```

- *.rules

```
*.rules
```

- *.mdc

```
*.mdc
```

- .coderabbit.yaml / .coderabbit.yml

```
.coderabbit.yaml
```

```
.coderabbit.yml
```

- greptile.json

```
greptile.json
```

```
.agents/
```

```
.devin/
```

```
.cursor/
```

```
.github/
```

```
src/.agents/REVIEW.md
```

```
src/
```

### ​ Custom Review Rules

- Go to Settings > Review

- Under Review Rules , type a file glob pattern (e.g. docs/**/*.md )

```
docs/**/*.md
```

- Click Add

```
**/REVIEW.md
```

### ​ REVIEW.md

```
REVIEW.md
```

```
REVIEW.md
```

```
**/REVIEW.md
```

```
REVIEW.md
```

- Areas of the codebase that need extra scrutiny

- Common pitfalls or anti-patterns to watch for

- Project-specific conventions that reviewers should enforce

- Files or directories that can be safely ignored during review

- Security or performance considerations unique to your project

```
REVIEW.md
```

```
# Review Guidelines ## Critical Areas - All changes to `src/auth/` must be reviewed for security implications. - Database migration files should be checked for backward compatibility. ## Conventions - API endpoints must include input validation and proper error handling. - All public functions require TypeScript return types — do not use `any` . - React components should use functional components with hooks, not class components. ## Ignore - Auto-generated files in `src/generated/` do not need review. - Lock files (package-lock.json, yarn.lock) can be skipped unless dependencies changed. ## Performance - Flag any database queries inside loops. - Watch for N+1 query patterns in API resolvers.
```

```
# Review Guidelines ## Critical Areas - All changes to `src/auth/` must be reviewed for security implications. - Database migration files should be checked for backward compatibility. ## Conventions - API endpoints must include input validation and proper error handling. - All public functions require TypeScript return types — do not use `any` . - React components should use functional components with hooks, not class components. ## Ignore - Auto-generated files in `src/generated/` do not need review. - Lock files (package-lock.json, yarn.lock) can be skipped unless dependencies changed. ## Performance - Flag any database queries inside loops. - Watch for N+1 query patterns in API resolvers.
```
