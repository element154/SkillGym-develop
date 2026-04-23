# Configuration

`$schema`

Section titled “$schema”Allows to pass a path to a JSON schema file.

We publish a JSON schema file for our `biome.json`

/`biome.jsonc`

files.

You can specify a relative path to the schema inside the `@biomejs/biome`

NPM
package if it is installed in the `node_modules`

folder:

If you have problems with resolving the physical file, you can use the one published on this site:

`extends`

Section titled “extends”A list of paths to other Biome configuration files. Biome resolves and applies
the configuration settings from the files contained in the `extends`

list, and
eventually applies the options contained in this `biome.json`

/`biome.jsonc`

file.

The order of paths to extend goes from least relevant to most relevant.

Since v2, this option accepts a string that must match the value `"//"`

, which can be used
when setting up monorepos

Whether this configuration should be treated as a root. By default, any configuration file is considered a root by default.
When a configuration file is a “nested configuration”, it must set `"root": false`

, otherwise an error is thrown.

This is required so Biome can orchestrate multiple files in CLI and editors at the same time.

Default:

`true`

`files.includes`

Section titled “files.includes”A list of glob patterns of files to process.

If a folder matches a glob pattern, all files inside that folder will be processed.

The following example matches all files with a `.js`

extension inside the `src`

folder:

`*`

is used to match *all files in a folder*, while `**`

*recursively* matches
all files and subfolders in a folder. For more information on globs, see the
glob syntax reference

`includes`

also supports negated patterns, or exceptions. These are patterns
that start with `!`

and they can be used to instruct Biome to process all files
*except* those matching the negated pattern. When using a negated pattern, you
should always specify `**`

first to match all files and folders, otherwise
the negated pattern will not match any files.

Note that exceptions are processed in order, allowing you to specify exceptions to exceptions.

Consider the following example:

This example specifies that:

- All files inside all (sub)folders are processed, thanks to the
`**`

pattern… - …
*except*when those files have a`.test.js`

extension… - … but the file
`special.test.js`

*is*still processed… - …
*except*when it occurs in the folder named`test`

, because*no*files inside that folder are processed.

This means that:

`src/app.js`

**is**processed.`src/app.test.js`

**is not**processed.`src/special.test.js`

**is**processed.`test/special.test.js`

**is not**processed.

Note that files inside `node_modules/`

are ignored regardless of the
`files.includes`

setting.

#### Interaction with the scanner

Section titled “Interaction with the scanner”Biome has a scanner that is responsible for
discovering nested configuration files as well as `.gitignore`

files. It can
also index source files if one or more rules from the
project domain are enabled.

The scanner respects both `files.includes`

and the ignored patterns from
`.gitignore`

files, but there are two exceptions to be aware of:

- Special files such as
`biome.json`

and`.gitignore`

take priority over any ignored patterns in`files.includes`

. - If any rule from the project domain is enabled, the scanner will index source
files
*including their dependencies*. This means that files that are ignored as part of`files.includes`

may still get indexed by the scanner, as long as there is another included file that imports those files. And this also means that`.d.ts`

files and`package.json`

manifests inside`node_modules/`

may still get indexed too.

If you want to explicitly force some files to be ignored by the scanner, you can
do so using a so-called *force-ignore pattern*. A force-ignore pattern looks
like a regular negated pattern, but starts with a double exclamation mark
(`!!`

).

For example, you can tell Biome to never look inside any `dist/`

folder using
the following configuration:

We recommend using the force-ignore syntax for any folders that contain *output*
files, such as `build/`

and `dist/`

. For such folders, it is highly unlikely
that indexing has any useful benefits. For folders containing generated files,
we advise using regular ignore patterns so that type information can still be
extracted from the files.

For nested `biome.json`

files as well as `.gitignore`

files that you wish to
explicitly ignore, the force-ignore syntax must also be used.

`files.ignoreUnknown`

Section titled “files.ignoreUnknown”If `true`

, Biome won’t emit diagnostics if it encounters files that it can’t
handle.

Default:

`false`

`files.maxSize`

Section titled “files.maxSize”The maximum allowed size for source code files in bytes. Files above this limit will be ignored for performance reasons.

