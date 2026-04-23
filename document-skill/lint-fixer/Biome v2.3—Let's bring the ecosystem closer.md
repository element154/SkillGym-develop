# Biome v2.3—Let's bring the ecosystem closer

We’re excited to announce the release of Biome 2.3, bringing several features that have been highly requested by the community. This release marks a significant milestone in our journey to support the broader web ecosystem.

Once you have upgraded to Biome v2.3.0, migrate your Biome configuration to the new version by running the `migrate`

command:

## Full support for Vue, Svelte, and Astro

Section titled “Full support for Vue, Svelte, and Astro”Biome 2.3 introduces full support for Vue, Svelte, and Astro files. This means you can now format and lint the JavaScript and TypeScript code inside `<script>`

tags, as well as the CSS inside `<style>`

tags in these frameworks. The HTML/template portions of these files are also parsed and formatted according to Biome’s HTML formatting rules.

This achievement wouldn’t have been possible without the great efforts of Core Contributor @ematipico and Core Contributor @dyc3 .

This is a feature that many developers have been asking for, and we’re thrilled to finally deliver it. Achieving this has had its challenges, and it required extensive trials to get the architecture right based on the constraints of the toolchain.

However, this feature is marked as **experimental** for several important reasons. First, these frameworks have their own specific syntaxes and idioms that extend beyond standard HTML, CSS, and JavaScript. While we’ve done extensive work to handle many patterns, there are cases and framework-specific syntaxes that may not yet be fully supported (for example Svelte control-flow syntax, or Astro JSX-like syntax). We encourage you to avail of this new feature, and fine-tune it based on your needs and possible limitations found.

Please open a discussion if you find something that hasn’t been implemented, or an issue if there’s a parsing error that should be handled correctly.

To enable the feature, you’ll have to opt in the new `html.experimentalFullSupportEnabled`

option:

### Script and style indentation

Section titled “Script and style indentation”Additionally, you can configure specific formatting options for HTML content, such as whether to indent the content of `<script>`

and `<style>`

tags:

By default, `indentScriptAndStyle`

is set to `false`

to match Prettier’s behavior.

### Possible inconsistencies

Section titled “Possible inconsistencies”With this release, we step into something new that needs to be addressed and discussed. In Biome you can configure each language as you see fit, which means that a project *might end up with different formatting (as example)*.

In the following configuration file, JavaScript files are formatted using double quotes, while CSS files are formatted using single quotes.

Why would someone want that? That’s not for us to answer, however with a configuration like this you would end with **different quotes inside your HTML-ish files**.
This could cause inconsistencies inside the same. We created a GitHub discussion to understand if this is a problem, and if so, how Biome should solve it. Please let us know what do you think.

## New ignore syntax

Section titled “New ignore syntax”Biome 2.3 introduces a refined syntax for ignoring paths in your project, addressing important problems that arose since the introduction of multi file analysis and TypeScript inference.

When Biome 2.0 came out, we internally introduced the concept of “paths being indexed”. When a path is indexed, Biome parses it and updates the module graph and the type inference, if enabled.

However, we slowly came to the realization that multi-file analysis and type inference are very complex problems that can get out of hand easily.

For example, type inference can enter a very nasty loop where tons of types are recursively indexed, consuming a lot of memory.

As for multi-file analysis, the `node_modules/`

folder can be a rabbit hole, full of symbolic links with high depths and path names that exceed the maximum allowed characters.

Solving these complex problems takes time, a lot of testing and patience from us and the community. With this new syntax, users have now more control over what Biome can and can’t do.

With this release, two syntaxes are now available:

`!`

(single exclamation mark): Ignores the path from linting and formatting, but still allows it to be indexed by the type system. This is useful for generated files or third-party code that you don’t want to format or lint, but still need for type inference and imports.`!!`

(double exclamation mark): Completely ignores the path from all Biome operations, including type indexing. This is useful for files that should be entirely excluded from Biome’s analysis, such as`dist/`

folders.

This distinction is particularly important when working with TypeScript projects that rely on type inference from dependencies or generated code. By using `!`

, you can exclude these files from formatting and linting while still maintaining correct type information across your project.

Here’s an example configuration:

In this configuration, files in the `generated/`

directory are ignored for formatting and linting but remain indexed for types and module graph, while files in `dist/`

directory are completely excluded from all Biome operations.

This is an important tool **at your disposal** that allows you to control Biome, and avoid possible slowness and memory leaks.

As result, the option `files.experimentalScannerIgnores`

has been **deprecated**. We plan to remove this option in the next releases. Run the `biome migrate`

command update your configuration file.

Great shoutout to Core Contributor @arendjr for implementing this new feature.

## Tailwind v4 support

