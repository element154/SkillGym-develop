# Biome v2.4—Embedded Snippets, HTML Accessibility, and Better Framework Support

Biome v2.4 is the first minor release of the year! After more than ten patches from v2.3, today we bring to you a new version that contains many new features!

Once you have upgraded to Biome v2.4.0, migrate your Biome configuration to the new version by running the `migrate`

command:

## Highlights

Section titled “Highlights”Among all the features shipped in this release, here are the ones we think you’re going to like most!

- Embedded snippets in JavaScript
- Editor inline configuration
- Major improvements to HTML-ish languages
- HTML accessibility rules
- Rule profiler
- Configuration file discovery

### Embedded snippets in JavaScript

Section titled “Embedded snippets in JavaScript”One of the most significant new features in Biome 2.4 is the ability to format and lint embedded CSS and GraphQL snippets within JavaScript files. Enable this experimental feature to automatically format and lint CSS and GraphQL code within template literals.

Biome recognizes CSS snippets from styled-components, Emotion, and similar CSS-in-JS libraries:

GraphQL queries and mutations within JavaScript are now properly formatted and linted:

To enable these features, add this to your configuration:

### Editor inline configuration

Section titled “Editor inline configuration”Editors can now inject a Biome configuration to the Biome Language Server without affecting the project’s configuration.

If you have a Biome extension compatible with your LSP-ready editor, you can map `inlineConfig`

. The configuration will be merged with the project’s configuration and it will take precedence.

In the following example, the editor won’t emit any diagnostics for the rule `noConsole`

, but the CLI will still conform to the configuration of the project.

### Major improvements to HTML-ish languages

Section titled “Major improvements to HTML-ish languages”In Biome v2.3, we announced experimental full support for HTML-ish languages such as Vue, Svelte, and Astro. We’ve since focused on improving the developer experience based on community feedback. Several improvements were shipped in patch releases.

Biome 2.4 brings significantly improved parsing for Vue and Svelte, resulting in better formatting across the board. Additionally, the rules `noUnusedVariables`

, `useConst`

, `useImportType`

and `noUnusedImports`

have been substantially improved, so you will see fewer false positives.

All these improvements are visible only when the flag `html.experimentalFullSupportEnabled`

is set to `true`

. If you previously used the `overrides`

configuration workaround to disable certain rules, you can now remove it. If you encounter false positives, please report them in this issue. We now have the infrastructure to address these problems.

The CSS parser can now parse Vue SFC syntax such as `:slotted`

, `:deep`

, and `v-bind()`

, as well as `:global`

and `:local`

inside `.astro`

, `.svelte`

and `.vue`

files.

### HTML accessibility rules

Section titled “HTML accessibility rules”Biome 2.4 introduces 15 comprehensive accessibility-focused lint rules for HTML, helping you build more accessible web applications:

`noAutofocus`

`noPositiveTabindex`

`useAltText`

`useAnchorContent`

`useMediaCaption`

`useHtmlLang`

`useValidLang`

`useValidAriaRole`

`useAriaPropsForRole`

`useButtonType`

`noAccessKey`

`noDistractingElements`

`noSvgWithoutTitle`

`noRedundantAlt`

`useIframeTitle`

These rules work seamlessly with Vue, Svelte, and Astro files. Please help us to ship more a11y rules.

### Rule profiler

Section titled “Rule profiler”The commands `lint`

and `check`

now have a `--profile-rules`

flag. This flag enables the new internal profiler, which allows you to capture the execution time of lint rules, assist actions, and GritQL plugins.

The profiler tracks only the execution time of the rule, and it doesn’t track the time spent in querying Biome’s CST. The flag will print an output similar to this one:

One way to interpret the data is to check the rules/actions that have low counts, and check their execution time. For example, if the execution time feels way too high compared to what it should be, maybe it’s a good place to look for possible optimizations. Since we landed this feature, we have found some bottlenecks that we have fixed since then.