Default:

`1048576`

(1024*1024, 1MB)

`files.experimentalScannerIgnores`

Section titled “files.experimentalScannerIgnores”An array of literal path segments that the scanner should ignore during the crawling. The ignored files won’t be indexed, which means that these files won’t be part of the module graph, and types won’t be inferred from them.

Set of properties to integrate Biome with a VCS (Version Control Software).

`vcs.enabled`

Section titled “vcs.enabled”Whether Biome should integrate itself with the VCS client

Default:

`false`

`vcs.clientKind`

Section titled “vcs.clientKind”The kind of client.

Values:

`"git"`

`vcs.useIgnoreFile`

Section titled “vcs.useIgnoreFile”Whether Biome should use the project’s VCS ignore files. When `true`

, Biome will ignore the files
specified in the VCS ignore files as well as those specified in `.ignore`

files.

This feature supports nested ignore files too.

The root ignore file yields the same semantics as the root `files.includes`

.

`vcs.root`

Section titled “vcs.root”The folder where Biome should check for VCS files. By default, Biome will use the same
folder where `biome.json`

was found.

`vcs.defaultBranch`

Section titled “vcs.defaultBranch”The main branch of the project. Biome will use this branch when evaluating the changed files.

`linter`

Section titled “linter”`linter.enabled`

Section titled “linter.enabled”Enables Biome’s linter.

Default:

`true`

`linter.includes`

Section titled “linter.includes”A list of glob patterns of files to lint.

The following example lints all files with a `.js`

extension inside the `src`

folder:

`*`

is used to match *all files in a folder*, while `**`

*recursively* matches
all files and subfolders in a folder. For more information on globs, see the
glob syntax reference

`includes`

also supports negated patterns, or exceptions. These are patterns
that start with `!`

and they can be used to instruct Biome to process all files
*except* those matching the negated pattern.

Note that exceptions are processed in order, allowing you to specify exceptions to exceptions.

Consider the following example:

This example specifies that:

- All files inside all (sub)folders are linted, thanks to the
`**`

pattern… - …
*except*when those files have a`.test.js`

extension… - … but the file
`special.test.ts`

*is*still linted.

This means that:

`src/app.js`

**is**linted.`src/app.test.js`

**is not**linted.`src/special.test.js`

**is*linted.

Note that `linter.includes`

is applied *after* `files.includes`

. This means
that any file that is not matched by `files.includes`

can no longer be matched
`linter.includes`

. This means the following example **doesn’t work**:

If `linter.includes`

is not specified, all files matched by
`files.includes`

are linted.

`linter.rules.recommended`

Section titled “linter.rules.recommended”Enables the recommended rules for all groups.

Default:

`true`

`linter.rules.[group]`

Section titled “linter.rules.[group]”Options that influence the rules of a single group. Biome supports the following groups:

- accessibility: Rules focused on preventing accessibility problems.
- complexity: Rules that focus on inspecting complex code that could be simplified.
- correctness: Rules that detect code that is guaranteed to be incorrect or useless.
- nursery: New rules that are still under development. Nursery rules require explicit opt-in via configuration on stable versions because they may still have bugs or performance problems (even if they are marked as recommended). They are enabled by default on nightly builds, but as they are unstable their diagnostic severity may be set to either error or warning, depending on whether we intend for the rule to be recommended or not when it eventually gets stabilized. Nursery rules get promoted to other groups once they become stable or may be removed. Rules that belong to this group are not subject to semantic version.
- performance: Rules catching ways your code could be written to run faster, or generally be more efficient.
- security: Rules that detect potential security flaws.
- style: Rules enforcing a consistent and idiomatic way of writing your code.
- suspicious: Rules that detect code that is likely to be incorrect or useless.

Each group can accept, as a value, a string that represents the severity or an object where each rule can be configured.

When passing the severity, you can control the severity emitted by all the rules that belong to a group.
For example, you can configure the `a11y`

group to emit information diagnostics:

Here are the accepted values:

`"on"`

: each rule that belongs to the group will emit a diagnostic with the default severity of the rule. Refer to the documentation of the rule, or use the`explain`

command:`"off"`

