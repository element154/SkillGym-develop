# Creating Playbooks - Devin Docs

Source: https://docs.devin.ai/product-guides/creating-playbooks

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

- What are Playbooks?

- Playbooks are easily shareable, reusable prompts for repeated tasks

- Getting Started with Playbooks

- Writing a Great Playbook

- Procedure

- Advice and Pointers

- Specifications

- What’s Needed From User

- Other Tips + Tactics

- Example Playbook

- Macros

- Version History

- Enterprise Playbooks

# Creating Playbooks

Build a library of reusable prompts for your organization

## ​ What are Playbooks?

### ​ Playbooks are easily shareable, reusable prompts for repeated tasks

- You or your teammates will reuse the prompt on multiple sessions.

- You find yourself repeating the same reminders to Devin

- The use case may be relevant to others — in your organization or within the Devin user community.

## ​ Getting Started with Playbooks

- Create a document that outlines… The outcome you want Devin to achieve The steps required to get there

- The outcome you want Devin to achieve

- The steps required to get there

- Optional : Add sections like Procedure , Specifications , Advice , Forbidden Actions or Required from User Procedure : Outline the  entire scope of the task. Include at least one step for setup, the actual task, and delivery. Specifications : Describe postconditions - what should be true after Devin is done? Advice : Include tips to correct Devin’s priors Forbidden Actions : Include any action Devin should absolutely not take Required from User : Describe any input or information required from the user

- Procedure : Outline the  entire scope of the task. Include at least one step for setup, the actual task, and delivery.

- Specifications : Describe postconditions - what should be true after Devin is done?

- Advice : Include tips to correct Devin’s priors

- Forbidden Actions : Include any action Devin should absolutely not take

- Required from User : Describe any input or information required from the user

- Create the playbook directly in the web app by clicking Create a new Playbook . Alternatively, save a file with the file extension .devin.md and drag-and-drop it in the web app when starting a Devin session

```
.devin.md
```

## ​ Writing a Great Playbook

### ​ Procedure

- Have one step per line , each line written imperatively

- Cover the entire scope of the task

- Include at least one step for setup, the actual task, and delivery

- Aim to make the steps Mutually Exclusive and Collectively Exhaustive

- Additional Tips Procedures should help you define the order of Devin’s action - like if/else/loops/goto in code Don’t make tasks too specific unless you really need to, this can reduce Devin’s ability to problem-solve Each procedure step should contain an action verb - e.g. Write, Navigate to, etc.

- Procedures should help you define the order of Devin’s action - like if/else/loops/goto in code

- Don’t make tasks too specific unless you really need to, this can reduce Devin’s ability to problem-solve

- Each procedure step should contain an action verb - e.g. Write, Navigate to, etc.

### ​ Advice and Pointers

- You have a preferred way of completing the tasks

- The advice applies to the entire task, or multiple steps. Advice specific to one step should be written next to that step (e.g. as a sub-bullet)

- You are correcting Devin’s priors. Advice can function like comments on pseudocode that influence its execution.

### ​ Specifications

### ​ What’s Needed From User

### ​ Other Tips + Tactics

Iterate and improve through trial and error

- Run 2+ Devins in parallel with the same playbook to quickly identify possible errors.

- If Devin needs help, chat with it to help it along. Then add to your playbook so Devin succeeds without intervention next time.

Tell Devin what good looks like

Optimize how quickly your playbook runs

Specific commands, incantations and strings are fair game

- They can be the difference maker between a working playbook and a broken one.

- For example, the following can be a very good detail to include because alloy and tts-1 are probably not things Devin would’ve picked otherwise, and this guides Devin in a direction that is more likely to succeed!

```
3. Create request dict with model: "tts-1", voice: "alloy"
```

```
3. Create request dict with model: "tts-1", voice: "alloy"
```

## ​ Example Playbook

## ​ Macros

```
!
```

```
!data-tutorial
```

## ​ Version History

## ​ Enterprise Playbooks