### Configuration file discovery

Section titled “Configuration file discovery”Biome 2.4 improves configuration file discovery in two major ways:

-
**Hidden configuration files**: Biome now loads`.biome.json`

and`.biome.jsonc`

files. The loading order is:`biome.json`

→`biome.jsonc`

→`.biome.json`

→`.biome.jsonc`

-
**Config home directories**: Biome now attempts to load configuration files from platform-specific config directories:`$XDG_CONFIG_HOME`

or`$HOME/.config/biome`

on Linux`/Users/$USER/Library/Application Support/biome`

on macOS`C:\Users\$USER\AppData\Roaming\biome\config`

on Windows

The priority order is: project folder (working directory) → parent folders → config home.

## Linter and Assist

Section titled “Linter and Assist”### New Assist Actions

Section titled “New Assist Actions”#### Remove Duplicate CSS Classes

Section titled “Remove Duplicate CSS Classes”Biome 2.4 introduces the `noDuplicateClasses`

assist action to detect and remove duplicate CSS classes.

**For JSX files:** Supports `class`

, `className`

attributes and utility functions like `clsx`

, `cn`

, `cva`

.

**For HTML files:** Checks `class`

attributes. This is the first assist action for HTML.

Thank you @mldangelo .

#### Sort Interface Members

Section titled “Sort Interface Members”Added a new assist action `useSortedInterfaceMembers`

that sorts TypeScript interface members for improved readability. It includes an autofix.

Before:

After:

### Enhanced Lint Rules

Section titled “Enhanced Lint Rules”`useSortedKeys`

with `groupByNesting`

Option

Section titled “useSortedKeys with groupByNesting Option”Added `groupByNesting`

option to the `useSortedKeys`

assist. When enabled, object keys are grouped by their value’s nesting depth before sorting alphabetically.

Simple values (primitives, single-line arrays, and single-line objects) are sorted first, followed by nested values (multi-line arrays and multi-line objects).

`useHookAtTopLevel`

with `ignore`

Option

Section titled “useHookAtTopLevel with ignore Option”Added `ignore`

option to the `useHookAtTopLevel`

rule. You can now specify function names that should not be treated as hooks, even if they follow the `use*`

naming convention.

`useIterableCallbackReturn`

with `checkForEach`

Option

Section titled “useIterableCallbackReturn with checkForEach Option”The rule `useIterableCallbackReturn`

now supports a `checkForEach`

option. When set to `false`

, the rule will skip checking for `forEach()`

callbacks for returning values.

#### Improved `useHookAtTopLevel`

Detection

Section titled “Improved useHookAtTopLevel Detection”Updated `useHookAtTopLevel`

to better catch invalid hook usage. The rule now generates diagnostics if:

- A hook is used at the module level (top of the file, outside any function)
- A hook is used within a function or method which is not a hook or component, unless it is a function expression (such as arrow functions commonly used in tests)

`useImportExtensions`

with Custom Mappings

Section titled “useImportExtensions with Custom Mappings”Added the `extensionMappings`

option to `useImportExtensions`

. This allows you to specify custom file extensions for different module types. For example, to ban all `.ts`

imports in favor of `.js`

imports:

`useUnifiedTypeSignatures`

Enhancements

Section titled “useUnifiedTypeSignatures Enhancements”Added 2 options from `typescript-eslint`

to `useUnifiedTypeSignatures`

:

`ignoreDifferentlyNamedParameters`

- Ignores overload signatures whose parameter names differ`ignoreDifferentJsDoc`

- Ignores overload signatures whose JSDoc comments differ

#### Ignore Options for CSS Rules

Section titled “Ignore Options for CSS Rules”Added `ignore`

option to `noUnknownProperty`

, `noUnknownFunction`

, `noUnknownPseudoClass`

, and `noUnknownPseudoElement`

. If an unknown property/function/selector name matches any of the items provided in `ignore`

, a diagnostic won’t be emitted.