: none of the rules that belong to the group will emit any diagnostics.`"info"`

: all rules that belong to the group will emit a diagnostic with information severity.`"warn"`

: all rules that belong to the group will emit a diagnostic with warning severity.`"error"`

: all rules that belong to the group will emit a diagnostic with error severity.

`linter.rules.[group].recommended`

Section titled “linter.rules.[group].recommended”Enables the recommended rules for a single group.

Example:

`assist`

Section titled “assist”`assist.enabled`

Section titled “assist.enabled”Enables Biome’s assist.

Default:

`true`

`assist.includes`

Section titled “assist.includes”A list of glob patterns of files to lint.

The following example analyzes all files with a `.js`

extension inside the `src`

folder:

`*`

is used to match *all files in a folder*, while `**`

*recursively* matches
all files and subfolders in a folder. For more information on globs, see the
glob syntax reference

`includes`

also supports negated patterns, or exceptions. These are patterns
that start with `!`

and they can be used to instruct Biome to process all files
*except* those matching the negated pattern.

Note that exceptions are processed in order, allowing you to specify exceptions to exceptions.

Consider the following example:

This example specifies that:

- All files inside all (sub)folders are analyzed, thanks to the
`**`

pattern… - …
*except*when those files have a`.test.js`

extension… - … but the file
`special.test.ts`

*is*still analyzed.

This means that:

`src/app.js`

**is**analysed.`src/app.test.js`

**is not**analyzed.`src/special.test.js`

**is*analyzed.

Note that `assist.includes`

is applied *after* `files.includes`

. This means
that any file that is not matched by `files.includes`

can no longer be matched
`assist.includes`

. This means the following example **doesn’t work**:

If `assist.includes`

is not specified, all files matched by
`files.includes`

are linted.

`assist.actions.recommended`

Section titled “assist.actions.recommended”Enables the recommended actions for all groups.

`assist.actions.[group]`

Section titled “assist.actions.[group]”Options that influence the rules of a single group. Biome supports the following groups:

- source: This group represents those actions that can be safely applied to a document upon saving. These actions are all generally safe, they typically don’t change the functionality of the program.

`assist.actions.[group].recommended`

Section titled “assist.actions.[group].recommended”Enables the recommended rules for a single group.

Example:

`formatter`

Section titled “formatter”These options apply to all languages. There are additional language-specific formatting options below.

`formatter.enabled`

Section titled “formatter.enabled”Enables Biome’s formatter.

Default:

`true`

`formatter.includes`

Section titled “formatter.includes”A list of glob patterns of files to format.

The following example formats all files with a `.js`

extension inside the `src`

folder:

`*`

is used to match *all files in a folder*, while `**`

*recursively* matches
all files and subfolders in a folder. For more information on globs, see the
glob syntax reference

`includes`

also supports negated patterns, or exceptions. These are patterns
that start with `!`

and they can be used to instruct Biome to process all files
*except* those matching the negated pattern.

Note that exceptions are processed in order, allowing you to specify exceptions to exceptions.

Consider the following example:

This example specifies that:

- All files inside all (sub)folders are formatted, thanks to the
`**`

pattern… - …
*except*when those files have a`.test.js`

extension… - … but the file
`special.test.ts`

*is*still formatted.

This means that:

`src/app.js`

**is**formatted.`src/app.test.js`

**is not**formatted.`src/special.test.js`

**is**formatted.

Note that `formatter.includes`

is applied *after* `files.includes`

. This means
that any file that is not matched by `files.includes`

can no longer be matched
`formatter.includes`

. This means the following example **doesn’t work**:

If `formatter.includes`

is not specified, all files matched by
`files.includes`

are formatted.

`formatter.formatWithErrors`

Section titled “formatter.formatWithErrors”Allows to format a document that has syntax errors.

Default:

`false`

`formatter.indentStyle`

Section titled “formatter.indentStyle”The style of the indentation. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`formatter.indentWidth`

Section titled “formatter.indentWidth”How big the indentation should be.

Default:

`2`

`formatter.lineEnding`

Section titled “formatter.lineEnding”The type of line ending.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`formatter.lineWidth`

