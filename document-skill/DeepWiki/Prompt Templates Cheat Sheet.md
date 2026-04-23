# Prompt Templates Cheat Sheet - Devin Docs

Source: https://docs.devin.ai/essential-guidelines/prompt-templates-cheat-sheet

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

- Bug Fixes

- Fix a Specific Bug

- Investigate Production Issue

- Feature Implementation

- Add a New API Endpoint

- Add a New UI Component

- Implement a Feature from Design

- Code Refactoring

- Refactor a Module

- Convert to New Pattern

- Testing

- Add Test Coverage

- Debug Failing Tests

- Documentation

- Document a Module

- Update API Documentation

- Performance Optimization

- Optimize Database Queries

- Optimize Frontend Performance

- Security

- Fix Security Vulnerability

- Add Security Headers

- Migration & Upgrades

- Upgrade Dependency

- Migrate to New Service

- Code Review

- Review a Pull Request

- General Purpose

- Research and Implement

- Debug and Fix

# Prompt Templates Cheat Sheet

Ready-to-use prompt templates for common tasks

```
[like this]
```

## ​ Bug Fixes

### ​ Fix a Specific Bug

```
Fix the bug where `[describe the bug behavior]`. Steps to reproduce: 1. `[Step 1]` 2. `[Step 2]` 3. `[Step 3]` Expected behavior: `[what should happen]` Actual behavior: `[what actually happens]` Please: 1. Investigate the root cause in `[relevant file/directory]` 2. Implement a fix that addresses the root cause 3. Add a regression test to prevent this issue from recurring 4. Run the existing test suite to ensure no regressions
```

```
Fix the bug where `[describe the bug behavior]`. Steps to reproduce: 1. `[Step 1]` 2. `[Step 2]` 3. `[Step 3]` Expected behavior: `[what should happen]` Actual behavior: `[what actually happens]` Please: 1. Investigate the root cause in `[relevant file/directory]` 2. Implement a fix that addresses the root cause 3. Add a regression test to prevent this issue from recurring 4. Run the existing test suite to ensure no regressions
```

### ​ Investigate Production Issue

```
Users are reporting `[describe the issue]` in production. Please: 1. Use the `[Sentry/DataDog/Log monitoring tool]` MCP to pull recent error logs and stack traces 2. Identify the root cause of the issue 3. Implement a fix 4. Add appropriate error handling to prevent similar issues 5. Create a regression test 6. Link the monitoring/alert in the PR description
```

```
Users are reporting `[describe the issue]` in production. Please: 1. Use the `[Sentry/DataDog/Log monitoring tool]` MCP to pull recent error logs and stack traces 2. Identify the root cause of the issue 3. Implement a fix 4. Add appropriate error handling to prevent similar issues 5. Create a regression test 6. Link the monitoring/alert in the PR description
```

## ​ Feature Implementation

### ​ Add a New API Endpoint

```
Create a new API endpoint `[endpoint path]` that `[describe what it does]`. Requirements: - Method: `[GET/POST/PUT/DELETE]` - Request body: `[describe request structure]` - Response format: `[describe response structure]` - Authentication: `[describe auth requirements]` Please: 1. Reference the existing `[similar endpoint file]` for patterns 2. Implement the endpoint following our existing conventions 3. Add input validation and error handling 4. Write unit tests for the new endpoint 5. Update API documentation if applicable 6. Run the test suite to ensure everything passes
```

```
Create a new API endpoint `[endpoint path]` that `[describe what it does]`. Requirements: - Method: `[GET/POST/PUT/DELETE]` - Request body: `[describe request structure]` - Response format: `[describe response structure]` - Authentication: `[describe auth requirements]` Please: 1. Reference the existing `[similar endpoint file]` for patterns 2. Implement the endpoint following our existing conventions 3. Add input validation and error handling 4. Write unit tests for the new endpoint 5. Update API documentation if applicable 6. Run the test suite to ensure everything passes
```

### ​ Add a New UI Component

```
Add a new `[component type]` component to `[file/location]`. Requirements: - Component name: `[ComponentName]` - Props: `[list props and their types]` - Functionality: `[describe what it should do]` - Styling: Use `[existing component/library]` as a reference Please: 1. Create the component following our existing patterns 2. Implement the required functionality 3. Add proper TypeScript types 4. Style it to match our design system 5. Add unit tests for the component 6. Integrate it into `[parent component/page]` 7. Test it manually by running the dev server
```