#### Improved Svelte Variables Detection

Section titled “Improved Svelte Variables Detection”Improved the rule `noUnusedVariables`

in Svelte files by correctly detecting variables defined in the JavaScript blocks and used inside the templates.

### New Linter Domain: `types`

Section titled “New Linter Domain: types”Biome 2.4 introduces a new linter domain called `types`

. This domain enables all rules that require the type inference engine to function.

As opposed to the `project`

domain (which only enables rules that require the module graph), the `types`

domain specifically targets rules that need type information.

The following nursery rules have been moved to the `types`

domain:

`useArraySortCompare`

`useAwaitThenable`

`useFind`

`useRegexpExec`

`noUnnecessaryConditions`

`noMisusedPromises`

`noFloatingPromises`

This allows you to enable or disable type-based linting more granularly using the `--only`

and `--skip`

flags.

### Promoted Rules

Section titled “Promoted Rules”Biome 2.4 promotes 24 nursery rules to stable groups, making them production-ready.

#### Correctness Rules

Section titled “Correctness Rules”Promoted the following rules to the `correctness`

group:

`noUnresolvedImports`

- Reports imports that cannot be resolved`noVueReservedProps`

- Reports Vue reserved props usage`noVueReservedKeys`

- Reports Vue reserved keys usage`noVueDataObjectDeclaration`

- Reports Vue 2 data declared as an object instead of a function`noNextAsyncClientComponent`

- Reports async Next.js client components`noVueDuplicateKeys`

- Reports duplicate keys in Vue component options`noVueSetupPropsReactivityLoss`

- Reports destructuring of props in Vue 3 setup which causes reactivity loss`useQwikMethodUsage`

- Enforces correct Qwik framework method usage`useQwikValidLexicalScope`

- Enforces valid lexical scope in Qwik framework

#### Suspicious Rules

Section titled “Suspicious Rules”Promoted the following rules to the `suspicious`

group:

`noImportCycles`

- Reports circular imports`noDeprecatedImports`

- Reports imports of deprecated symbols`noReactForwardRef`

- Reports usage of`React.forwardRef`

`noUnusedExpressions`

- Reports expressions that are never used`noEmptySource`

- Reports empty source files`useDeprecatedDate`

- Enforces use of GraphQL`@deprecated`

directive with date`noDuplicateDependencies`

- Reports duplicate dependencies in package.json

#### Complexity Rules

Section titled “Complexity Rules”Promoted the following rules to the `complexity`

group:

`noUselessUndefined`

- Reports useless`undefined`

initialization and returns`useMaxParams`

- Enforces a maximum number of function parameters`noUselessCatchBinding`

- Reports useless catch binding parameters

#### Style Rules

Section titled “Style Rules”Promoted the following rules to the `style`

group:

`useConsistentArrowReturn`

- Enforces consistent return in arrow functions`noJsxLiterals`

- Reports literal strings in JSX

## Formatter

Section titled “Formatter”### Embedded Snippets Formatting

Section titled “Embedded Snippets Formatting”Biome 2.4 can now format embedded CSS and GraphQL snippets within JavaScript files. See the Embedded snippets in JavaScript section in Highlights for details and examples.

### Trailing Newline Option

Section titled “Trailing Newline Option”Added the formatter option `trailingNewline`

. When set to `false`

, the formatter will remove the trailing newline at the end of formatted files. The default value is `true`

, which preserves the current behavior.

This option is available globally and for each language-specific formatter configuration:

CLI flags are also available: `--formatter-trailing-newline`

, `--javascript-formatter-trailing-newline`

, `--json-formatter-trailing-newline`

, etc.

### Top-Level Suppression Comments

Section titled “Top-Level Suppression Comments”Added support for the top-level suppression comment `biome-ignore-all format: <explanation>`

. When placed at the beginning of the document, Biome won’t format the code.

### Formatting Applied with Code Fixes

Section titled “Formatting Applied with Code Fixes”Formatting is now applied when applying safe/unsafe fixes via `biome check`