Section titled “formatter.lineWidth”The amount of characters that can be written on a single line..

Default:

`80`

`formatter.attributePosition`

Section titled “formatter.attributePosition”The attribute position style in HTMLish languages.

`"auto"`

, the attributes are automatically formatted, and they will collapse in multiple lines only when they hit certain criteria;`"multiline"`

, the attributes will collapse in multiple lines if more than 1 attribute is used.

Default:

`"auto"`

`formatter.bracketSpacing`

Section titled “formatter.bracketSpacing”Choose whether spaces should be added between brackets and inner values.

Default:

`true`

`formatter.expand`

Section titled “formatter.expand”Whether to expand arrays and objects on multiple lines.

`"auto"`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line.`"always"`

, these literals are formatted on multiple lines, regardless of length of the list.`"never"`

, these literals are formatted on a single line if it fits in the line.

When formatting `package.json`

, Biome will use `always`

unless configured otherwise.

Default:

`"auto"`

`formatter.trailingNewline`

Section titled “formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`formatter.useEditorconfig`

Section titled “formatter.useEditorconfig”Whether Biome should use the `.editorconfig`

file to determine the formatting options.

The config files `.editorconfig`

and `biome.json`

will follow the following rules:

- Formatting settings in
`biome.json`

always take precedence over`.editorconfig`

files. `.editorconfig`

files that exist higher up in the hierarchy than a`biome.json`

file are already ignored. This is to avoid loading formatting settings from someone’s home directory into a project with a`biome.json`

file.- Nested
`.editorconfig`

files aren’t supported currently.

Default:

`false`

`javascript`

Section titled “javascript”These options apply only to JavaScript (and TypeScript) files.

`javascript.parser.unsafeParameterDecoratorsEnabled`

Section titled “javascript.parser.unsafeParameterDecoratorsEnabled”Allows to support the unsafe/experimental parameter decorators.

Default:

`false`

`javascript.parser.jsxEverywhere`

Section titled “javascript.parser.jsxEverywhere”When set to `true`

, allows to parse JSX syntax inside `.js`

files. When set to `false`

, Biome will raise diagnostics when it encounters JSX syntax inside `.js`

files.

Default:

`true`

`javascript.formatter.quoteStyle`

Section titled “javascript.formatter.quoteStyle”The type of quote used when representing string literals. It can be `"single"`

or `"double"`

.

Default:

`"double"`

`javascript.formatter.jsxQuoteStyle`

Section titled “javascript.formatter.jsxQuoteStyle”The type of quote used when representing jsx string literals. It can be `"single"`

or `"double"`

.

Default:

`"double"`

`javascript.formatter.quoteProperties`

Section titled “javascript.formatter.quoteProperties”When properties inside objects should be quoted. It can be `"asNeeded"`

or `"preserve"`

.

Default:

`"asNeeded"`

`javascript.formatter.trailingCommas`

Section titled “javascript.formatter.trailingCommas”Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Possible values:

`"all"`

, the trailing comma is always added;`"es5"`

, the trailing comma is added only in places where it’s supported by older version of JavaScript;`"none"`

, trailing commas are never added.

Default:

`"all"`

`javascript.formatter.semicolons`

Section titled “javascript.formatter.semicolons”It configures where the formatter prints semicolons:

`"always"`

, the semicolons is always added at the end of each statement;`"asNeeded"`

, the semicolons are added only in places where it’s needed, to protect from ASI.

Default:

`"always"`

Example:

`javascript.formatter.arrowParentheses`

Section titled “javascript.formatter.arrowParentheses”Whether to add non-necessary parentheses to arrow functions:

`"always"`

, the parentheses are always added;`"asNeeded"`

, the parentheses are added only when they are needed.

Default:

`"always"`

`javascript.formatter.enabled`

Section titled “javascript.formatter.enabled”Enables Biome’s formatter for JavaScript (and its super languages) files.

Default:

`true`

`javascript.formatter.indentStyle`

Section titled “javascript.formatter.indentStyle”The style of the indentation for JavaScript (and its super languages) files. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`javascript.formatter.indentWidth`

Section titled “javascript.formatter.indentWidth”How big the indentation should be for JavaScript (and its super languages) files.

