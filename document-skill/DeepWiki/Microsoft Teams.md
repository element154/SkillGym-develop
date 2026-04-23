# Microsoft Teams - Devin Docs

Source: https://docs.devin.ai/integrations/microsoft-teams

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

- Get started

- Installation

- How to use Devin from Microsoft Teams

- Inline Teams Keywords & Functions

- Pricing

- Privacy

- Authentication Flow

- Permissions Details

- Tenant-wide Microsoft Graph (Application) Permissions

- Teams Bot Resource-Specific Consent (RSC) Permissions

- Example: Certificate-Based Authentication for Teams Discovery

- Complete Message Processing Flow (Teams → Cognition)

- Consent & Installation Flow

- Least-Privilege Notes

- Revocation & Uninstallation

# Microsoft Teams

Chat and collaborate with Devin directly in Microsoft Teams

## ​ Get started

### ​ Installation

- Go to Settings > Integrations and select Microsoft Teams

- Click “Connect”

- You’ll be prompted to install the Devin app for Microsoft Teams in your tenant and/or target Team

- Make sure to link your individual user. All users in your organization will need to complete this step to use Devin

- Mention @Devin in a Team channel or chat to start a session

```
@Devin
```

### ​ How to use Devin from Microsoft Teams

```
@Devin
```

### ​ Inline Teams Keywords & Functions

```
!ask
```

```
!deep
```

```
mute
```

```
unmute
```

```
(aside)
```

```
!aside
```

```
sleep
```

```
archive
```

```
EXIT
```

```
help
```

### ​ Pricing

### ​ Privacy

### ​ Authentication Flow

### ​ Permissions Details

- Graph (Application, tenant-wide): discovery & installation orchestration.

- Teams bot RSC (per Team/Chat): scoped access to messages/members/settings only where the bot is installed or present.

#### ​ Tenant-wide Microsoft Graph (Application) Permissions

```
Organization.Read.All
```

```
User.ReadBasic.All
```

```
AppCatalog.Read.All
```

```
teamsAppId
```

```
TeamsAppInstallation.ReadWriteAndConsentSelfForTeam.All
```

#### ​ Teams Bot Resource-Specific Consent (RSC) Permissions

```
ChannelMessage.Read.Group
```

```
ChannelMessage.Send.Group
```

```
Member.Read.Group
```

```
TeamSettings.Read.Group
```

```
ChatMember.Read.Chat
```

```
ChatMessage.Read.Chat
```

```
ChatMessage.Send.Chat
```

```
ChatSettings.Read.Chat
```

#### ​ Example: Certificate-Based Authentication for Teams Discovery

#### ​ Complete Message Processing Flow (Teams → Cognition)

#### ​ Consent & Installation Flow

- Admin Consent (tenant-wide) An Entra ID admin grants the Graph Application permissions listed above.

- An Entra ID admin grants the Graph Application permissions listed above.

- App Discovery The integration queries the Teams app catalog to locate our app and retrieve teamsAppId .

- The integration queries the Teams app catalog to locate our app and retrieve teamsAppId .

```
teamsAppId
```

- Targeted Installation From our dashboard, we install the bot into a specific Team. During installation, the RSC scopes are granted only to that Team (or to the specific Chat when invoked in a chat).

- From our dashboard, we install the bot into a specific Team.

- During installation, the RSC scopes are granted only to that Team (or to the specific Chat when invoked in a chat).

- Operation Discovery (org/teams/channels/app catalog) uses Graph Application permissions. Reading/sending messages and reading members/settings rely on RSC within installed surfaces.

- Discovery (org/teams/channels/app catalog) uses Graph Application permissions.

- Reading/sending messages and reading members/settings rely on RSC within installed surfaces.

#### ​ Least-Privilege Notes

- Basic readers only: User.ReadBasic.All (no tenant-wide message reading).

```
User.ReadBasic.All
```

- Message content is accessed exclusively via RSC and only where the bot is installed/present.

- No mailbox, files, or calendar permissions are requested.

#### ​ Revocation & Uninstallation

- Revoke Admin Consent: A tenant admin can remove the app’s enterprise app permissions in Entra ID.

- Uninstall from Teams: Remove the app from a Team/Chat to revoke RSC for that resource.

- Data Handling: On uninstall, our integration stops processing events for that Team/Chat and cleans up related subscriptions/links.
