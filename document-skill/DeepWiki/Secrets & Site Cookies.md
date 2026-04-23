# Secrets & Site Cookies - Devin Docs

Source: https://docs.devin.ai/product-guides/secrets

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

- Giving Devin Credentials

- Persisted Global Secrets

- Personal Secrets

- Repo-Specific Secrets

- Session-Specific Secrets

- Working With Secrets

- Adding a New Site Cookie

- One-Time Password

- Tips for TOTPs

# Secrets & Site Cookies

Securely share credentials with Devin so it can access any tool

## ​ Giving Devin Credentials

- This API key should only be used in our production env but never in staging or dev.

- Used for our AWS RDS Database in us-west-2

- These credentials are scheduled to be deprecated after Q3 2025

- Auto-expires every 30 days - ping the SecOps team for rotation if this starts failing

- This API key is attached to the devin@company.com user account

## ​ Persisted Global Secrets

### ​ Personal Secrets

Raw Secret

- API Keys

- SSH Keys

- Usernames or Passwords

- Tokens

Site Cookies

```
;
```

Time-Based One-Time Password (TOTP)

Key-Value Secrets (Deprecated)

## ​ Repo-Specific Secrets

## ​ Session-Specific Secrets

## ​ Working With Secrets

- It removes invalid characters by replacing anything other than a letter, digit, or underscore with another underscore. For example, the secret named Abc%123 would become the ENV variable Abc_123

- If your secret name does not begin with a letter, Devin adds an underscore to the begining of the name. For example, the secret 123MYVAR would become the ENV variable _123MYVAR

- If you have two secrets with the same name, Devin will add a counter to the end. For example, if you have two secrets named MY_SECRET you would end up with two ENV variables named MY_SECRET and MY_SECRET_2 and so on.

## ​ Adding a New Site Cookie

- Log in as you normally would to the account you’d like to share with Devin. This will generate cookie(s).

- In order to get the cookie(s) from the browser store, download the browser extension Share your cookies and follow the steps on that Extension to extract your cookies. You may want to test that importing the cookie in another Chrome Profile successfully authenticates you to the site.

- Add the exported cookie to Devin via the Secrets page.

- When using the cookie for a site, Devin should find that it’s already logged in when it navigates to that site. Tell Devin to give it a try!

```
;
```

## ​ One-Time Password

- Access Devin’s account for the service that requires 2FA.

- Go to the account security settings and look for an option to regenerate or view the QR code. This may be called Set up or Replace Authenticator.

- If the application allows, select the option to view the QR code.

- Once the QR code is displayed on your screen, take a screenshot.

- Go to Devin’s Secrets , click on the “Add Secret” button, and change the Secret type to “One-time Password”. Put a descriptive name. Click the small QR code icon in the top right of the Value input box and upload your QR code screenshot.

### ​ Tips for TOTPs

- Some applications may not allow you to view the existing QR code once 2FA is enabled. In such cases, regenerating the QR code is the only option.

- Always save any new backup codes provided during the process in a secure location.