Default:

`2`

`javascript.formatter.lineEnding`

Section titled “javascript.formatter.lineEnding”The type of line ending for JavaScript (and its super languages) files.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`javascript.formatter.lineWidth`

Section titled “javascript.formatter.lineWidth”The amount of characters that can be written on a single line in JavaScript (and its super languages) files.

Default:

`80`

`javascript.formatter.bracketSameLine`

Section titled “javascript.formatter.bracketSameLine”Choose whether the ending `>`

of a multi-line JSX element should be on the last attribute line or not

Default:

`false`

`javascript.formatter.bracketSpacing`

Section titled “javascript.formatter.bracketSpacing”Choose whether spaces should be added between brackets and inner values.

Default:

`true`

`javascript.formatter.attributePosition`

Section titled “javascript.formatter.attributePosition”The attribute position style in jsx elements.

`"auto"`

, do not enforce single attribute per line.`"multiline"`

, enforce single attribute per line.

Default:

`"auto"`

`javascript.formatter.expand`

Section titled “javascript.formatter.expand”Whether to expand arrays and objects on multiple lines.

`"auto"`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line.`"always"`

, these literals are formatted on multiple lines, regardless of length of the list.`"never"`

, these literals are formatted on a single line if it fits in the line.

Default:

`"auto"`

`javascript.formatter.operatorLinebreak`

Section titled “javascript.formatter.operatorLinebreak”When breaking binary expressions into multiple lines, whether to break them before or after the binary operator.

Default:

`"after"`

.

`"after`

: the operator is placed after the expression:`"before`

: the operator is placed before the expression:

`javascript.formatter.trailingNewline`

Section titled “javascript.formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`javascript.globals`

Section titled “javascript.globals”A list of global names that Biome should ignore (analyzer, linter, etc.)

`javascript.jsxRuntime`

Section titled “javascript.jsxRuntime”Indicates the type of runtime or transformation used for interpreting JSX.

`"transparent"`

— Indicates a modern or native JSX environment, that doesn’t require special handling by Biome.`"reactClassic"`

— Indicates a classic React environment that requires the`React`

import. Corresponds to the`react`

value for the`jsx`

option in TypeScript’s`tsconfig.json`

.

For more information about the old vs. new JSX runtime, please see: https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html

Default:

`"transparent"`

`javascript.linter.enabled`

Section titled “javascript.linter.enabled”Enables Biome’s linter for JavaScript (and its super languages) files.

Default:

`true`

`javascript.assist.enabled`

Section titled “javascript.assist.enabled”Enables Biome’s assist for JavaScript (and its super languages) files.

Default:

`true`

`javascript.experimentalEmbeddedSnippetsEnabled`

Section titled “javascript.experimentalEmbeddedSnippetsEnabled”Enables parsing and formatting embedded language snippets in JavaScript (and its super languages) files.

Default:

`false`

Options applied to the JSON files.

`json.parser.allowComments`

Section titled “json.parser.allowComments”Enables the parsing of comments in JSON files.

`json.parser.allowTrailingCommas`

Section titled “json.parser.allowTrailingCommas”Enables the parsing of trailing commas in JSON files.

`json.formatter.enabled`

Section titled “json.formatter.enabled”Enables Biome’s formatter for JSON (and its super languages) files.

Default:

`true`

`json.formatter.indentStyle`

Section titled “json.formatter.indentStyle”The style of the indentation for JSON (and its super languages) files. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`json.formatter.indentWidth`

Section titled “json.formatter.indentWidth”How big the indentation should be for JSON (and its super languages) files.

Default:

`2`

`json.formatter.lineEnding`

Section titled “json.formatter.lineEnding”The type of line ending for JSON (and its super languages) files.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`json.formatter.lineWidth`

Section titled “json.formatter.lineWidth”The amount of characters that can be written on a single line in JSON (and its super languages) files.

Default:

`80`

`json.formatter.trailingCommas`

Section titled “json.formatter.trailingCommas”Print trailing commas wherever possible in multi-line comma-separated syntactic structures.

Allowed values:

`"none"`

: the trailing comma is removed;`"all"`

: the trailing comma is kept**and**preferred.

