# Biome v1.7

Today we’re excited to announce the release of Biome v1.7!

This new version provides an easy path to migrate from ESLint and Prettier. It also introduces experimental machine-readable reports for the formatter and the linter, new linter rules, and many fixes.

Update Biome using the following commands:

## Migrate from ESLint with a single command

Section titled “Migrate from ESLint with a single command”This release introduces a new subcommand
`biome migrate eslint`

. This command will read your ESLint configuration and attempt to port their settings to Biome.

The subcommand is able to handle both the legacy and the flat configuration files. It supports the
`extends`

field of the legacy configuration and loads both shared and plugin configurations!
The subcommand also migrates `.eslintignore`

.

Given the following ESLint configuration:

And the following Biome configuration:

Run
`biome migrate eslint --write`

to migrate your ESLint configuration to Biome. The command overwrites your initial Biome configuration. For example, it disables
`recommended`

. This results in the following Biome configuration:

The subcommand needs Node.js to load and resolve all the plugins and
`extends`

configured in the ESLint configuration file. For now,
`biome migrate eslint`

doesn’t support configuration written in YAML.

We have a dedicated page that lists the equivalent Biome rule of a given ESLint rule. We handle some ESLint plugins such as TypeScript ESLint, ESLint JSX A11y, ESLint React, and ESLint Unicorn. Some rules are equivalent to their ESLint counterparts, while others are inspired. By default, Biome doesn’t migrate inspired rules. You can use the CLI flag
`--include-inspired`

to migrate them.

## Migrate from Prettier with a single command

Section titled “Migrate from Prettier with a single command”Biome v1.6 introduced the subcommand `biome migrate prettier`

.

In Biome v1.7, we add support of Prettier’s
`overrides`

and attempts to convert
`.prettierignore`

glob patterns to globs supported by Biome.

During the migration, Prettier’s `overrides`

is translated to Biome’s
`overrides`

. Given the following `.prettierrc.json`

Run
`biome migrate prettier --write`

to migrate your Prettier configuration to Biome. This results in the following Biome configuration:

The subcommand needs Node.js to load JavaScript configurations such as `.prettierrc.js`

.
`biome migrate prettier`

doesn’t support configuration written in JSON5, TOML, or YAML.

## Emit machine-readable reports

Section titled “Emit machine-readable reports”Biome is now able to output JSON reports detailing the diagnostics emitted by a command.

For instance, you can emit a report when you lint a codebase:

For now, we support two report formats: `json`

and `json-pretty`

.

Note that the report format is **experimental **, and it might change in the future. Please try this feature and let us know if any information needs to be added to the reports.

## Check `git`

staged files

Section titled “Check git staged files”Biome v1.5 added the `--changed`

to format and lint `git`

tracked files that have been changed.

Today we are introducing a new option `--staged`

which allows you to check only files added to the *Git index* (*staged
files*). This is useful for checking that the files you want to commit are formatted and linted:

This is handy for writing your own pre-commit script. Note that unstaged changes on a staged file are
**not** ignored. Thus, we still recommend using a dedicated pre-commit tool.

Thanks to @castarco for implementing this feature!

## Linter

Section titled “Linter”### New nursery rules

Section titled “New nursery rules”Since *Biome
v1.6*, we added several new rules. New rules are incubated in the nursery group. Nursery rules are exempt from semantic versioning.

The new rules are:

- nursery/noConstantMathMinMaxClamp
- nursery/noDoneCallback
- nursery/noDuplicateElseIf
- nursery/noEvolvingTypes
- nursery/noFlatMapIdentity
- nursery/noMisplacedAssertion

### Promoted rules

Section titled “Promoted rules”Once stable, a nursery rule is promoted to a stable group. The following rules are promoted:

- complexity/noExcessiveNestedTestSuites
- complexity/noUselessTernary
- correctness/useJsxKeyInIterable
- performance/noBarrelFile
- performance/noReExportAll
- style/noNamespaceImport
- style/useNodeAssertStrict
- suspicious/noDuplicateTestHooks
- suspicious/noExportsInTest
- suspicious/noFocusedTests
- suspicious/noSkippedTests
- suspicious/noSuspiciousSemicolonInJsx

## Miscellaneous

Section titled “Miscellaneous”-
By default, Biome searches a configuration file in the working directory and parent directories if it doesn’t exist. Biome provides a CLI option

`--config-path`

and an environment variable`BIOME_CONFIG_PATH`

that allows which can be used to override this behavior. Previously, they required a directory containing a Biome configuration file. For example, the following command uses the Biome configuration file in`./config/`

.This wasn’t very clear for many users who are used to specifying the configuration file path directly. They now accept a file, so the following command is valid:

-
You can now ignore

`React`

imports in the rules noUnusedImports and useImportType by setting`javascript.jsxRuntime`

to`reactClassic`

. -
Biome applies specific settings to well-known files. It now recognizes more files and distinguishes between JSON files that only allow comments and JSON files that allow both comments and trailing commas.

-
In the React ecosystem, files ending in

`.js`

are allowed to contain JSX syntax. The Biome extension is now able to parse JSX syntax in files that are associated with the JavaScript language identifier. -
useExhaustiveDependencies now supports Preact.

See the changelog for more details.

## What’s Next?

Section titled “What’s Next?”We have started work on the CSS formatter and linter. Early implementation towards a plugin system is also underway. Some of our contributors have started preliminary work for
*GraphQL* and YAML. Any help is welcome!

Follow us on our BlueSky and join our Discord community.

Copyright (c) 2023-present Biome Developers and Contributors.