. This ensures your code is properly formatted after applying automated fixes.

### CSS Parser Improvements

Section titled “CSS Parser Improvements”#### CSS `@function`

At-Rule Support

Section titled “CSS @function At-Rule Support”Added support for parsing and formatting the CSS `@function`

at-rule from the CSS Mixins Module Level 1 specification:

#### CSS Modules Auto-Detection

Section titled “CSS Modules Auto-Detection”Biome now automatically enables CSS modules parsing for `*.module.css`

files. If your codebase only uses `*.module.css`

files, you can remove the manual parser configuration.

#### CSS Properties Ordering Update

Section titled “CSS Properties Ordering Update”Updated the CSS properties ordering to align with `stylelint-config-recess-order`

v7.4.0, adding support for containment properties, font synthesis properties, ruby properties, color adjustment properties, view transitions properties, shapes properties, motion path properties, and more.

#### CSS Module Syntax in Vue/Svelte/Astro

Section titled “CSS Module Syntax in Vue/Svelte/Astro”Added support for parsing `:global`

and `:local`

inside `.astro`

, `.svelte`

and `.vue`

files, in the `<style>`

portion of the file. This capability is only available when `experimentalFullHtmlSupportEnabled`

is set to `true`

.

### Enhanced `--skip`

and `--only`

Flags

Section titled “Enhanced --skip and --only Flags”Added `--only`

and `--skip`

options to `biome check`

and `biome ci`

, covering both lint diagnostics and assist actions. You can now run or exclude specific:

- Lint rules
- Assist actions
- Groups of rules and actions
- Domains (including the new
`types`

domain)

Examples:

### Multiple Reporters and Reporter Output to Files

Section titled “Multiple Reporters and Reporter Output to Files”Biome 2.4 adds support for multiple reporters and the ability to save reporter output to arbitrary files.

#### Combine Multiple Reporters in CI

Section titled “Combine Multiple Reporters in CI”If you run Biome on GitHub, you can now use both the default reporter and the GitHub reporter:

#### Save Reporter Output to a File

Section titled “Save Reporter Output to a File”With the new `--reporter-file`

CLI option, it’s now possible to save the output of all reporters to a file:

You can combine these two features. For example, have the `default`

reporter written on terminal, and the `rdjson`

reporter written on file:

**The --reporter and --reporter-file flags must appear next to each other.**

### New SARIF Reporter

Section titled “New SARIF Reporter”Added a new reporter `--reporter=sarif`

, that emits diagnostics using the SARIF format. This is particularly useful for integrating Biome with security and code quality platforms.

### File Watcher Control

Section titled “File Watcher Control”Added new CLI options to the commands `lsp-proxy`

and `start`

that allow control over the Biome file watcher:

(env:`--watcher-kind`

`BIOME_WATCHER_KIND`

): Controls how the Biome file watcher behaves. Options:`recommended`

(default),`polling`

, or`none`

.(env:`--watcher-polling-interval`

`BIOME_WATCHER_POLLING_INTERVAL`

): The polling interval in milliseconds when using`polling`

mode (defaults to 2000ms).

### Enhanced Logging Options

Section titled “Enhanced Logging Options”Revamped the logging options for all Biome commands. The commands `format`

, `lint`

, `check`

, `ci`

, `search`

, `lsp-proxy`

and `start`

now accept consistent logging CLI options with environment variable aliases:

`--log-file`

(env:`BIOME_LOG_FILE`

) - Optional path/file to redirect log messages to`--log-prefix-name`

(env:`BIOME_LOG_PREFIX_NAME`

) - Allows changing the prefix applied to the file name of the logs (daemon only)`--log-path`

(env:`BIOME_LOG_PATH`

) - Allows changing the folder where logs are stored (daemon only)`--log-level`

(env:`BIOME_LOG_LEVEL`

) - The level of logging:`debug`

,`info`

,`warn`

