# MCP (Model Context Protocol) Marketplace - Devin Docs

Source: https://docs.devin.ai/work-with-devin/mcp

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

- Why use MCP?

- Get started with MCPs

- Configuration tips

- Setting up a custom MCP server

- Step-by-step: Adding a custom MCP server

- Configuration format

- STDIO transport

- SSE and HTTP transports

- Common patterns

- Connecting to an internal API

- Connecting to a database

- Connecting to a custom tool or script

- Using environment variables for secrets

- Troubleshooting custom MCP servers

- ”Test listing tools” fails

- Server connects but tools aren’t available

- OAuth authentication issues

- General debugging tips

- Marketplace MCPs

- Vercel, Atlassian, Notion, Sentry, Neon, Asana, Jam and many more

- Datadog

- Slack

- Supabase

- Figma

- Stripe

- Zapier

- Airtable

- Docker Hub

- SonarQube

- Netlify

- Pulumi

- Parallel

- Heroku

- CircleCI

- Cortex

- Square

- Hubspot

- Redis

- Google Maps

- Playwright

- Firecrawl

- ElasticSearch

- Postgres

- Plaid

- Replicate

- Grafana

- Pinecone

- Snyk

# MCP (Model Context Protocol) Marketplace

## ​ Why use MCP?

- dig through Sentry, Datadog and Vercel logs

- use Devin as a data analyst in Slack with database MCPs

- dig into SonarQube, CircleCI, and Jam issues

- bulk create Linear tickets, Notion docs, Google Docs (through Zapier) and more

- pull in context from and interact with Airtable, Stripe, and Hubspot

- a lot more!

## ​ Get started with MCPs

## Use Devin for data analysis in Slack by connecting Devin to database MCPs

## Browse MCP use cases

## ​ Configuration tips

## ​ Setting up a custom MCP server

```
npx
```

```
uvx
```

### ​ Step-by-step: Adding a custom MCP server

- Navigate to Settings > MCP Marketplace .

- Click Add Your Own at the top of the page.

- Fill in the server details: Server Name : A descriptive name for the server (e.g., “Internal API Gateway”). Icon (optional): An emoji or URL to use as the server’s icon. Short Description : A brief summary of what the server does.

- Server Name : A descriptive name for the server (e.g., “Internal API Gateway”).

- Icon (optional): An emoji or URL to use as the server’s icon.

- Short Description : A brief summary of what the server does.

- Select the transport type (STDIO, SSE, or HTTP).

- Fill in the transport-specific configuration fields (see Configuration format below).

- Click Save to create the server.

- Click Test listing tools to verify the connection. Devin will spin up an isolated test environment, connect to your server, and attempt to discover its available tools.

### ​ Configuration format

#### ​ STDIO transport

- Command (required): The executable to run (e.g., npx , uvx , docker ).

```
npx
```

```
uvx
```

```
docker
```

- Arguments : Command-line arguments passed to the server.

- Environment Variables : Key-value pairs set in the server’s process environment. Use these to pass API keys, tokens, or configuration values.

```
npx
```

```
{ "transport" : "STDIO" , "command" : "npx" , "args" : [ "-y" , "@example/my-mcp-server" ], "env_variables" : { "API_KEY" : "your-api-key" , "API_BASE_URL" : "https://internal-api.example.com" } }
```

```
{ "transport" : "STDIO" , "command" : "npx" , "args" : [ "-y" , "@example/my-mcp-server" ], "env_variables" : { "API_KEY" : "your-api-key" , "API_BASE_URL" : "https://internal-api.example.com" } }
```

```
{ "transport" : "STDIO" , "command" : "docker" , "args" : [ "run" , "-i" , "--rm" , "-e" , "DB_CONNECTION_STRING" , "my-org/my-mcp-server:latest" ], "env_variables" : { "DB_CONNECTION_STRING" : "postgresql://user:pass@host:5432/mydb" } }
```

```
{ "transport" : "STDIO" , "command" : "docker" , "args" : [ "run" , "-i" , "--rm" , "-e" , "DB_CONNECTION_STRING" , "my-org/my-mcp-server:latest" ], "env_variables" : { "DB_CONNECTION_STRING" : "postgresql://user:pass@host:5432/mydb" } }
```

#### ​ SSE and HTTP transports

- Server URL (required): The endpoint URL of the MCP server.

- Authentication method : Choose between None , Auth Header , or OAuth . For Auth Header : Provide the header key (defaults to Authorization ) and the header value (e.g., Bearer your-token ). For OAuth : Devin will prompt you to complete an OAuth flow during your first session.

```
None
```

```
Auth Header
```

```
OAuth
```

- For Auth Header : Provide the header key (defaults to Authorization ) and the header value (e.g., Bearer your-token ).

```
Authorization
```

```
Bearer your-token
```

- For OAuth : Devin will prompt you to complete an OAuth flow during your first session.

```
{ "transport" : "HTTP" , "url" : "https://mcp.internal-service.example.com/mcp" , "auth_method" : "auth_header" , "headers" : { "Authorization" : "Bearer your-api-token" } }
```