```
Add a new `[component type]` component to `[file/location]`. Requirements: - Component name: `[ComponentName]` - Props: `[list props and their types]` - Functionality: `[describe what it should do]` - Styling: Use `[existing component/library]` as a reference Please: 1. Create the component following our existing patterns 2. Implement the required functionality 3. Add proper TypeScript types 4. Style it to match our design system 5. Add unit tests for the component 6. Integrate it into `[parent component/page]` 7. Test it manually by running the dev server
```

### ​ Implement a Feature from Design

```
Implement the `[feature name]` from this design file: `[Figma/link to design]` Focus on the `[specific frame/section]` frame. Requirements: - Use our existing components from `[component library path]` - Follow the styling in `[design system file]` - Ensure responsive design at `[breakpoint 1]` and `[breakpoint 2]` Please: 1. Implement the feature following the design specifications 2. Reuse existing components where possible 3. Test at desktop (1440px) and mobile (375px) widths 4. Take screenshots to verify it matches the design 5. Do not open a PR until it visually matches the design
```

```
Implement the `[feature name]` from this design file: `[Figma/link to design]` Focus on the `[specific frame/section]` frame. Requirements: - Use our existing components from `[component library path]` - Follow the styling in `[design system file]` - Ensure responsive design at `[breakpoint 1]` and `[breakpoint 2]` Please: 1. Implement the feature following the design specifications 2. Reuse existing components where possible 3. Test at desktop (1440px) and mobile (375px) widths 4. Take screenshots to verify it matches the design 5. Do not open a PR until it visually matches the design
```

## ​ Code Refactoring

### ​ Refactor a Module

```
Refactor the `[module/file name]` to improve `[specific aspect: maintainability/performance/readability]`. Current issues: - `[Issue 1]` - `[Issue 2]` - `[Issue 3]` Requirements: - Keep all existing functionality intact - Follow the patterns in `[reference file]` - Improve `[specific metric: code complexity/performance]` Please: 1. Analyze the current implementation 2. Refactor following best practices 3. Ensure all existing tests still pass 4. Add tests for any new functions introduced 5. Run the full test suite 6. Measure and report performance improvements if applicable
```

```
Refactor the `[module/file name]` to improve `[specific aspect: maintainability/performance/readability]`. Current issues: - `[Issue 1]` - `[Issue 2]` - `[Issue 3]` Requirements: - Keep all existing functionality intact - Follow the patterns in `[reference file]` - Improve `[specific metric: code complexity/performance]` Please: 1. Analyze the current implementation 2. Refactor following best practices 3. Ensure all existing tests still pass 4. Add tests for any new functions introduced 5. Run the full test suite 6. Measure and report performance improvements if applicable
```

### ​ Convert to New Pattern

```
Convert `[file/directory]` to use `[new pattern/library/framework]`. Reference: `[link to documentation or example file]` Requirements: - Maintain all existing functionality - Follow the conventions in `[example file]` - Update any dependent code Please: 1. Review the documentation and examples 2. Convert the code step by step 3. Update imports and dependencies 4. Ensure all tests pass 5. Run `[build command]` to verify no errors 6. Test the functionality manually
```

```
Convert `[file/directory]` to use `[new pattern/library/framework]`. Reference: `[link to documentation or example file]` Requirements: - Maintain all existing functionality - Follow the conventions in `[example file]` - Update any dependent code Please: 1. Review the documentation and examples 2. Convert the code step by step 3. Update imports and dependencies 4. Ensure all tests pass 5. Run `[build command]` to verify no errors 6. Test the functionality manually
```

## ​ Testing

### ​ Add Test Coverage

```
Add comprehensive test coverage for `[file/module/function]`. Current coverage: `[current coverage %]` Target coverage: `[target coverage %]` Please: 1. Analyze the existing code to identify edge cases 2. Write unit tests for all public methods 3. Add integration tests if applicable 4. Reference `[existing test file]` for testing patterns 5. Run `npm test -- --coverage` and verify coverage meets target 6. Ensure all tests pass
```

```
Add comprehensive test coverage for `[file/module/function]`. Current coverage: `[current coverage %]` Target coverage: `[target coverage %]` Please: 1. Analyze the existing code to identify edge cases 2. Write unit tests for all public methods 3. Add integration tests if applicable 4. Reference `[existing test file]` for testing patterns 5. Run `npm test -- --coverage` and verify coverage meets target 6. Ensure all tests pass
```

### ​ Debug Failing Tests

```
Fix the failing tests in `[test file or directory]`. Test failures: - `[Test name 1]`: `[error message]` - `[Test name 2]`: `[error message]` Please: 1. Investigate why these tests are failing 2. Determine if the tests or the implementation need fixing 3. Fix the root cause 4. Ensure all tests in the suite pass 5. Run the full test suite to check for regressions
```

