# GitHub - Devin Docs

Source: https://docs.devin.ai/integrations/gh

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

- Why integrate Devin with GitHub?

- Setting up the Integration

- Using Devin with the GitHub Integration

- For Core and Teams users

- For Enterprise users

- Managing Devin’s Permissions in GitHub

- Pull Request Templates

- Devin-specific template (recommended)

- Template search order

- Commit Signing

- Security Considerations

- IP Allowlisting

- Troubleshooting: GitHub organization connected to the wrong Devin organization

- GitHub Integration FAQs

# GitHub

Work with Devin directly in your repos

## ​ Why integrate Devin with GitHub?

## ​ Setting up the Integration

- In your Devin account at app.devin.ai , navigate to Settings > Integrations > GitHub and click Add Connection .

- If you are not already logged in to GitHub, you will be prompted to authenticate.

- Select the GitHub organization you want to connect to Devin.

- Choose whether to grant Devin access to All repositories or Select repositories to control which repositories Devin can access.

- After completing the GitHub authorization, you will be redirected to Devin settings where you can confirm the integration is active.

## ​ Using Devin with the GitHub Integration

### ​ For Core and Teams users

### ​ For Enterprise users

## ​ Managing Devin’s Permissions in GitHub

- Navigate to your GitHub organization’s Settings > GitHub Apps (e.g., https://github.com/organizations/<org_name>/settings/installations )

```
https://github.com/organizations/<org_name>/settings/installations
```

- Select Configure for the Devin.ai integration

- Under Repository access , choose to grant access to all repositories or select specific repositories

- Click Save to apply your changes

```
dependabot alerts
```

```
actions
```

```
deployments
```

```
metadata
```

```
packages
```

```
pages
```

```
repository security advisories
```

```
members
```

```
webhooks
```

```
checks
```

```
commit statuses
```

```
contents
```

```
discussions
```

```
issues
```

```
pull requests
```

```
projects
```

```
workflows
```

## ​ Pull Request Templates

### ​ Devin-specific template (recommended)

```
devin_pr_template.md
```

```
PULL_REQUEST_TEMPLATE
```

### ​ Template search order

- PULL_REQUEST_TEMPLATE/devin_pr_template.md

- docs/PULL_REQUEST_TEMPLATE/devin_pr_template.md

- .github/PULL_REQUEST_TEMPLATE/devin_pr_template.md

- pull_request_template.md

- docs/pull_request_template.md

- .github/pull_request_template.md

```
pull_request_template.md
```

```
devin_pr_template.md
```

### ​ Commit Signing

```
user.email
```

- Create (or pick) a dedicated GitHub user account that will own both the commit author identity and the credentials Devin pushes with — e.g., devin@company.com . Using one account for both makes the signing setup straightforward; using two splits the configuration described below across both.

```
devin@company.com
```

- Generate a GPG key locally with that account’s email as the UID, following GitHub’s instructions .

- Upload the public key to the GitHub account whose verified email matches the GPG UID, under GitHub Settings > SSH and GPG keys . GitHub verifies signatures against the commit author identity, not the pushing identity — the public key must live on the account that owns the email in user.email . (If that’s the same dedicated account you’re pushing as, you only need to do this once.)

```
user.email
```

- Export the private key, base64-encode it, and add it (along with the matching GIT_USER_NAME / GIT_USER_EMAIL ) as secrets in Settings > Secrets .

```
GIT_USER_NAME
```

```
GIT_USER_EMAIL
```

- In your org-wide environment config , import the key and enable signing on every session start. See the copy-paste GPG commit signing example for the full YAML.

```
user.email
```

### ​ Security Considerations

- Branch protection: We recommend enabling branch protection rules on your main branch to ensure all required checks pass before Devin can merge changes.

- Organization-level permissions: Devin uses the permissions granted at the organization level, not the permissions of the individual user running a session.

- Consistent access: All users with access to both the GitHub and Devin organizations share the same Devin integration permissions.

- Repository creation: Devin cannot create new repositories in your GitHub account.

## ​ IP Allowlisting

- 100.20.50.251

- 44.238.19.62

- 52.10.84.81

- 52.183.72.253

- 20.172.46.235

- 52.159.232.99

- 4.204.199.103

## ​ Troubleshooting: GitHub organization connected to the wrong Devin organization

- Go to github.com/settings/installations and click Configure next to Devin.ai Integration . If needed, switch to the correct GitHub organization context using the Go to settings page dropdown in the top right.

- On the installation page, scroll to the Danger zone section and click Uninstall to remove the Devin.ai Integration from the GitHub organization.

- Return to app.devin.ai and refresh the page. You can now reinstall the GitHub integration under your Devin organization.

## ​ GitHub Integration FAQs

Can I connect a personal GitHub account to my organization's Devin account?

How does the GitHub app handle user authentication?

How does Devin manage and rotate encryption keys?