```
{ "transport" : "HTTP" , "url" : "https://mcp.internal-service.example.com/mcp" , "auth_method" : "auth_header" , "headers" : { "Authorization" : "Bearer your-api-token" } }
```

```
{ "transport" : "SSE" , "url" : "https://mcp.example.com/sse" }
```

```
{ "transport" : "SSE" , "url" : "https://mcp.example.com/sse" }
```

## ​ Common patterns

### ​ Connecting to an internal API

```
{ "transport" : "STDIO" , "command" : "npx" , "args" : [ "-y" , "@example/api-mcp-bridge" ], "env_variables" : { "API_BASE_URL" : "https://api.internal.example.com" , "API_TOKEN" : "your-internal-api-token" } }
```

```
{ "transport" : "STDIO" , "command" : "npx" , "args" : [ "-y" , "@example/api-mcp-bridge" ], "env_variables" : { "API_BASE_URL" : "https://api.internal.example.com" , "API_TOKEN" : "your-internal-api-token" } }
```

```
{ "transport" : "HTTP" , "url" : "https://api.internal.example.com/mcp" , "headers" : { "Authorization" : "Bearer your-internal-api-token" } }
```

```
{ "transport" : "HTTP" , "url" : "https://api.internal.example.com/mcp" , "headers" : { "Authorization" : "Bearer your-internal-api-token" } }
```

### ​ Connecting to a database

```
{ "transport" : "STDIO" , "command" : "npx" , "args" : [ "-y" , "@modelcontextprotocol/server-postgres" , "postgresql://user:password@host:5432/database" ] }
```

```
{ "transport" : "STDIO" , "command" : "npx" , "args" : [ "-y" , "@modelcontextprotocol/server-postgres" , "postgresql://user:password@host:5432/database" ] }
```

### ​ Connecting to a custom tool or script

```
uvx
```

```
{ "transport" : "STDIO" , "command" : "uvx" , "args" : [ "my-custom-mcp-server" ], "env_variables" : { "CONFIG_PATH" : "/path/to/config.json" } }
```

```
{ "transport" : "STDIO" , "command" : "uvx" , "args" : [ "my-custom-mcp-server" ], "env_variables" : { "CONFIG_PATH" : "/path/to/config.json" } }
```

```
{ "transport" : "STDIO" , "command" : "docker" , "args" : [ "run" , "-i" , "--rm" , "my-org/custom-mcp-server:latest" ] }
```

```
{ "transport" : "STDIO" , "command" : "docker" , "args" : [ "run" , "-i" , "--rm" , "my-org/custom-mcp-server:latest" ] }
```

### ​ Using environment variables for secrets

## ​ Troubleshooting custom MCP servers

### ​ ”Test listing tools” fails

### ​ Server connects but tools aren’t available

- Verify the server correctly implements the MCP protocol’s tools/list method.

```
tools/list
```

- For STDIO servers, ensure the process writes valid JSON-RPC messages to stdout and reads from stdin — logging or debug output to stdout will break the protocol.

- Check that environment variables are set correctly. Missing values (e.g., a blank API key) can cause the server to start but fail to register tools.

### ​ OAuth authentication issues

- When prompted to authenticate, complete the OAuth flow in the browser window that opens. Devin will wait for the callback.

- If authentication fails, check that the OAuth redirect URI is configured correctly on the provider side.

- Only organization admins can authenticate OAuth-based MCP servers. If you see a permissions error, contact your org admin.

### ​ General debugging tips

- Check the server locally first. Before adding a custom server to Devin, verify it works by running the command or hitting the URL from your own machine.

- Review Devin’s session logs. If a server fails during a session, Devin will log the error. Look for MCP-related messages in the session output.

- Simplify and iterate. Start with the minimal configuration (e.g., no auth, default settings) and add complexity once the basic connection works.

- Verify environment variables. A common issue is missing or misnamed env variables. Double-check that every required variable is set in the configuration.

## ​ Marketplace MCPs

### ​ Vercel, Atlassian, Notion, Sentry, Neon, Asana, Jam and many more

- AlloyDB

- Asana

- Atlassian

- BigQuery

- Cloud SQL (MySQL)

- Cloud SQL (PostgreSQL)

- Cloud SQL (SQL Server)

- Cloudflare

- Cortex

- Dataplex

- Fireflies

- Firestore

- Jam

- Linear

- Looker

- Metabase

- MySQL

- Neon

- Notion

- PostgreSQL

- Prisma

- Sentry

- Spanner

- SQL Server

- Vercel

- More below!

### ​ Datadog

- DD-API-KEY - Datadog API key, which can be found on the Organization Settings > API Keys page in Datadog

- DD-APPLICATION-KEY - Datadog Application key, which can be found on the Organization Settings > Application Keys page in Datadog

### ​ Slack

- In the sidebar, navigate to Oauth & Permissions

- Look for the Bot User OAuth Token (should start with “xoxb-”).

- If you don’t see your Bot User Oauth Token, make sure you’ve configured app-level tokens (in Settings > Basic Information), added at least 1 scope (in Settings > Oauth & Permissions), and installed your app to your workspace.