```
Fix the failing tests in `[test file or directory]`. Test failures: - `[Test name 1]`: `[error message]` - `[Test name 2]`: `[error message]` Please: 1. Investigate why these tests are failing 2. Determine if the tests or the implementation need fixing 3. Fix the root cause 4. Ensure all tests in the suite pass 5. Run the full test suite to check for regressions
```

## ​ Documentation

### ​ Document a Module

```
Add comprehensive documentation to `[file/module]`. Please: 1. Add JSDoc/TypeDoc comments to all public functions 2. Document parameters, return values, and exceptions 3. Add usage examples for complex functions 4. Create a README if this is a new module 5. Follow our documentation style guide in `[style guide link]` 6. Update the main API documentation if applicable
```

```
Add comprehensive documentation to `[file/module]`. Please: 1. Add JSDoc/TypeDoc comments to all public functions 2. Document parameters, return values, and exceptions 3. Add usage examples for complex functions 4. Create a README if this is a new module 5. Follow our documentation style guide in `[style guide link]` 6. Update the main API documentation if applicable
```

### ​ Update API Documentation

```
Update the API documentation for `[endpoint/function]`. Changes made: - `[Change 1]` - `[Change 2]` Please: 1. Update the `[OpenAPI/Swagger]` specification 2. Update any inline code comments 3. Add usage examples if the behavior changed 4. Update the `[documentation file]` 5. Verify the documentation builds successfully
```

```
Update the API documentation for `[endpoint/function]`. Changes made: - `[Change 1]` - `[Change 2]` Please: 1. Update the `[OpenAPI/Swagger]` specification 2. Update any inline code comments 3. Add usage examples if the behavior changed 4. Update the `[documentation file]` 5. Verify the documentation builds successfully
```

## ​ Performance Optimization

### ​ Optimize Database Queries

```
Optimize the database queries in `[file/module]`. Performance issues: - `[Specific query]` is slow (takes `[time]`) - `[Specific operation]` causes N+1 queries Please: 1. Analyze the query execution plans 2. Add appropriate indexes to `[table/column]` 3. Refactor queries to use joins instead of N+1 4. Benchmark before and after performance 5. Ensure all tests still pass 6. Document the performance improvements
```

```
Optimize the database queries in `[file/module]`. Performance issues: - `[Specific query]` is slow (takes `[time]`) - `[Specific operation]` causes N+1 queries Please: 1. Analyze the query execution plans 2. Add appropriate indexes to `[table/column]` 3. Refactor queries to use joins instead of N+1 4. Benchmark before and after performance 5. Ensure all tests still pass 6. Document the performance improvements
```

### ​ Optimize Frontend Performance

```
Optimize the performance of `[component/page]`. Performance issues: - Slow initial load time - Large bundle size - Unnecessary re-renders Please: 1. Analyze the bundle size using `[bundle analyzer]` 2. Implement code splitting for `[large module]` 3. Add memoization where appropriate 4. Optimize images and assets 5. Lazy load components below the fold 6. Measure performance improvements using Lighthouse 7. Ensure functionality remains intact
```

```
Optimize the performance of `[component/page]`. Performance issues: - Slow initial load time - Large bundle size - Unnecessary re-renders Please: 1. Analyze the bundle size using `[bundle analyzer]` 2. Implement code splitting for `[large module]` 3. Add memoization where appropriate 4. Optimize images and assets 5. Lazy load components below the fold 6. Measure performance improvements using Lighthouse 7. Ensure functionality remains intact
```

## ​ Security

### ​ Fix Security Vulnerability

```
Fix the security vulnerability identified in `[file/module]`. Vulnerability type: `[e.g., SQL injection, XSS, CSRF]` Severity: `[High/Medium/Low]` Please: 1. Review the security advisory: `[link to advisory]` 2. Implement the recommended fix 3. Add input validation and sanitization 4. Add a security test to prevent regression 5. Run the security audit: `[audit command]` 6. Ensure no other similar vulnerabilities exist
```

```
Fix the security vulnerability identified in `[file/module]`. Vulnerability type: `[e.g., SQL injection, XSS, CSRF]` Severity: `[High/Medium/Low]` Please: 1. Review the security advisory: `[link to advisory]` 2. Implement the recommended fix 3. Add input validation and sanitization 4. Add a security test to prevent regression 5. Run the security audit: `[audit command]` 6. Ensure no other similar vulnerabilities exist
```

### ​ Add Security Headers