Default:

`"none"`

`json.formatter.bracketSpacing`

Section titled “json.formatter.bracketSpacing”Choose whether spaces should be added between brackets and inner values.

Default:

`true`

`json.formatter.expand`

Section titled “json.formatter.expand”Whether to expand arrays and objects on multiple lines.

`"auto"`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line.`"always"`

, these literals are formatted on multiple lines, regardless of length of the list.`"never"`

, these literals are formatted on a single line if it fits in the line.

When formatting `package.json`

, Biome will use `always`

unless configured otherwise.

Default:

`"auto"`

`json.formatter.trailingNewline`

Section titled “json.formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`json.linter.enabled`

Section titled “json.linter.enabled”Enables Biome’s formatter for JSON (and its super languages) files.

Default:

`true`

`json.assist.enabled`

Section titled “json.assist.enabled”Enables Biome’s assist for JSON (and its super languages) files.

Default:

`true`

Options applied to the CSS files.

`css.parser.cssModules`

Section titled “css.parser.cssModules”Enables parsing of CSS modules

Default:

`false`

`css.parser.tailwindDirectives`

Section titled “css.parser.tailwindDirectives”Enables parsing of Tailwind specific syntax, like `@theme`

, `@utility`

and `@apply`

.

Default:

`false`

`css.formatter.enabled`

Section titled “css.formatter.enabled”Enables Biome’s formatter for CSS files.

Default:

`false`

`css.formatter.indentStyle`

Section titled “css.formatter.indentStyle”The style of the indentation for CSS files. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`css.formatter.indentWidth`

Section titled “css.formatter.indentWidth”How big the indentation should be for CSS files.

Default:

`2`

`css.formatter.lineEnding`

Section titled “css.formatter.lineEnding”The type of line ending for CSS files.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`css.formatter.lineWidth`

Section titled “css.formatter.lineWidth”The amount of characters that can be written on a single line in CSS files.

Default:

`80`

`css.formatter.quoteStyle`

Section titled “css.formatter.quoteStyle”The type of quote used when representing string literals. It can be `"single"`

or `"double"`

.

Default:

`"double"`

`css.formatter.trailingNewline`

Section titled “css.formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`css.linter.enabled`

Section titled “css.linter.enabled”Enables Biome’s linter for CSS files.

Default:

`true`

`css.assist.enabled`

Section titled “css.assist.enabled”Enables Biome’s assist for CSS files.

Default:

`true`

`graphql`

Section titled “graphql”Options applied to the GraphQL files.

`graphql.formatter.enabled`

Section titled “graphql.formatter.enabled”Enables Biome’s formatter for GraphQL files.

Default:

`false`

`graphql.formatter.indentStyle`

Section titled “graphql.formatter.indentStyle”The style of the indentation for GraphQL files. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`graphql.formatter.indentWidth`

Section titled “graphql.formatter.indentWidth”How big the indentation should be for GraphQL files.

Default:

`2`

`graphql.formatter.lineEnding`

Section titled “graphql.formatter.lineEnding”The type of line ending for GraphQL files.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`graphql.formatter.lineWidth`

Section titled “graphql.formatter.lineWidth”The amount of characters that can be written on a single line in GraphQL files.

Default:

`80`

`graphql.formatter.quoteStyle`

Section titled “graphql.formatter.quoteStyle”The type of quote used when representing string literals. It can be `"single"`

or `"double"`

.

Default:

`"double"`

`graphql.formatter.trailingNewline`

Section titled “graphql.formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`graphql.linter.enabled`

Section titled “graphql.linter.enabled”Enables Biome’s linter for GraphQL files.

Default:

`true`

`graphql.assist.enabled`

Section titled “graphql.assist.enabled”Enables Biome’s assist for GraphQL files.

Default:

`true`

Options applied to the Grit files.

`grit.formatter.enabled`

Section titled “grit.formatter.enabled”Enables Biome’s formatter for Grit files.

Default:

`false`

`grit.formatter.indentStyle`

Section titled “grit.formatter.indentStyle”The style of the indentation for Grit files. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`grit.formatter.indentWidth`

Section titled “grit.formatter.indentWidth”How big the indentation should be for Grit files.