- Use the curl command: curl -H "Authorization: Bearer xoxb-your-token" https://slack.com/api/auth.test where xoxb-your-token should be replaced with your OAuth token

```
curl -H "Authorization: Bearer xoxb-your-token" https://slack.com/api/auth.test
```

```
xoxb-your-token
```

- Use the curl command: curl -H "Authorization: Bearer xoxb-your-token" https://slack.com/api/conversations.list where xoxb-your-token is replaced with your OAuth token

```
curl -H "Authorization: Bearer xoxb-your-token" https://slack.com/api/conversations.list
```

```
xoxb-your-token
```

- For this command to work, you’ll need to add at least the following scopes: channels:read,groups:read,mpim:read,im:read

### ​ Supabase

### ​ Figma

- From the home page in Figma, click the profile icon in the top left corner and select Settings from the dropdown.

- In the settings menu, select the Security tab.

- Scroll down to the Personal access tokens section and click Generate new token.

- Enter a name for the token and make sure you provide the appropriate permissions. We recommend at least read permissions on File content and Dev resources.

- Click Generate token.

### ​ Stripe

```
Bearer <TOKEN>
```

```
<TOKEN>
```

### ​ Zapier

```
Bearer <TOKEN>
```

```
Bearer *****
```

### ​ Airtable

### ​ Docker Hub

- Docker Hub username: This can be obtained from My Hub

- Personal Access Token: Go to Account settings > Personal access tokens and create a token

### ​ SonarQube

- Sonarqube token: Go to my Account > Security and generate your API token

- Sonarqube org: This is your username, example shown in the below image

- Sonarqube URL: For self hosted: format is http://localhost:9000 OR https://sonarqube.mycompany.com For SonarCloud: use https://sonarcloud.io

- For self hosted: format is http://localhost:9000 OR https://sonarqube.mycompany.com

- For SonarCloud: use https://sonarcloud.io

### ​ Netlify

### ​ Pulumi

### ​ Parallel

### ​ Heroku

### ​ CircleCI

- CIRCLECI_TOKEN - CircleCI API Token, which can be created at https://app.circleci.com/settings/user/tokens . Make sure to copy the API token as soon as it is created. You won’t be able to see it again!

```
CIRCLECI_TOKEN
```

- CIRCLECI_BASE_URL [Optional] - This is optional and is required for on-prem customers only. The default value is "https://circleci.com"

```
CIRCLECI_BASE_URL
```

```
"https://circleci.com"
```

### ​ Cortex

- Log in to your Cortex instance.

- From the left-hand menu, go to Settings → My access tokens .

- Click Create new token .

- Enter a name for the token and description.

- Click Create token and copy the token.

```
https://api.getcortexapp.com
```

### ​ Square

```
Bearer <TOKEN>
```

```
<TOKEN>
```

### ​ Hubspot

- Create a private app in HubSpot:

- Go to Settings > Integrations > Private Apps

- Click “Create private app”

- Name your app and set required scopes

- Click “Create app”

- Copy the generated access token from the “Auth” tab

### ​ Redis

- Redis host

- Redis port

- Redis username

- Redis password

### ​ Google Maps

### ​ Playwright

### ​ Firecrawl

```
FIRECRAWL_API_KEY
```

### ​ ElasticSearch

- ES_URL - ElasticSearch URL or endpoint, which can be found on the /overview page in Elasticsearch.

```
ES_URL
```

- ES_API_KEY - ElasticSearch API key, which can be created on the /indices/index_details/<name>/data page in Elasticsearch.

```
ES_API_KEY
```

```
/indices/index_details/<name>/data
```

```
ES_SSL_SKIP_VERIFY
```

```
true
```

### ​ Postgres

### ​ Plaid

```
curl - X POST https : //production.plaid.com/oauth/token \ - H 'Content-Type: application/json' \ - d ' { "client_id" : "YOUR_PLAID_CLIENT_ID" , "client_secret" : "YOUR_PRODUCTION_SECRET" , "grant_type" : "client_credentials" , "scope" : "mcp:dashboard" } '
```

```
curl - X POST https : //production.plaid.com/oauth/token \ - H 'Content-Type: application/json' \ - d ' { "client_id" : "YOUR_PLAID_CLIENT_ID" , "client_secret" : "YOUR_PRODUCTION_SECRET" , "grant_type" : "client_credentials" , "scope" : "mcp:dashboard" } '
```

### ​ Replicate

### ​ Grafana

- Grafana URL

- Grafana service account token: To obtain the token, in the sidebar, go to Administration > Users and access > Service accounts > Add service account (if you don’t already have one added) > Add service account token

### ​ Pinecone

### ​ Snyk

- First, configure the MCP server. Documentation is available here . Note: Make sure to add a env variable at the bottom (not listed in documentation guide).

- Install the Snyk CLI on Devin’s machine. Documentation is available here

```
brew tap snyk / tap brew install snyk - cli snyk -- disable - trust
```

```
brew tap snyk / tap brew install snyk - cli snyk -- disable - trust
```
