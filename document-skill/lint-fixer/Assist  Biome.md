# Assist

Biome Assist offers a series of actions meant to improve code quality and developer experience.

Contrary to linter rules, assist actions always offer a code fix. They might sort properties or fields, simplify binary expressions, perform refactorings, and more. Assist actions are not meant to catch bugs or impose a particular coding style. There are currently **6 assist actions available**.

Assist code fixes are generally safe to apply. If an assist fix breaks your code, we would consider this a bug and appreciate bug reports.

Assist works best in editors and IDEs. However, it’s possible to enforce the use of assist actions even with the CLI. Assist actions are very close to LSP code actions in semantics, and they are divided in groups.

Biome assist is enabled by default, and some rules are in the recommended rule set. The following example shows how to enable the `useSortedKeys`

action:

## Use assist actions in your IDE

Section titled “Use assist actions in your IDE”If you have an LSP-compatible IDE, then you can configure Biome to execute particular actions on save. Each assist action has a particular code called “code action”. While the majority of names follow the same pattern, there might be few exceptions (e.g. `organizeImports`

), so refer to the documentation page of each action to learn to associated code.

First, you need to setup your editor for apply all fixes on save. The configuration changes based on your editor. The code action name is `source.fixAll.biome`

:

`source.fixAll.biome`

Then, you can add the code of each action. For example, the action `useSortedKeys`

has a code action called `source.action.useSortedKeys.biome`

. If you use VS Code, you can copy this code and place it in the `editor.codeActionsOnSave`

section, and Biome will apply it when you save a document:

`source.action.useSortedKeys.biome`

## Enforce assist actions via CLI

Section titled “Enforce assist actions via CLI”Assist actions can be enforced via CLI via `check`

command:

However, the `check`

is meant for running multiple tools at once, so if you want to check only the assist actions, you should run:

### Don’t enforce assist

Section titled “Don’t enforce assist”By default, Biome enforces assists when running the `check`

command. If you wish *to not enforce assist*, you can use the `--enforce-assist`

CLI flag to `false`

. This way, Biome won’t emit a diagnostic error if some actions haven’t been applied:

## Suppression assist actions

Section titled “Suppression assist actions”You can refer to the suppression page.

## Groups

Section titled “Groups”### Source

Section titled “Source”This group represents those actions that can be safely applied to a document upon saving. These actions are all generally safe, they typically don’t change the functionality of the program.

Copyright (c) 2023-present Biome Developers and Contributors.
