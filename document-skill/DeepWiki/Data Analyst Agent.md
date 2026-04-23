# Data Analyst Agent - Devin Docs

Source: https://docs.devin.ai/work-with-devin/data-analyst

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

- When to use the Data Analyst Agent

- Accessing the Data Analyst Agent

- From the web app

- From Slack

- Prerequisites

- How it works

- Database Knowledge

- Example prompts

- Simple lookups

- Aggregations and metrics

- Joins and cross-table analysis

- Filtering and segmentation

- Time-series analysis

- Investigations and anomaly detection

- Multi-step analysis

- Supported data sources

- SQL databases

- Analytics and observability platforms

- Connecting a data source

- Best practices

- Be specific about metrics

- Specify time periods

- Request specific output formats

- Define business logic upfront

- Ask for comparisons and context

- Iterate on results

- Validate the SQL

- Output formats

- Tables

- Charts and visualizations

- Summaries and insights

- Knowledge management

- Differences from standard Devin

# Data Analyst Agent

Use the Data Analyst agent for fast database queries, data analysis, and visualizations

## ​ When to use the Data Analyst Agent

- Query databases : Write and execute SQL queries against your connected data sources

- Analyze data : Explore patterns, calculate metrics, and investigate trends in your data

- Create visualizations : Generate professional charts and graphs using seaborn

- Answer data questions : Get quick, accurate answers to questions about your data

- Generate insights : Discover patterns, anomalies, and actionable findings

## ​ Accessing the Data Analyst Agent

### ​ From the web app

- Go to the Devin home page

- Click the agent picker dropdown

- Select Data Analyst from the dropdown menu

- Start your session with a data-related question or task

### ​ From Slack

```
/dana What were our top 10 customers by revenue last month?
```

```
/dana What were our top 10 customers by revenue last month?
```

```
!dana
```

```
@Devin !dana What were our top 10 customers by revenue last month?
```

```
@Devin !dana What were our top 10 customers by revenue last month?
```

## ​ Prerequisites

- Database MCPs : Redshift, PostgreSQL, Snowflake, BigQuery, and other SQL databases

- Analytics MCPs : Datadog, Metabase, and other observability platforms

## Set up MCP integrations

## ​ How it works

### ​ Database Knowledge

## ​ Example prompts

### ​ Simple lookups

- “How many active users did we have last week?”

- “What’s our daily revenue trend for the past month?”

- “Which customers have the highest usage?”

### ​ Aggregations and metrics

- “What’s the average session duration by plan tier for the past 30 days?”

- “Show me total revenue grouped by region and product line for Q4”

- “Calculate the 95th percentile response time for each API endpoint this week”

### ​ Joins and cross-table analysis

- “Join our users table with the orders table and show the top 20 customers by lifetime value”

- “Correlate signup source with 30-day retention — which acquisition channels have the best retention rates?”

- “Combine session data with billing records to find accounts with high usage but low spend”

### ​ Filtering and segmentation

- “Show me only enterprise customers who signed up after January 2025 and have more than 100 sessions”

- “Filter error logs to 5xx errors from the payments service in the last 48 hours”

- “Break down consumption by enterprise vs. self-serve customers, excluding trial accounts”

### ​ Time-series analysis

- “Plot weekly active users over the past 6 months — highlight any weeks with more than 10% change”

- “Show me a month-over-month comparison of signup rates for 2025 vs. 2024”

- “What’s the daily trend for API calls over the past 90 days? Overlay a 7-day moving average”

### ​ Investigations and anomaly detection

- “Why did signups drop last Tuesday? Check if there were any related incidents or deployments”

- “Are there any anomalies in our error rates this week?”

- “Compare this month’s metrics to the same period last year and flag significant deviations”

### ​ Multi-step analysis

- “Analyze user retention by cohort for Q4, then identify which cohorts have the steepest drop-off and suggest possible causes”

- “Find the top 10 users by session count, show their activity over time, and flag any that look like potential churns”

## ​ Supported data sources

### ​ SQL databases

### ​ Analytics and observability platforms

### ​ Connecting a data source

- Navigate to Settings > MCP Marketplace

- Find your data source and click Enable

- Provide any required credentials (connection strings, API keys, or OAuth)

- Start a Data Analyst session — the agent will automatically discover your connected data sources

## Set up MCP integrations

## ​ Best practices

### ​ Be specific about metrics

```
"What's our 7-day active user count, defined as users who started at least one session?"
```

```
"What's our 7-day active user count, defined as users who started at least one session?"
```

### ​ Specify time periods

```
"Show me daily revenue for the past 30 days"
```

```
"Show me daily revenue for the past 30 days"
```

### ​ Request specific output formats

```
"Plot a line chart of weekly signups for the past quarter, with a table of the raw numbers below"
```

```
"Plot a line chart of weekly signups for the past quarter, with a table of the raw numbers below"
```

### ​ Define business logic upfront

```
"Show monthly churn rate, where churn is defined as accounts with zero sessions in the past 30 days that had at least one session in the prior 30 days"
```

```
"Show monthly churn rate, where churn is defined as accounts with zero sessions in the past 30 days that had at least one session in the prior 30 days"
```

### ​ Ask for comparisons and context

```
"Show this week's daily active users compared to the same week last month, and highlight any days with more than 15% deviation"
```

```
"Show this week's daily active users compared to the same week last month, and highlight any days with more than 15% deviation"
```

### ​ Iterate on results

- Start broad: “What are our top 10 customers by revenue this quarter?”

- Drill down: “For the top 3, show me their monthly revenue trend over the past year”

- Investigate: “Customer X had a revenue spike in March — what drove that?”

### ​ Validate the SQL

## ​ Output formats

### ​ Tables

```
| Customer       | Revenue   | Sessions | Avg Duration | |----------------|-----------|----------|--------------| | Acme Corp      | $125,400  | 1,247    | 34 min       | | Globex Inc     | $98,200   | 983      | 28 min       | | Initech        | $87,600   | 876      | 41 min       |
```

```
| Customer       | Revenue   | Sessions | Avg Duration | |----------------|-----------|----------|--------------| | Acme Corp      | $125,400  | 1,247    | 34 min       | | Globex Inc     | $98,200   | 983      | 28 min       | | Initech        | $87,600   | 876      | 41 min       |
```

### ​ Charts and visualizations

- Line charts — time-series trends, comparisons over time

- Bar charts — categorical comparisons, rankings

- Heatmaps — correlation matrices, activity patterns

- Scatter plots — relationship analysis between two metrics

### ​ Summaries and insights

- Analysis summary — a plain-language answer to your question

- SQL query — the exact query used, so you can verify the logic

- Key numbers — the most important metrics highlighted

- Data insights — patterns, anomalies, or notable findings

- Metabase link — if your organization has Metabase connected via MCP, the agent may include a link to an interactive dashboard for further exploration

## ​ Knowledge management

- New schema information or table relationships

- Business logic or metric definitions

- Data quality patterns or caveats

## Learn more about Knowledge

## ​ Differences from standard Devin
