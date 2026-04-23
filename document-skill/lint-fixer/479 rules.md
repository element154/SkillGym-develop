# Linter

Biome’s linter statically analyzes your code to find and fix common errors and to help you write better, modern code.
It supports multiple languages and provides a total of **479 rules**.

You can quickly try the Biome linter via the CLI. The following command runs the linter on all files from the root of your project:

Or you can specify one or multiple folders, for example `./src`

and `./public`

The command accepts a list of files and directories.

For more information about all the available options, check the CLI reference.

The linter is organized into rules. A rule is meant to enforce or deny a code style, the use of something that could lead to a bug, and more. Generally, a rule shouldn’t conflict with another rule, unless told otherwise.
Biome rules have a naming convention: Rules that start with `use*`

are meant to enforce/suggest something, while rules that start with `no*`

are meant to deny something. When a rule encounters a *violation* of its concept, it emits a diagnostic.

For example, the noDebugger denies the use of `debugger`

statements in JavaScript code, and it emits a diagnostic when it finds one.

Biome linter ships with a set of recommended rules that varies based on languages, which are enabled by default when you avail of the default Biome configuration (or no-configuration) when you run the `lint`

or `check`

command:

Each lint rule ships with a default severity which you can learn more about by reading the documentation of the rule.

The rules are divided into groups. For example, the `noDebugger`

rule is part of the `suspicious`

group.

Biome supports *language-agnostic rules*. Those are rules that work across more than one language, such as `noUselessEscapeInString`

, which can report useless escape sequences in both JavaScript and CSS.

Unlike other linters, Biome doesn’t provide any rules that check for code formatting; the Biome formatter is intended to handle all formatting decisions.

Many rules provide a **code fix** that can be automatically applied.

Biome makes a difference between **safe fixes** and **unsafe fixes**, which work slightly differently: The main difference is that safe fixes can be automatically applied when saving a file, while unsafe fixes can’t. Users can override which fixes are considered safe however.

Biome linter comes with a set of recommended rules that are automatically enabled, and vary based on the language.

### Safe fixes

Section titled “Safe fixes”Safe fixes are guaranteed to not change the semantic of your code. They can be applied without explicit review.

To apply *safe fixes* from the CLI, use `--write`

:

From an LSP-compatible editor, you can apply safe fixes **on save** with the code action `source.fixAll.biome`

.
Refer to the documentation of your extension to learn how to apply it.

### Unsafe fixes

Section titled “Unsafe fixes”Unsafe fixes may change the semantic of your program. Therefore, it’s advised to manually review the changes.

To apply both *safe fixes* and *unsafe fixes* from the CLI, use `--write --unsafe`

:

From an LSP-compatible editor, it’s not possible to apply all unsafe fixes on save. It would be undesirable to change the semantics of your code on save. However, you can review the single code fix and choose to apply it.

### Rule pillars

Section titled “Rule pillars”In Biome, rules should be informative and explain to the user why a rule is triggered and tell them what they should to do fix the error.
A rule should follow these **pillars**:

- Explain to the user the error. Generally, this is the message of the diagnostic.
- Explain to the user
**why**the error is triggered. Generally, this is implemented with an additional note. - Tell the user what they should do. Generally, this is implemented using a code action. If a code action is not applicable a note should tell the user what they should do to fix the error.

If you think a rule doesn’t follow these pillars, please open an issue.

## Configure the linter

Section titled “Configure the linter”In many cases, you want to change the linter based on your personal needs, or the needs or your organisation/project. Biome allows you to customise the linter, and in this section you will learn how to do it.

### Disable a rule

Section titled “Disable a rule”You can turn off a rule with `off`

.

The following configuration disables the recommended rule `noDebugger`

:

### Disable recommended rules

Section titled “Disable recommended rules”You can disable the recommended rules with a simple configuration. This may be useful in cases when you only want to enable a few rules.

### Change rule severity

Section titled “Change rule severity”Biome lint rules are shipped with their own default severity. If you want to apply the default severity, you can use the `"on"`

configuration.

For example the `noShoutyConstants`

isn’t recommended by default, and when it’s triggered it emits a diagnostic with information severity.

If you’re happy with this default and you want to use it, the configuration will look like this:

If you aren’t happy with the default severity, Biome allows you to change it with `"error"`

, `"warn"`

and `"info"`

.

Diagnostics with the `"error"`

always cause the CLI to exit with an error code. This severity can be useful when you want to block the CI if there’s a violation that belongs to a certain rule.

`"warn"`