```
Add security headers to the `[application/API]`. Required headers: - `[Header 1]`: `[value]` - `[Header 2]`: `[value]` - `[Header 3]`: `[value]` Please: 1. Configure the headers in `[config file]` 2. Test that headers are set correctly using `[tool/method]` 3. Ensure existing functionality is not broken 4. Document the security improvements
```

```
Add security headers to the `[application/API]`. Required headers: - `[Header 1]`: `[value]` - `[Header 2]`: `[value]` - `[Header 3]`: `[value]` Please: 1. Configure the headers in `[config file]` 2. Test that headers are set correctly using `[tool/method]` 3. Ensure existing functionality is not broken 4. Document the security improvements
```

## ​ Migration & Upgrades

### ​ Upgrade Dependency

```
Upgrade `[package/library]` from version `[old version]` to version `[new version]`. Please: 1. Review the changelog for breaking changes: `[changelog link]` 2. Update the dependency in `[package.json/requirements.txt]` 3. Update any deprecated API usage 4. Run the migration script if applicable: `[migration command]` 5. Run all tests to ensure compatibility 6. Test the application manually 7. Update documentation if APIs changed
```

```
Upgrade `[package/library]` from version `[old version]` to version `[new version]`. Please: 1. Review the changelog for breaking changes: `[changelog link]` 2. Update the dependency in `[package.json/requirements.txt]` 3. Update any deprecated API usage 4. Run the migration script if applicable: `[migration command]` 5. Run all tests to ensure compatibility 6. Test the application manually 7. Update documentation if APIs changed
```

### ​ Migrate to New Service

```
Migrate from `[old service]` to `[new service]`. Reference documentation: `[link to new service docs]` Please: 1. Set up the new service following the documentation 2. Migrate existing data/configuration 3. Update all code to use the new service 4. Reference `[example file]` for implementation patterns 5. Run integration tests to verify functionality 6. Gradually roll out and monitor for issues 7. Decommission the old service after verification
```

```
Migrate from `[old service]` to `[new service]`. Reference documentation: `[link to new service docs]` Please: 1. Set up the new service following the documentation 2. Migrate existing data/configuration 3. Update all code to use the new service 4. Reference `[example file]` for implementation patterns 5. Run integration tests to verify functionality 6. Gradually roll out and monitor for issues 7. Decommission the old service after verification
```

## ​ Code Review

### ​ Review a Pull Request

```
Review the pull request: `[PR link or number]` Focus areas: - Code quality and maintainability - Performance implications - Security considerations - Test coverage - Documentation Please: 1. Review each file changed 2. Leave specific, actionable comments 3. Verify the changes address the PR description 4. Check for edge cases and error handling 5. Ensure tests are adequate 6. Approve or request changes with clear feedback
```

```
Review the pull request: `[PR link or number]` Focus areas: - Code quality and maintainability - Performance implications - Security considerations - Test coverage - Documentation Please: 1. Review each file changed 2. Leave specific, actionable comments 3. Verify the changes address the PR description 4. Check for edge cases and error handling 5. Ensure tests are adequate 6. Approve or request changes with clear feedback
```

## ​ General Purpose

### ​ Research and Implement

```
I need to implement `[feature/functionality]` using `[technology/library]`. Please: 1. Research the best practices for `[technology/library]` 2. Find and review documentation: `[expected doc sources]` 3. Look at open-source examples if applicable 4. Propose an approach before implementing 5. Implement the solution following best practices 6. Add tests and documentation 7. Verify it works as expected
```

```
I need to implement `[feature/functionality]` using `[technology/library]`. Please: 1. Research the best practices for `[technology/library]` 2. Find and review documentation: `[expected doc sources]` 3. Look at open-source examples if applicable 4. Propose an approach before implementing 5. Implement the solution following best practices 6. Add tests and documentation 7. Verify it works as expected
```

### ​ Debug and Fix

```
Something is wrong with `[feature/component]`. Symptoms: - `[Symptom 1]` - `[Symptom 2]` Please: 1. Investigate the issue in `[relevant files]` 2. Add logging/debugging statements as needed 3. Identify the root cause 4. Implement a fix 5. Test the fix thoroughly 6. Remove any temporary debugging code 7. Ensure no regressions
```

```
Something is wrong with `[feature/component]`. Symptoms: - `[Symptom 1]` - `[Symptom 2]` Please: 1. Investigate the issue in `[relevant files]` 2. Add logging/debugging statements as needed 3. Identify the root cause 4. Implement a fix 5. Test the fix thoroughly 6. Remove any temporary debugging code 7. Ensure no regressions
```
