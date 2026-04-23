# Instructing Devin Effectively - Devin Docs

Source: https://docs.devin.ai/essential-guidelines/instructing-devin-effectively

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

- How to Write Effective Prompts

- Why This Works Well

- Best Practices: Do’s and Don’ts

# Instructing Devin Effectively

How to achieve optimal results.

## ​ How to Write Effective Prompts

- Create a background task that launches automatically when devin.rs starts.

- The task should open a connection to all forked remote machines used in this Devin session and monitor their RAM and CPU usage.

- If usage exceeds 80% of the available resource, emit a new type of Devin event to signal this (check how we use Kafka).

- Architect this in a smart way that doesn’t block other operations. You should understand how all the containers for the Devin sub-agents interact with each other.

### ​ Why This Works Well

## Provides Helpful Context

- Detail: Specifies the Devin repo and the broader purpose (monitoring resource usage).

- Benefit: Devin knows the scope and domain clearly.

## Gives Step-by-Step Instructions

- Detail: Tasks like “create a background task” and “emit an event at 80% usage.”

- Benefit: Breaks down the work into logical parts.

## Defines Clear Success Criteria

- Detail: Defines “success” as emitting a specific event upon 80% usage.

- Benefit: Devin knows exactly what to achieve.

## References Existing Patterns and Code

- Detail: Mentions Kafka and container interactions.

- Benefit: Encourages reuse of established code or design approaches.

## ​ Best Practices: Do’s and Don’ts

Be Opinionated and Specific

- Why: Devin can get stuck without a clear path or when faced with too many interpretations.

- How: Make important decisions and judgment calls for Devin. Offer specific design choices and implementation strategies. Define clear scope, boundaries, and success criteria.

- Make important decisions and judgment calls for Devin.

- Offer specific design choices and implementation strategies.

- Define clear scope, boundaries, and success criteria.

- Example: “Optimize the getOrderDetails query in orderService.js by adding a composite index on the order_id and product_id columns in the order_items table. Refactor the query to replace the existing correlated subquery with a JOIN to the products table for fetching product details.”

- Why: Vague instructions can lead Devin to implement solutions that don’t align with your actual needs.

- How: Avoid statements that require Devin to make significant design or implementation decisions without guidance. This can lead to unexpected results.

- Avoid statements that require Devin to make significant design or implementation decisions without guidance. This can lead to unexpected results.

- Example: Don’t: “Improve our database’s performance.”

Leverage Devin's Strengths

- Why: Maximize Results: By assigning tasks that align with Devin’s capabilities, you get the best results for the least amount of effort and ACUs spent.

- Maximize Results: By assigning tasks that align with Devin’s capabilities, you get the best results for the least amount of effort and ACUs spent.

- How: Read this guide: When to use Devin Provide examples, modules, resources, and templates that Devin can follow. Share direct links to docs sites so Devin can read about details like API request bodies and features it might not know about. Share specific filenames that you want Devin to look at and learn from. Connect MCP integrations to give Devin access to Figma designs, databases, monitoring tools, and more. Example: Do: “Refactor state management in the Header component to use React’s useReducer hook for better scalability and maintainability. Ensure that all existing functionality is preserved and add unit tests to cover the new state logic.” Example: Do: “Use authTemplate.rs as a reference to maintain consistency in error handling.” Example: Do: “Check out the official Sequelize docs at https://sequelize.org/docs/v6/getting-started/ for migration steps.”

- Read this guide: When to use Devin

- Provide examples, modules, resources, and templates that Devin can follow. Share direct links to docs sites so Devin can read about details like API request bodies and features it might not know about. Share specific filenames that you want Devin to look at and learn from.

- Share direct links to docs sites so Devin can read about details like API request bodies and features it might not know about.

- Share specific filenames that you want Devin to look at and learn from.

- Connect MCP integrations to give Devin access to Figma designs, databases, monitoring tools, and more.

- Example: Do: “Refactor state management in the Header component to use React’s useReducer hook for better scalability and maintainability. Ensure that all existing functionality is preserved and add unit tests to cover the new state logic.”