Default:

`2`

`grit.formatter.lineEnding`

Section titled “grit.formatter.lineEnding”The type of line ending for Grit files.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`grit.formatter.lineWidth`

Section titled “grit.formatter.lineWidth”The amount of characters that can be written on a single line in Grit files.

Default:

`80`

`grit.formatter.quoteStyle`

Section titled “grit.formatter.quoteStyle”The type of quote used when representing string literals. It can be `"single"`

or `"double"`

.

Default:

`"double"`

`grit.formatter.trailingNewline`

Section titled “grit.formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`grit.linter.enabled`

Section titled “grit.linter.enabled”Enables Biome’s linter for Grit files.

Default:

`true`

`grit.assist.enabled`

Section titled “grit.assist.enabled”Enables Biome’s assist for Grit files.

Default:

`true`

`html.experimentalFullSupportEnabled`

Section titled “html.experimentalFullSupportEnabled”When enabled, Biome enables full support for HTML-ish languages (Vue, Svelte, and Astro files). Parsing, formatting and linting of embedded languages inside these files are consistent.

When disabled, Biome will only extract the JavaScript/TypeScript parts of these files for analysis, while ignoring the rest of the content.

`html.parser.interpolation`

Section titled “html.parser.interpolation”Enables the parsing of double text expressions such as `{{ expression }}`

inside `.html`

files.

Default:

`false`

`html.formatter.enabled`

Section titled “html.formatter.enabled”Enables Biome’s formatter for HTML files.

Default:

`false`

`html.formatter.indentStyle`

Section titled “html.formatter.indentStyle”The style of the indentation for HTML files. It can be `"tab"`

or `"space"`

.

Default:

`"tab"`

`html.formatter.indentWidth`

Section titled “html.formatter.indentWidth”How big the indentation should be for HTML files.

Default:

`2`

`html.formatter.lineEnding`

Section titled “html.formatter.lineEnding”The type of line ending for HTML files.

`"lf"`

, Line Feed only (`\n`

), common on Linux and macOS as well as inside git repos;`"crlf"`

, Carriage Return + Line Feed characters (`\r\n`

), common on Windows;`"cr"`

, Carriage Return character only (`\r`

), used very rarely.

Default:

`"lf"`

`html.formatter.lineWidth`

Section titled “html.formatter.lineWidth”The amount of characters that can be written on a single line in HTML files.

Default:

`80`

`html.formatter.attributePosition`

Section titled “html.formatter.attributePosition”The attribute position style in HTML elements.

`"auto"`

, the attributes are automatically formatted, and they will collapse in multiple lines only when they hit certain criteria;`"multiline"`

, the attributes will collapse in multiple lines if more than 1 attribute is used.

Default:

`"auto"`

`html.formatter.bracketSameLine`

Section titled “html.formatter.bracketSameLine”Whether to hug the closing bracket of multiline HTML tags to the end of the last line, rather than being alone on the following line.

Default:

`false`

`html.formatter.whitespaceSensitivity`

Section titled “html.formatter.whitespaceSensitivity”Whether to account for whitespace sensitivity when formatting HTML (and its super languages).

Default: “css”

-
`"css"`

: The formatter considers whitespace significant for elements that have an “inline” display style by default in browser’s user agent style sheets. -
`"strict"`

: Leading and trailing whitespace in content is considered significant for all elements.The formatter should leave at least one whitespace character if whitespace is present. Otherwise, if there is no whitespace, it should not add any after

`>`

or before`<`

. In other words, if there’s no whitespace, the text content should hug the tags.Example of text hugging the tags:

-
`"ignore"`

: whitespace is considered insignificant. The formatter is free to remove or add whitespace as it sees fit.

`html.formatter.indentScriptAndStyle`

Section titled “html.formatter.indentScriptAndStyle”*Since 2.3: Only affects .vue and .svelte files*

Whether to indent the content of `<script>`

and `<style>`

tags for Vue and Svelte files. Currently, this does not apply to plain HTML files.

Default:

`false`

When true, the content of `<script>`

and `<style>`

tags will be indented by one level relative to the tags.

`html.formatter.selfCloseVoidElements`