are similar to errors, but they don’t cause the CLI to exit with an error code, unless the `--error-on-warnings`

flag is used. A possible use for the `warn`

severity is when you want to make the CI pass while there are still diagnostics for a given rule.

The `"info"`

severity won’t affect the exit status code of the CLI, even when `--error-on-warnings`

is passed.

### Change group severity

Section titled “Change group severity”Additionally, you can control the severity of lint rules **at the group level**. This way, it’s possible to control the diagnostic severity of **all rules** that belong to a group.

For example, a project doesn’t require the use of `a11y`

rules because it’s code that runs at the backend, so accessibility isn’t a concern. The following example turns off all rules that belong to the `a11y`

group:

### Configure the code fix

Section titled “Configure the code fix”As explained above, rules might emit code fixes that are **safe** or **unsafe**. Biome allows configuring a safe fix to be treated as unsafe and vice-versa. You can also turn the code fix off entirely.

Code fixes can be configured using the `fix`

option. It can have one of three values:

`none`

: the rule won’t emit a code fix;`safe`

: the rule will emit a safe fix;`unsafe`

: the rule will emit an unsafe fix;

### Skip a rule or a group

Section titled “Skip a rule or a group”The command `biome lint`

accepts an option `--skip`

that allows disabling individual rules or groups of rules.

For example, the following command skips all the rules that belong to the `style`

group and the `suspicious/noExplicitAny`

rule:

### Run only a rule or a group

Section titled “Run only a rule or a group”The command `biome lint`

accepts an option `--only`

that allows running individual rules or groups of rules.

For example, the following command runs only the rule `style/useNamingConvention`

, the rule `style/noInferrableTypes`

and the rules that belong to `a11y`

. If the rule is disabled in the configuration, then its severity level is set to `error`

for a recommended rule or `warn`

otherwise.

### Rule options

Section titled “Rule options”A few rules have options. You can set them by shaping the value of the rule differently.

`level`

will indicate the severity of the diagnostic;`options`

will change based on the rule.

### Domains

Section titled “Domains”Domains are a Biome feature that allow for grouping rules by technology, or well, *domain*. Examples of domains are `"react"`

, `"solid"`

, and `"test"`

.

A domain:

- Has its own set of recommended rules.
- Can be automatically enabled when Biome detects certain dependencies in your
`package.json`

file. - Can define additional global variables.

Biome’s linter will automatically enable the rules that belong to a domain when it detects certain dependencies in the nearest `package.json`

. For example, if the `mocha`

dependency is detected, Biome will enable the **recommended rules** of the `test`

domain.

However, if there’s no `package.json`

or the default configuration doesn’t apply, you can enable the domain via configuration:

Additionally, you can enable **all** rules that belong to a domain using the `"all"`

value:

Like rules and groups, you can also turn the rules that belong to a domains with the `"off"`

value:

To learn more about each domain, consult the appropriate page.

## Suppress lint rules

Section titled “Suppress lint rules”You can refer to the suppression page.

## Integration with editors

Section titled “Integration with editors”The first-class integration with LSP-compatible editors allows you to configure certain aspects of how Biome should behave.

When a violation is detected by Biome, a diagnostic is sent to the editor alongside with an arbitrary number of code actions, that are meant to address the diagnostic. Those actions are:

- A possible code fix. This code fix appears only if the rule
**has**a code fix. The code fix appears regardless if it’s safe or unsafe. - Suppress the diagnostic with an inline suppression.
- Suppress the diagnostic with a top-level suppression.

Usually, by positioning your cursor in the range of the diagnostic and typing a certain shortcut (it varies per editor), a tooltip will appear with the possible code actions.

By default, these actions are always displayed by the editor, however it’s possible to opt-out from them.

### Apply actions on save

Section titled “Apply actions on save”Use the `source.fixAll.biome`

code action to instruct Biome to apply all **safe fixes** on save.

`source.fixAll.biome`

### Editor suppressions

Section titled “Editor suppressions”Use `source.suppressRule.inline.biome`

to control whether the editor should show the inline suppression code action:

`source.suppressRule.inline.biome`

Use `source.suppressRule.topLevel.biome`

to control whether the editor should show the top-level suppression code action:

`source.suppressRule.topLevel.biome`

## Migrate from other linters

Section titled “Migrate from other linters”Many of Biome lint rules are inspired from other linters.
If you want to migrate from other linters such as ESLint or `typescript-eslint`

, check the rules sources page.
If you are migrating from ESLint, there’s a dedicated migration guide.

- Use the command
`biome migrate eslint`