Section titled “Tailwind v4 support” Core Contributor @dyc3 worked really hard, and he shipped for us **native support** of tailwind files!

This is a opt-in feature of the CSS parser, and you can enable it using the new `css.parser.tailwindDirectives`

option:

## Lint rules

Section titled “Lint rules”### Promoted rules

Section titled “Promoted rules”- Promoted
`noNonNullAssertedOptionalChain`

to the suspicious group - Promoted
`useReactFunctionComponents`

to the`style`

group - Promoted
`useImageSize`

to the`correctness`

group - Promoted
`useConsistentTypeDefinitions`

to the`style`

group - Promoted
`useQwikClasslist`

to the`correctness`

group - Promoted
`noSecrets`

to the`security`

group

### Removed rules

Section titled “Removed rules”Removed nursery lint rule `useAnchorHref`

, because its use case is covered by `useValidAnchor`

.

### Updated the `react`

domain

Section titled “Updated the react domain”The following rules are now a part of the `react`

domain, and they won’t be enabled automatically unless you enabled the domain, or Biome detects `react`

as a dependency of your closest `package.json`

:

`lint/correctness/noChildrenProp`

(recommended)`lint/correctness/noReactPropAssignments`

`lint/security/noDangerouslySetInnerHtml`

(recommended)`lint/security/noDangerouslySetInnerHtmlWithChildren`

(recommended)`lint/style/useComponentExportOnlyModules`

`lint/suspicious/noArrayIndexKey`

(recommended)

## Improved `--skip`

and `--only`

flags

Section titled “Improved --skip and --only flags”The flags `--skip`

and `--only`

have been enhanced, and they can accept lint domains too.

In the following example, the `lint`

command runs only the rules that belong to the `project`

domain:

In the following example, the `lint`

command runs all the rules that you configured, expect for the rules that belong to the `test`

domain:

## Enhanced `init`

command

Section titled “Enhanced init command”The `init`

command now checks if the project contains ignore files and `dist/`

folders. If supported ignore files are found, Biome will
enable the VCS integration, and if `dist/`

folder is found, it will exclude it using the new ignore syntax. This should help reducing
the friction when starting with Biome:

## New reporters

Section titled “New reporters”Two new CLI reporters have been added:

- checkstyle reporter via the new option
`--reporter=checkstyle`

- RDJSON reporter via the new option
`--reporter=rdjson`

## New CLI flags

Section titled “New CLI flags”We added the new CLI flags to better control Biome without relying on the configuration file. Here’s the list:

`--format-with-errors`

: CLI flag that allows to format code that contains parse errors.`--css-parse-css-modules`

: CLI flag to control whether CSS Modules syntax is enabled.`--css-parse-tailwind-directives`

: CLI flag to control whether Tailwind CSS 4.0 directives and functions are enabled.`--json-parse-allow-comments`

: CLI flag to control whether comments are allowed in JSON files.`--json-parse-allow-trailing-commas`

: CLI flag to control whether trailing commas are allowed in JSON files.

`lineEnding`

format option

Section titled “lineEnding format option”The option `lineEnding`

now has a variant called `auto`

to match the operating system’s expected
line-ending style: on Windows, this will be CRLF (`\r\n`

), and on macOS / Linux, this will
be LF (`\n`

).

This allows for cross-platform projects that use Biome not to have to force one option or the other, which aligns better with Git’s default behavior on these platforms.

## And more!

Section titled “And more!”More features and fixes have been shipped, like React v19 support, `baseUrl`

support inside `tsconfig.json`

, and more. Refer to the changelog page for a detailed breakdown of the features.

## I like where this is going, how can I help?

Section titled “I like where this is going, how can I help?”I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome 😁

#### Translations

Section titled “Translations”If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this dashboard, you can check the supported languages and if they are up to date.

#### Chat with us

Section titled “Chat with us”Join our Discord server, and engage with the community. Chatting with the community and being part of the community is a form of contribution.

#### Code contributions

Section titled “Code contributions”If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project that does for you!

There are numerous aspects to explore; I assure you that you won’t get bored. Here is a small list of the things you can start with:

- Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have a very extensive technical guide.
- Help building Biome parsers! One interesting fact about Biome parsers is that they are recoverable parsers error resilient which emit a CST instead of a classic AST.
- Implement new capabilities in our LSP (Language Server Protocol), or add new features in one of our editor extensions: VS Code, Zed and JetBrains IntelliJ.

#### Financial help

Section titled “Financial help”If you believe in the future of the project, you can also help with a financial contribution, via Open Collective or GitHub Sponsors.

Additionally, the project provides an enterprise support program where a company you can employ one of the core contributors to work a specific aspect of the Biome toolchain.

Copyright (c) 2023-present Biome Developers and Contributors.