Section titled “html.formatter.selfCloseVoidElements”Whether void elements should be self-closed. Defaults to never.

Default:

`"never"`

`"never"`

: The slash`/`

inside void elements is removed by the formatter.`"always"`

: The slash`/`

inside void elements is always added.

`html.formatter.trailingNewline`

Section titled “html.formatter.trailingNewline”Whether to add a trailing newline at the end of the file.

Defaults to true.

`html.linter.enabled`

Section titled “html.linter.enabled”Enables Biome’s linter for HTML files.

Default:

`true`

`html.assist.enabled`

Section titled “html.assist.enabled”Enables Biome’s assist for HTML files.

Default:

`true`

`overrides`

Section titled “overrides”A list of patterns.

Use this configuration to change the behaviour of the tools for certain files.

When a file is matched against an override pattern, the configuration specified in that pattern will be override the top-level configuration.

The order of the patterns matter. If a file *can* match three patterns, only the first one is used.

`overrides.<ITEM>.includes`

Section titled “overrides.<ITEM>.includes”A list of glob patterns of files for which to apply customised settings.

`overrides.<ITEM>.formatter`

Section titled “overrides.<ITEM>.formatter”Includes the options of the top level formatter configuration, minus `ignore`

and `include`

.

#### Examples

Section titled “Examples”For example, it’s possible to modify the formatter `lineWidth`

, `indentStyle`

for certain files that are included in the glob path `generated/**`

:

`overrides.<ITEM>.linter`

Section titled “overrides.<ITEM>.linter”Includes the options of the top level linter configuration, minus `ignore`

and `include`

.

#### Examples

Section titled “Examples”You can disable certain rules for certain glob paths, and disable the linter for other glob paths:

`overrides.<ITEM>.javascript`

Section titled “overrides.<ITEM>.javascript”Includes the options of the top level javascript configuration. Lets you override JavaScript-specific settings for certain files.

#### Examples

Section titled “Examples”You can change the formatting behaviour of JavaScript files in certain folders:

`overrides.<ITEM>.json`

Section titled “overrides.<ITEM>.json”Includes the options of the top level json configuration. Lets you override JSON-specific settings for certain files.

#### Examples

Section titled “Examples”You can enable parsing features for certain JSON files:

`overrides.<ITEM>.[language]`

Section titled “overrides.<ITEM>.[language]”Includes the options of the top level language configuration. Lets you override language-specific settings for certain files.

## Glob syntax reference

Section titled “Glob syntax reference”Glob patterns are used to match paths of files and folders. Biome supports the following syntax in globs:

`*`

matches zero or more characters. It cannot match the path separator`/`

.`**`

recursively matches directories and files. This sequence must be used as an entire path component, so both`**a`

and`b**`

are invalid and will result in an error. A sequence of more than two consecutive`*`

characters is also invalid.`[...]`

matches any character inside the brackets. Ranges of characters can also be specified, as ordered by Unicode, so e.g.`[0-9]`

specifies any character between 0 and 9 inclusive.`[!...]`

is the negation of`[...]`

, i.e. it matches any characters**not**in the brackets.- If the entire glob starts with
`!`

, it is a so-called negated pattern. This glob only matches if the path*doesn’t*match the glob. Negated patterns cannot be used alone, they can only be used as*exception*to a regular glob. - When determining whether a file is included or not, Biome considers the parent
folders too. This means that if you want to
*include*all files in a folder, you need to use the`/**`

suffix to match those files. But if you want to*ignore*all files in a folder, you may do so without the`/**`

suffix. We recommend ignoring folders without the trailing`/**`

, to avoid needlessly traversing it, as well as to avoid the risk of Biome loading a`biome.json`

or a`.gitignore`

file from an ignored folder.

Some examples:

`dist/**`

matches the`dist/`

folder and all files inside it.`!dist`

ignores the`dist/`

folder and all files inside it.`**/test/**`

matches all files under any folder named`test`

, regardless of where they are. E.g.`dist/test`

,`src/test`

.`**/*.js`

matches all files ending with the extension`.js`

in all folders.

Copyright (c) 2023-present Biome Developers and Contributors.