- Example: Do: “Use authTemplate.rs as a reference to maintain consistency in error handling.”

- Example: Do: “Check out the official Sequelize docs at https://sequelize.org/docs/v6/getting-started/ for migration steps.”

- Why: Even though Devin can handle complex work, it performs best when you provide context and clear direction.

- How: For tasks requiring domain knowledge, provide relevant docs, examples, or references. For visual tasks, provide Figma files via the Figma MCP , reference designs, or detailed specs — Devin can build from these but won’t invent aesthetics on its own. For mobile apps, keep in mind that Devin doesn’t have access to a phone emulator, so provide clear testing criteria.

- For tasks requiring domain knowledge, provide relevant docs, examples, or references.

- For visual tasks, provide Figma files via the Figma MCP , reference designs, or detailed specs — Devin can build from these but won’t invent aesthetics on its own.

- For mobile apps, keep in mind that Devin doesn’t have access to a phone emulator, so provide clear testing criteria.

- Example: Don’t: “Make the app look better” — instead, provide specific design specs or a Figma file.

- Example: Don’t: “Improve our database’s performance” — instead, specify which queries to optimize and what metrics to target.

Use Feedback Loops

- Why: Frequent feedback (both from you and from tests/checks/linters) ensures Devin corrects mistakes effectively.

- How: Use tests (unit/integration) to confirm correctness. Maintain build validations, lint checks, and static analysis for code quality. Enable Devin Review with Auto-Fix so Devin automatically responds to review comments and CI failures — creating a closed loop where PRs iterate toward merge-ready quality without you in the loop.

- Use tests (unit/integration) to confirm correctness.

- Maintain build validations, lint checks, and static analysis for code quality.

- Enable Devin Review with Auto-Fix so Devin automatically responds to review comments and CI failures — creating a closed loop where PRs iterate toward merge-ready quality without you in the loop.

- Example: Do: “Run npm test after each iteration.”

- Example: Do: “Ensure the pipeline on CircleCI doesn’t fail.”

- Example: Do: “Pass ESLint/Prettier checks before pushing any commits.”

- Why: Without feedback, Devin won’t know if its solutions meet your standards.

- How: Avoid assigning tasks without defining how you’ll evaluate them.

- Avoid assigning tasks without defining how you’ll evaluate them.

Set Checkpoints

- Why: Breaking down complex tasks into smaller checkpoints helps Devin stay focused and reduces errors.

- How: Split tasks into verifiable sub-tasks, and start one Devin session for each sub-task. Define what success looks like for each sub-task and optionally set checkpoints within each sub-task. Ask Devin to report back after completing each checkpoint or sub-task.

- Split tasks into verifiable sub-tasks, and start one Devin session for each sub-task.

- Define what success looks like for each sub-task and optionally set checkpoints within each sub-task.

- Ask Devin to report back after completing each checkpoint or sub-task.

- Example: Do: “When working with the dataset, verify that it has at least 500 rows and contains columns X, Y, Z.”

- Example: Do: “When modifying the API, confirm the endpoint returns status 200 and includes all required fields.”

- Example: Do: “When updating UI, check that the component renders without console errors and matches the design spec.”

- Why: Without defined validation steps, Devin cannot confidently complete tasks.

- How: Avoid vague success criteria. Don’t leave verification steps implicit or undefined.

- Avoid vague success criteria.

- Don’t leave verification steps implicit or undefined.

- Example: Don’t: “Make sure it works.”

Let Devin Test Its Own Work

- Spin up the app: “Run npm run dev and verify the new page renders at /settings .”

```
npm run dev
```

```
/settings
```

- Browser testing: “Open the browser, navigate to the login page, and confirm the OAuth flow completes successfully.”

- Visual verification: “Take screenshots at desktop (1440px) and mobile (375px) widths and confirm the layout matches the design.”

- Screen recording: “Record yourself testing the checkout flow end-to-end.”

Use Playbooks and Knowledge