,`error`

, or`none`

`--log-kind`

(env:`BIOME_LOG_KIND`

) - What the log should look like

### Stacktrace for Fatal Errors

Section titled “Stacktrace for Fatal Errors”It’s now possible to provide the stacktrace for a fatal error. The stacktrace is only available when the environment variable `RUST_BACKTRACE=1`

is set:

## Additional Features

Section titled “Additional Features”### GritQL JSON Support

Section titled “GritQL JSON Support”Added JSON as a target language for GritQL pattern matching. You can now write Grit plugins for JSON files, enabling:

- Searching and transforming JSON configuration files
- Enforcing patterns in
`package.json`

and other JSON configs - Writing custom lint rules for JSON using GritQL

Example patterns:

Match all key-value pairs:

Match objects with specific structure:

Supports both native Biome AST names (`JsonMember`

, `JsonObjectValue`

) and TreeSitter-compatible names (`pair`

, `object`

, `array`

) for compatibility with existing Grit patterns.

For more details, see the GritQL documentation.

### LSP and Editor Features

Section titled “LSP and Editor Features”#### LSP Progress Reporting

Section titled “LSP Progress Reporting”The Biome Language Server now reports progress while scanning files and dependencies in the project, providing better feedback during long-running operations.

### Configuration and Editor Support

Section titled “Configuration and Editor Support”#### Cursor Files Support

Section titled “Cursor Files Support”Added support for Cursor files. When Biome sees a Cursor JSON file, it will parse it with comments enabled and trailing commas enabled:

`$PROJECT/.cursor/`

`%APPDATA%\Cursor\User\`

on Windows`~/Library/Application Support/Cursor/User/`

on macOS`~/.config/Cursor/User/`

on Linux

### Other Improvements

Section titled “Other Improvements”#### Vue SFC CSS Syntax Support

Section titled “Vue SFC CSS Syntax Support”The Biome CSS parser is now able to parse Vue SFC syntax such as `:slotted`

, `:deep`

, and `v-bind()`

. These pseudo-functions and directives are only correctly parsed when the CSS is defined inside `.vue`

components.

This capability is only available when `experimentalFullHtmlSupportEnabled`

is set to `true`

.

#### e18e ESLint Plugin Support

Section titled “e18e ESLint Plugin Support”Added e18e ESLint plugin as a recognized rule source. Six Biome rules now reference their e18e equivalents: `useAtIndex`

, `useExponentiationOperator`

, `noPrototypeBuiltins`

, `useDateNow`

, `useSpread`

, and `useObjectSpread`

.

## More Improvements

Section titled “More Improvements”In addition to the features highlighted above, Biome 2.4 includes numerous bug fixes, performance improvements, and smaller enhancements across the toolchain. For a complete list of changes, refer to the changelog page.

## I like where this is going, how can I help?

Section titled “I like where this is going, how can I help?”I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome.

### Translations

Section titled “Translations”If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this dashboard, you can check the supported languages and if they are up-to-date.

### Chat with us

Section titled “Chat with us”Join our Discord server, and engage with the community. Chatting with the community and being part of the community is a form of contribution.

### Code contributions

Section titled “Code contributions”If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project for you!

There are numerous aspects to explore; I assure you that you won’t get bored. Here is a small list of the things you can start with:

- Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have a very extensive technical guide.
- Help building Biome parsers! One interesting fact about Biome parsers is that they are recoverable parsers error resilient which emit a CST instead of a classic AST.
- Implement new capabilities in our LSP (Language Server Protocol), or add new features in one of our editor extensions: VS Code, Zed and JetBrains IntelliJ.

### Financial help

Section titled “Financial help”If you believe in the future of the project, you can also help with a financial contribution, via Open Collective or GitHub Sponsors.

Additionally, the project provides an enterprise support program where you as a company can employ one of the core contributors to work a specific aspect of the Biome toolchain.

Copyright (c) 2023-present Biome Developers and Contributors.
