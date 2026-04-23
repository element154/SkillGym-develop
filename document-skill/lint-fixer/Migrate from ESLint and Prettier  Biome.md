# Migrate from ESLint and Prettier

Biome provides dedicated commands to ease the migration from ESLint and Prettier.

If you don’t want to know the details, just run the following commands:

## Migrate from ESLint

Section titled “Migrate from ESLint”Many Biome linter rules are inspired by or identical to the ESLint rules or the rules of an ESLint plugin.
We handle some ESLint plugins such as TypeScript ESLint, ESLint JSX A11y, ESLint React, and ESLint Unicorn.
However, Biome has its own naming convention for its rules.
Biome uses `camelCaseRuleName`

while ESLint uses `kebab-case-rule-name`

.
Moreover, Biome has often chosen to use different names to better convey the intent of its rules.
The source of a rule can be found on the page describing the rule.
You can also find the equivalent Biome rule from an ESLint rule using the dedicated page.

To ease the migration, Biome provides the `biome migrate eslint`

subcommand.
This subcommand will read your ESLint configuration and attempt to port its settings to Biome.
The subcommand is able to handle both the legacy and the flat configuration files.
It supports the `extends`

field of the legacy configuration and loads both shared and plugin configurations.
For flat configuration files, the subcommand will attempt to search for JavaScript extension only (`js`

, `cjs`

, `mjs`

) to be loaded into Node.js.
The subcommand needs Node.js to load and resolve all the plugins and `extends`

configured in the ESLint configuration file.
The subcommand also migrates `.eslintignore`

.

Given the following ESLint configuration:

And the following Biome configuration:

Run the following command to migrate your ESLint configuration to Biome.

The subcommand overwrites your initial Biome configuration.
For example, it disables `recommended`

.
This results in the following Biome configuration:

For now, `biome migrate eslint`

doesn’t support configuration written in YAML.

By default, Biome doesn’t migrate inspired rules.
You can use the CLI flag `--include-inspired`

to migrate them.

Note that you are unlikely to get exactly the same behavior as ESLint because Biome has chosen not to implement some rule options or to deviate slightly from the original implementation.

Since ESLint takes VCS ignore files into account, we recommend that you enable Biome’s VCS integration.

## Migrate from Prettier

Section titled “Migrate from Prettier”Biome tries to match the Prettier formatter as closely as possible.
However, Biome uses different defaults for its formatter.
For example, it uses tabs for indentation instead of spaces.
You can easily migrate to Biome by running `biome migrate prettier --write`

.

Given the following Prettier configuration:

Run the following command to migrate your Prettier configuration to Biome.

This results in the following Biome configuration:

The subcommand needs Node.js to load JavaScript configurations such as `.prettierrc.js`

.
`biome migrate prettier`

doesn’t support configuration written in JSON5, TOML, or YAML.

Since Prettier takes VCS ignore files into account, we recommend that you enable Biome’s VCS integration.

Copyright (c) 2023-present Biome Developers and Contributors.