to port the rules defined in your`eslint`

configuration file to`biome.json`

: - Lint the project by suppressing possible new rules that are caught by Biome, using the following command:
The command will suppress all linting violation that Biome finds, using the reason
`"suppressed due to migration"`

. Now the linter shouldn’t error anymore, and it’s possible to remove the suppression comments at a later stage.

## Linter Groups

Section titled “Linter Groups”The linter divides rules under *groups*. Groups are meant to offer some sort of category which rules falls under. This information becomes useful, for users, when choosing a rule to enable/disable, or for developers when creating new lint rules.

### Accessibility

Section titled “Accessibility”Rules focused on preventing accessibility problems.

### Complexity

Section titled “Complexity”Rules that focus on inspecting complex code that could be simplified.

### Correctness

Section titled “Correctness”Rules that detect code that is guaranteed to be incorrect or useless.

### Nursery

Section titled “Nursery”New rules that are still under development.

Nursery rules require explicit opt-in via configuration on stable versions because they may still have bugs or performance problems (even if they are marked as recommended). They are enabled by default on nightly builds, but as they are unstable their diagnostic severity may be set to either error or warning, depending on whether we intend for the rule to be recommended or not when it eventually gets stabilized. Nursery rules get promoted to other groups once they become stable or may be removed.

### Performance

Section titled “Performance”Rules catching ways your code could be written to run faster, or generally be more efficient.

### Security

Section titled “Security”Rules that detect potential security flaws.

Rules enforcing a consistent and idiomatic way of writing your code. By default, these rules will only generate warnings instead of errors.

### Suspicious

Section titled “Suspicious”Rules that detect code that is likely to be incorrect or useless.

## Frequently Asked Questions (FAQ)

Section titled “Frequently Asked Questions (FAQ)”### Why does rule X have an *unsafe* fix? It seems safe to me.

Section titled “Why does rule X have an unsafe fix? It seems safe to me.”There are different reasons why the Biome team decides to mark a fix unsafe, but mostly it boils down to the following:

- The lint rule is still under heavy development, as well as the fix.
- The rule fix can change the semantics of a program, so the fix must be opted in by the user.
- The rule fix can deteriorate the DX while typing and/or saving. An example is
`noUnusedVariables`

, which adds`_`

to the name of unused variables. This can deteriorate the DX of programmers while typing and saving. You can change this behavior via configuration.

If a code fix doesn’t follow these three guidelines, it’s possible that the team forgot to make the rule fix safe. Please open an issue or send a PR!

### Why is Biome linter so slow compared to v1?

Section titled “Why is Biome linter so slow compared to v1?”Since Biome v2, we’ve extended its architecture with a tool called Scanner. The Scanner is responsible for crawling your project files and creating important information such as the module graph and the inferred types.

Such information **is needed** for some rules as `noFloatingPromises`

, `noUnresolvedImports`

or `noImportCycles`

, which can’t function otherwise. Generally, for rules that belong to the project domain

The Scanner is **opt-in**, and it’s triggered only when a rule that belongs to the project domain is enabled.

Based on our tests, we noticed roughly these numbers:

| Without Scanner | With Scanner | |
|---|---|---|
| ~2k files | ~800ms | ~2s |
| ~5k files | ~1000ms | ~8s |

It’s also worth mentioning that **we’re aware** of this impact on performance, and the team is pledged to improve the performance in this part of the software.

See the Investigate slowness guide for advice on investigating and mitigating slow-downs.

If you notice some abnormal numbers in terms of memory or time, please file an issue with a link to the repository, so we can help.

### Why is Biome using so much memory?

Section titled “Why is Biome using so much memory?”If you use an editor extension that uses Biome, you might notice that one of its processes could use a lot of memory.

This usually happens if you enable one of the rules that belong to the project domain.

Since Biome v2, the toolchain is now able to use TypeScript to infer types and provide more powerful rules. To achieve this, Biome
scans `.d.ts`

files inside the `node_modules`

folder, including those of transitive dependencies.

While this might seem a silly mistake, this is intentional due to how the language works. Libraries
**can export types from its dependencies**, which end-users might not depend on from.

For example, you might depend on from a library `@org/foo`

that exports the type `Validator`

,
however this `Validator`

comes from the library `@other-org/validator`

, which is a *dependency of @org/foo*. However,
the library

`@other-org/validator`

isn’t a direct dependency of the project.The **team is aware** of the constraint and will work towards optimizing the infrastructure with time and resources.

Copyright (c) 2023-present Biome Developers and Contributors.
