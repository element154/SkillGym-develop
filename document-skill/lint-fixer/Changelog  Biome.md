# Changelog

# Biome changelog

Section titled “Biome changelog”This project follows Semantic Versioning. Due to the nature of Biome as a toolchain, it can be unclear what changes are considered major, minor, or patch. Read our guidelines to categorize a change.

New entries must be placed in a section entitled
`Unreleased`

. Read our guidelines for writing a good changelog entry.

## v1.9.4 (2024-10-17)

Section titled “v1.9.4 (2024-10-17)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”-
Implement GraphQL suppression action. Contributed by @vohoanglong0107

-
Improved the message for unused suppression comments. Contributed by @dyc3

-
Fix #4228, where the rule

`a11y/noInteractiveElementToNoninteractiveRole`

incorrectly reports a`role`

for non-interactive elements. Contributed by @eryue0220 -
`noSuspiciousSemicolonInJsx`

now catches suspicious semicolons in React fragments. Contributed by @vasucp1207 -
The syntax rule

`noTypeOnlyImportAttributes`

now ignores`.cts`

files (#4361).Since TypeScript 5.3, type-only imports can be associated to an import attribute in CommonJS-enabled files. See the TypeScript docs.

The following code is no longer reported as a syntax error:

Note that this is only allowed in files ending with the

`cts`

extension.Contributed by @Conaclos

#### Enhancements

Section titled “Enhancements”-
The

`--summary`

reporter now reports parsing diagnostics too. Contributed by @ematipico -
Improved performance of GritQL queries by roughly 25-30%. Contributed by @arendjr

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”- Fix an issue where the JSON schema marked lint rules options as mandatory. Contributed by @ematipico

### Editors

Section titled “Editors”### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #4121. Respect line width when printing multiline strings. Contributed by @ah-yu
- Fix #4384. Keep
`@charset`

dobule quote under any situation for css syntax rule. Contributed by @fireairforce

### JavaScript APIs

Section titled “JavaScript APIs”### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add useGuardForIn. Contributed by @fireairforce
- Add noDocumentCookie. Contributed by @tunamaguro
- Add noDocumentImportInPage. Contributed by @kaioduarte
- Add noDuplicateProperties. Contributed by @togami2864
- Add noHeadElement. Contributed by @kaioduarte
- Add noHeadImportInDocument. Contributed by @kaioduarte
- Add noImgElement. Contributed by @kaioduarte
- Add noUnknownTypeSelector. Contributed by @Kazuhiro-Mimaki
- Add useAtIndex. Contributed by @GunseiKPaseri
- Add noUselessStringRaw. Contributed by @fireairforce
- Add nursery/useCollapsedIf. Contributed by @siketyan
- Add useGoogleFontDisplay. Contributed by @kaioduarte
- Add useExportsLast. Contributed by @tommymorgan

#### Bug Fixes

Section titled “Bug Fixes”-
Biome no longer crashes when it encounters a string that contain a multibyte character (#4181).

This fixes a regression introduced in Biome 1.9.3 The regression affected the following linter rules:

`nursery/useSortedClasses`

`nursery/useTrimStartEnd`

`style/useTemplate`

`suspicious/noMisleadingCharacterClass`

Contributed by @Conaclos

-
Fix #4190, where the rule

`noMissingVarFunction`

wrongly reported a variable as missing when used inside a`var()`

function that was a newline. Contributed by @ematipico -
Fix #4041. Now the rule

`useSortedClasses`

won’t be triggered if`className`

is composed only by inlined variables. Contributed by @ematipico -
useImportType and useExportType now report useless inline type qualifiers (#4178).

The following fix is now proposed:

Contributed by @Conaclos

-
useExportType now reports ungrouped

`export from`

.The following fix is now proposed:

Contributed by @Conaclos

-
noVoidTypeReturn now accepts

`void`

expressions in return position (#4173).The following code is now accepted:

Contributed by @Conaclos

-
noUselessFragments now correctly handles fragments containing HTML escapes (e.g.

` `

) inside expression escapes`{ ... }`

(#4059).The following code is no longer reported:

Contributed by @fireairforce

-
noUnusedFunctionParameters and noUnusedVariables no longer reports a parameter as unused when another parameter has a constructor type with the same parameter name (#4227).

In the following code, the

`name`

parameter is no longer reported as unused.Contributed by @Conaclos

-
noUndeclaredDependencies now accepts dependency names with dots. Contributed by @Conaclos

-
useFilenamingConvention now correctly handles renamed exports (#4254).

The rule allows the filename to be named as one of the exports of the module. For instance, the file containing the following export can be named

`Button`

.The rule now correctly handles the renaming of an export. For example, the file containing the following export can only be named

`Button`

. Previously the rule expected the file to be named`A`

.Contributed by @Conaclos

-
useConsistentMemberAccessibility now ignore private class members such as

`#property`

(#4276). Contributed by @Conaclos -
noUnknownFunction correctly handles

`calc-size`

function (#4212).The following code

`calc-size`

is no longer reported as unknown:Contributed by @fireairforce

-
useNamingConvention now allows configuring conventions for readonly index signatures.

Contributed by @sepruko

- noDuplicateCustomProperties now correctly handles custom properties and ignores non-custom properties. Previously, the rule incorrectly reported duplicates for all properties, including non-custom ones. Contributed by @togami2864

### Parser

Section titled “Parser”#### Bug Fixes

Section titled “Bug Fixes”-
The CSS parser now accepts more emoji in identifiers (#3627).

Browsers accept more emoji than the standard allows. Biome now accepts these additional emojis.

The following code is now correctly parsed:

Contributed by @Conaclos

-
Add support for parsing typescript’s

`resolution-mode`

in Import Types(#2115)Contributed by @fireairforce

## v1.9.3 (2024-10-01)

Section titled “v1.9.3 (2024-10-01)”#### New features

Section titled “New features”-
GritQL queries that match functions or methods will now match async functions or methods as well.

If this is not what you want, you can capture the

`async`

keyword (or its absence) in a metavariable and assert its emptiness:Contributed by @arendjr

#### Bug fixes

Section titled “Bug fixes”-
Fix #4077: Grit queries no longer need to match the statement’s trailing semicolon. Contributed by @arendjr

-
Fix #4102. Now the CLI command

`lint`

doesn’t exit with an error code when using`--write`

/`--fix`

. Contributed by @ematipico

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”- Fix #4125, where
`noLabelWithoutControl`

options where incorrectly marked as mandatory. Contributed by @ematipico

### Editors

Section titled “Editors”- Fix a case where CSS files weren’t correctly linted using the default configuration. Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”- Fix #4116. Unify LSP code action kinds. Contributed by @vitallium

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”-
Fix #3924 where GraphQL formatter panics in block comments with empty line. Contributed by @vohoanglong0107

-
Fix #3364 where the

`useSelfClosingElements`

rule forces the`script`

tag to be self-closing. Previously, this rule applies to all elements and cannot be disabled for native HTML elements.Now, this rule accepts a

`ignoreHtmlElements`

option, which when set to`true`

, ignores native HTML elements and allows them to be non-self-closing.Contributed by @abidjappie

-
Fix a case where raw values inside

`url()`

functions weren’t properly trimmed.Contributed by @ematipico

-
Fixed #4076, where a media query wasn’t correctly formatted:

Contributed by @blaze-d83

### JavaScript API

Section titled “JavaScript API”#### Bug fixes

Section titled “Bug fixes”- Fix #3881, by updating the APIs to use the latest WASM changes. Contributed by @ematipico

### Linter

Section titled “Linter”#### New features

Section titled “New features”-
Add noDescendingSpecificity. Contributed by @tunamaguro

-
Add noNestedTernary. Contributed by @kaykdm

-
Add noTemplateCurlyInString. Contributed by @fireairforce

-
Add noOctalEscape. Contributed by @fireairforce

#### Enhancements

Section titled “Enhancements”-
Add an option

`reportUnnecessaryDependencies`

to useExhaustiveDependencies.Defaults to true. When set to false, errors will be suppressed for React hooks that declare dependencies but do not use them.

Contributed by @simon-paris

-
Add an option

`reportMissingDependenciesArray`

to useExhaustiveDependencies. Contributed by @simon-paris

#### Bug fixes

Section titled “Bug fixes”-
noControlCharactersInRegex no longer panics on regexes with incomplete escape sequences. Contributed by @Conaclos

-
noMisleadingCharacterClass no longer reports issues outside of character classes.

The following code is no longer reported:

Contributed by @Conaclos

-
noUndeclaredDependencies no longer reports Node.js builtin modules as undeclared dependencies.

The rule no longer reports the following code:

Contributed by @Conaclos

-
noUnusedVariables no longer panics when suggesting the renaming of a variable at the start of a file (#4114). Contributed by @Conaclos

-
noUselessEscapeInRegex no longer panics on regexes that start with an empty character class. Contributed by @Conaclos

-
noUselessStringConcat no longer panics when it encounters malformed code. Contributed by @Conaclos

-
noUnusedFunctionParameters no longer reports unused parameters inside an object pattern with a rest parameter.

In the following code, the rule no longer reports

`a`

as unused.This matches the behavior of noUnusedVariables.

Contributed by @Conaclos

-
useButtonType no longer reports dynamically created button with a valid type (#4072).

The following code is no longer reported:

Contributed by @Conaclos

-
useSemanticElements now ignores elements with the

`img`

role (#3994).MDN recommends using

`role="img"`

for grouping images or creating an image from other elements. The following code is no longer reported:Contributed by @Conaclos

-
useSemanticElements now ignores

`alert`

and`alertdialog`

roles (#3858). Contributed by @Conaclos -
noUselessFragments don’t create invalid JSX code when Fragments children contains JSX Expression and in a LogicalExpression. Contributed by @fireairforce

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”- Forbid undefined as type name for typescript parser. Contributed by @fireairforce

## v1.9.2 (2024-09-19)

Section titled “v1.9.2 (2024-09-19)”#### New features

Section titled “New features”-
Added support for custom GritQL definitions, including:

- Pattern and predicate definitions: https://docs.grit.io/guides/patterns
- Function definitions: https://docs.grit.io/language/functions#function-definitions

Contributed by @arendjr

#### Bug fixes

Section titled “Bug fixes”- Fix #3917, where the fixed files were incorrectly computed. Contributed by @ematipico
- Fixed an issue that caused GritQL
`contains`

queries to report false positives when the matched node appeared inside a sibling node. Contributed by @arendjr

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”-
Fix #3923. Now the

`.editorconfig`

is correctly parsed by the LSP, and the options are correctly applied to files when formatting is triggered. Plus, the Biome LSP now watches for any change to the`.editorconfig`

, and updates the formatting settings. -
Reduced the number of log files generated by the LSP server. Now the maximum number of logs saved on disk is **seven **. Contributed by @ematipico

-
Fix the code actions capabilities available in the LSP Biome server. Before, the LSP was using the default capabilities, which resulted in pulling code actions even when they were disabled by the editor.

This means that the code actions are pulled by the client

**only**when the editor enables`quickfix.biome`

,`source.organizeImports.biome`

and`source.fixAll.biome`

.Now, if you enable

`organizeImports.enabled: true`

in the`biome.json`

, and then you configure your editor with the following code action`source.organizeImports.biome: false`

, the editor**won’t**sort the imports.Contributed by @ematipico

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add nursery/noMissingVarFunction. Contributed by @michellocana
- Add nursery/useComponentExportOnlyModules. Use this rule in React projects to enforce a code styling that fits React Refresh. Contributed by @GunseiKPaseri

#### Bug fixes

Section titled “Bug fixes”-
noLabelWithoutControl now accept JSX expression as label value (#3875). Contributed by @Conaclos

-
useFilenamingConvention no longer suggests names with a disallowed case (#3952). Contributed by @Conaclos

-
useFilenamingConvention now recognizes file names starting with ASCII digits as lowercase (#3952).

Thus,

`2024-09-17-filename`

,`2024_09_17_filename`

and`20240917FileName`

are in`kebab-case`

,`snake_case`

, and`camelCase`

respectively.Contributed by @Conaclos

-
useFilenamingConvention now applies the configured formats to the file extensions (#3650). Contributed by @Conaclos

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”-
useStrictMode now reports Script files with some directives, but without the

`use strict`

directive. Contributed by @Conaclos -
The CSS parser now accepts the characters U+FFDCF and U+FFFD in identifiers. Contributed by @Conaclos

## v1.9.1 (2024-09-15)

Section titled “v1.9.1 (2024-09-15)”#### Bug fixes

Section titled “Bug fixes”`useEditorConfig`

now loads the editorconfig when running`biome ci`

#3864. Contributed by @dyc3

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Revert #3731 to fix broken quick fixes and code actions. Contributed by @nhedger

### Linter

Section titled “Linter”#### New Features

Section titled “New Features”- Add nursery/noProcessEnv. Contributed by @unvalley

#### Bug fixes

Section titled “Bug fixes”- noUndeclaredDependencies now ignores
`@/`

imports and recognizes type imports from Definitely Typed and`bun`

imports. Contributed by @Conaclos

## v1.9.0 (2024-09-12)

Section titled “v1.9.0 (2024-09-12)”### Analyzer

Section titled “Analyzer”- Implement the semantic model for CSS. Contributed by @togami2864

#### New features

Section titled “New features”-
Add

`--graphql-linter-enabled`

option, to control whether the linter should be enabled or not for GraphQL files. Contributed by @ematipico -
New EXPERIMENTAL

`search`

command. The search command allows you to search a Biome project using GritQL syntax.GritQL is a powerful language that lets you do

*structural*searches on your codebase. This means that trivia such as whitespace or even the type of strings quotes used will be ignored in your search query. It also has many features for querying the structure of your code, making it much more elegant for searching code than regular expressions.While we believe this command may already be useful to users in some situations (especially when integrated in the IDE extensions!), we also had an ulterior motive for adding this command: We intend to utilize GritQL for our plugin efforts, and by allowing our users to try it out in a first iteration, we hope to gain insight in the type of queries you want to do, as well as the bugs we need to focus on.

For now, the

`search`

command is explicitly marked as EXPERIMENTAL, since many bugs remain. Keep this in mind when you try it out, and please let us know your issues!Note: GritQL escapes code snippets using backticks, but most shells interpret backticks as command invocations. To avoid this, it’s best to put

*single quotes*around your Grit queries.Contributed by @arendjr and @BackupMiles

-
The option

`--max-diagnostics`

now accept a`none`

value, which lifts the limit of diagnostics shown. Contributed by @ematipico-
Add a new reporter

`--reporter=gitlab`

, that emits diagnostics for using the GitLab Code Quality report.Contributed by @NiclasvanEyk

-
-
Add new options to the

`lsp-proxy`

and`start`

commands:`--log-path`

: a directory where to store the daemon logs. The commands also accepts the environment variable`BIOME_LOG_PATH`

.`--log-prefix-name`

: a prefix that’s added to the file name of the logs. It defaults to`server.log`

. The commands also accepts the environment variable`BIOME_LOG_PREFIX_NAME`

.

@Contributed by @ematipico

#### Enhancements

Section titled “Enhancements”-
When a

`--reporter`

is provided, and it’s different from the default one, the value provided by via`--max-diagnostics`

is ignored and**the limit is lifted**. Contributed by @ematipico -
`biome init`

now generates a new config file with more options set. This change intends to improve discoverability of the options and to set the more commonly used options to their default values. Contributed by @Conaclos -
The

`--verbose`

flag now reports the list of files that were evaluated, and the list of files that were fixed. The * *evaluated ** files are the those files that can be handled by Biome, files that are ignored, don’t have an extension or have an extension that Biome can’t evaluate are excluded by this list. The **fixed** files are those files that were handled by Biome and *changed*. Files that stays the same after the process are excluded from this list.Contributed by @ematipico

-
Allow passing

`nursery`

to the`--only`

and`--skip`

filters.The

`--only`

option allows you to run a given rule or rule group. The`--skip`

option allows you to skip the execution of a given group or a given rule.Previously, it was not possible to pass

`nursery`

. This restriction is now removed, as it may make sense to skip the nursery rules that a project has enabled.Contributed by @Conaclos

-
The CLI now returns an error code when calling a command in

`stdin`

mode, and the contents of the files aren’t fixed. For example, the following example will result in an error code of`1`

because the`lint`

command triggers some lint rules:Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”-
`biome lint --write`

now takes`--only`

and`--skip`

into account (#3470). Contributed by @Conaclos -
Fix #3368, now the reporter

`github`

tracks the diagnostics that belong to formatting and organize imports. Contributed by @ematipico -
Fix #3545, display a warning, ‘Avoid using unnecessary Fragment,’ when a Fragment contains only one child element that is placed on a new line. Contributed by @satojin219

-
Migrating from Prettier or ESLint no longer overwrite the

`overrides`

field from the configuration (#3544). Contributed by @Conaclos -
Fix JSX expressions for

`noAriaHiddenOnFocusable`

(#3708). Contributed by @anthonyshew -
Fix edge case for

`<canvas>`

elements that use`role="img"`

(#3728). Contributed by @anthonyshew -
Fix #3633, where diagnostics where incorrectly printed if the code has errors. Contributed by @ematipico

-
Allow

`aria-label`

on heading to prevent`useHeadingContent`

diagnostic (#3767). Contributed by @anthonyshew -
Fix edge case #3791 for rule

`noFocusedTests`

being used with non-string-like expressions (#3793). Contributed by @h-a-n-a -
Fix optional ARIA properties for

`role="separator"`

in`useAriaPropsForRole`

(#3856). Contributed by @anthonyshew

### Configuration

Section titled “Configuration”-
Add support for loading configuration from

`.editorconfig`

files (#1724).Configuration supplied in

`.editorconfig`

will be overridden by the configuration in`biome.json`

. Support is disabled by default and can be enabled by adding the following to your formatter configuration in`biome.json`

:Contributed by @dyc3

-
`overrides`

from an extended configuration is now merged with the`overrides`

of the extension.Given the following shared configuration

`biome.shared.json`

:and the following configuration:

Previously, the

`overrides`

from`biome.shared.json`

was overwritten. It is now merged and results in the following configuration:Contributed by @Conaclos

### Editors

Section titled “Editors”-
Fix #3577, where the update of the configuration file was resulting in the creation of a new internal project. Contributed by @ematipico

-
Fix #3696, where

`biome.jsonc`

was incorrectly parsed with incorrect options. Contributed by @ematipico

### Formatter

Section titled “Formatter”-
The CSS formatter is enabled by default. Which means that you don’t need to opt-in anymore using the configuration file

`biome.json`

:Contributed by @ematipico

-
Add parentheses for nullcoalescing in ternaries.

This change aligns on Prettier 3.3.3. This adds clarity to operator precedence.

Contributed by @Conaclos

-
Keep the parentheses around

`infer ... extends`

declarations in type unions and type intersections (#3419). Contributed by @Conaclos -
Keep parentheses around a

`yield`

expression inside a type assertion.Previously, Biome removed parentheses around some expressions that require them inside a type assertion. For example, in the following code, Biome now preserves the parentheses.

Contributed by @Conaclos

-
Remove parentheses around expressions that don’t need them inside a decorator.

Biome now matches Prettier in the following cases:

Contributed by @Conaclos

-
Keep parentheses around objects preceded with a

`@satisfies`

comment.In the following example, parentheses are no longer removed.

Contributed by @Conaclos

### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”New rules are incubated in the nursery group. Once stable, we promote them to a stable group.

The following CSS rules are promoted:

- a11y/useGenericFontNames
- correctness/noInvalidDirectionInLinearGradient
- correctness/noInvalidGridAreas
- correctness/noInvalidPositionAtImportRule
- correctness/noUnknownFunction
- correctness/noUnknownMediaFeatureName
- correctness/noUnknownProperty
- correctness/noUnknownUnit
- correctness/noUnmatchableAnbSelector
- suspicious/noDuplicateAtImportRules
- suspicious/noDuplicateFontNames
- suspicious/noDuplicateSelectorsKeyframeBlock
- suspicious/noEmptyBlock
- suspicious/noImportantInKeyframe
- suspicious/noShorthandPropertyOverrides

The following JavaScript rules are promoted:

- a11y/noLabelWithoutControl
- a11y/useFocusableInteractive
- a11y/useSemanticElements
- complexity/noUselessStringConcat
- complexity/noUselessUndefinedInitialization
- complexity/useDateNow
- correctness/noUndeclaredDependencies
- correctness/noInvalidBuiltinInstantiation
- correctness/noUnusedFunctionParameters
- correctness/useImportExtensions
- performance/useTopLevelRegex
- style/noDoneCallback
- style/noYodaExpression
- style/useConsistentBuiltinInstantiation
- style/useDefaultSwitchClause
- style/useExplicitLengthCheck
- style/useThrowNewError
- style/useThrowOnlyError
- suspicious/noConsole
- suspicious/noEvolvingTypes
- suspicious/noMisplacedAssertion
- suspicious/noReactSpecificProps
- suspicious/useErrorMessage
- suspicious/useNumberToFixedDigitsArgument

#### Deprecated rules

Section titled “Deprecated rules”`correctness/noInvalidNewBuiltin`

is deprecated. Use correctness/noInvalidBuiltinInstantiation instead.`style/useSingleCaseStatement`

is deprecated. Use correctness/noSwitchDeclarations instead.`suspicious/noConsoleLog`

is deprecated. Use suspicious/noConsole instead.

#### New features

Section titled “New features”-
Implement css suppression action. Contributed by @togami2864

-
Add support for GraphQL linting. Contributed by @ematipico

-
Add nursery/noCommonJs. Contributed by @minht11

-
Add nursery/noDuplicateCustomProperties. Contributed by @chansuke

-
Add nursery/noEnum. Contributed by @nickfla1

-
Add nursery/noDynamicNamespaceImportAccess. Contributed by @minht11

-
Add nursery/noIrregularWhitespace. Contributed by @michellocana

-
Add nursery/noRestrictedTypes. Contributed by @minht11

-
Add nursery/noSecrets. Contributed by @SaadBazaz

-
Add nursery/noUselessEscapeInRegex. Contributed by @Conaclos

-
Add nursery/noValueAtRule. Contributed by @rishabh3112

-
Add nursery/useAriaPropsSupportedByRole. Contributed by @ryo-ebata

-
Add nursery/useConsistentMemberAccessibility. Contributed by @seitarof

-
Add nursery/useStrictMode. Contributed by @ematipico

-
Add nursery/useTrimStartEnd. Contributed by @chansuke

-
Add nursery/noIrregularWhitespace. Contributed by @DerTimonius

#### Enhancements

Section titled “Enhancements”-
Rename

`nursery/noUnknownSelectorPseudoElement`

to`nursery/noUnknownPseudoElement`

. Contributed by @togami2864 -
The CSS linter is now enabled by default. Which means that you don’t need to opt-in anymore using the configuration file

`biome.json`

:Contributed by @ematipico

-
The JavaScript linter recognizes TypeScript 5.5 and 5.6 globals. Contributed by @Conaclos

-
noBlankTarget now supports an array of allowed domains.

The following configuration allows

`example.com`

and`example.org`

as blank targets.Contributed by @Jayllyz

-
noConsole now accepts an option that specifies some allowed calls on

`console`

. Contributed by @Conaclos -
Add an

`ignoreNull`

option for noDoubleEquals.By default the rule allows loose comparisons against

`null`

. The option`ignoreNull`

can be set to`false`

for reporting loose comparison against`null`

.Contributed by @peaBerberian.

-
noDuplicateObjectKeys now works for JSON and JSONC files. Contributed by @ematipico

-
noInvalidUseBeforeDeclaration now reports direct use of an enum member before its declaration.

In the following code,

`A`

is reported as use before its declaration.Contributed by @Conaclos

-
noNodejsModules now ignores imports of a package which has the same name as a Node.js module. Contributed by @Conaclos

-
noNodejsModules now ignores type-only imports (#1674).

The rule no longer reports type-only imports such as:

Contributed by @Conaclos

-
noRedundantUseStrict no longer reports

`"use strict"`

directives when the`package.json`

marks explicitly the file as a script using the field`"type": "commonjs"`

. Contributed by @ematipico -
noStaticOnlyClass no longer reports a class that extends another class (#3612). Contributed by @errmayank

-
noUndeclaredVariables no longer reports a direct reference to an enum member (#2974).

In the following code, the

`A`

reference is no longer reported as an undeclared variable.Contributed by @Conaclos

-
noUndeclaredVariables recognized Svelte 5 runes in Svelte components and svelte files.

Svelte 5 introduced runes. The rule now recognizes Svelte 5 runes in files ending with the

`.svelte`

,`.svelte.js`

or`.svelte.ts`

extensions.Contributed by @Conaclos

-
noUnusedVariables now checks TypeScript declaration files.

This allows to report a type that is unused because it isn’t exported. Global declarations files (declarations files without exports and imports) are still ignored.

Contributed by @Conaclos

-
useFilenamingConvention now supports unicase letters.

unicase letters have a single case: they are neither uppercase nor lowercase. Biome now accepts filenames in unicase. For example, the filename

`안녕하세요`

is now accepted.We still reject a name that mixes unicase characters with lowercase or uppercase characters. For example, the filename

`A안녕하세요`

is rejected.This change also fixes #3353. Filenames consisting only of numbers are now accepted.

Contributed by @Conaclos

-
useFilenamingConvention now supports Next.js/Nuxt/Astro dynamic routes (#3465).

Next.js, SolidStart, Nuxt, and Astro support dynamic routes such as

`[...slug].js`

and`[[...slug]].js`

.Biome now recognizes this syntax.

`slug`

must contain only alphanumeric characters.Contributed by @Conaclos

-
useExportType no longer reports empty

`export`

(#3535).An empty

`export {}`

allows you to force TypeScript to consider a file with no imports and exports as an EcmaScript module. While`export type {}`

is valid, it is more common to use`export {}`

. Users may find it confusing that the linter asks them to convert it to`export type {}`

. Also, a bundler should be able to remove`export {}`

as well as`export type {}`

. So it is not so useful to report`export {}`

.Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
noControlCharactersInRegex now corretcly handle

`\u`

escapes in unicode-aware regexes.Previously, the rule didn’t consider regex with the

`v`

flags as unicode-aware regexes. Moreover,`\uhhhh`

was not handled in unicode-aware regexes.Contributed by @Conaclos

-
noControlCharactersInRegex now reports control characters and escape sequence of control characters in string regexes. Contributed by @Conaclos

-
`noExcessiveNestedTestSuites`

: fix an edge case where the rule would alert on heavily nested zod schemas. Contributed by @dyc3 -
`noExtraNonNullAssertion`

no longer reports a single non-null assertion enclosed in parentheses (#3352). Contributed by @Conaclos -
noMultipleSpacesInRegularExpressionLiterals now correctly provides a code fix when Unicode characters are used. Contributed by @Conaclos

-
noRedeclare no longer report redeclartions for lexically scoped function declarations #3664.

In JavaScript strict mode, function declarations are lexically scoped: they cannot be accessed outside the block where they are declared.

In non-strict mode, function declarations are hoisted to the top of the enclosing function or global scope.

Previously Biome always hoisted function declarations. It now takes into account whether the code is in strict or non strict mode.

Contributed by @Conaclos

-
noUndeclaredDependencies now ignores self package imports.

Given teh following

`package.json`

:The following import is no longer reported by the rule:

Contributed by @Conaclos

-
Fix [#3149] crashes that occurred when applying the

`noUselessFragments`

unsafe fixes in certain scenarios. Contributed by @unvalley -
noRedeclare no longer reports a variable named as the function expression where it is declared. Contributed by @Conaclos

-
`useAdjacentOverloadSignatures`

no longer reports a`#private`

class member and a public class member that share the same name (#3309).The following code is no longer reported:

Contributed by @Conaclos

-
useAltText n olonger requests alt text for elements hidden from assistive technologies (#3316). Contributed by @robintown

-
useNamingConvention now accepts applying custom convention on abstract classes. Contributed by @Conaclos

-
useNamingConvention no longer suggests an empty fix when a name doesn’t match strict Pascal case (#3561).

Previously the following code led

`useNamingConvention`

to suggest an empty fix. The rule no longer provides a fix for this case.Contributed by @Conaclos

-
useNamingConvention no longer provides fixes for global TypeScript declaration files.

Global TypeScript declaration files have no epxorts and no imports. All the declared types are available in all files of the project. Thus, it is not safe to propose renaming only in the declaration file.

Contributed by @Conaclos

-
useSortedClasses lint error with Template literals (#3394). Contributed by @hangaoke1

-
useValidAriaValues now correctly check property types (3748).

Properties that expect a string now accept arbitrary text. An identifiers can now be made up of any characters except ASCII whitespace. An identifier list can now be separated by any ASCII whitespace.

Contributed by @Conaclos

### Parser

Section titled “Parser”#### Enhancements

Section titled “Enhancements”-
The JSON parser now allows comments in

`turbo.json`

and`jest.config.json`

. Contributed by @Netail and @Conaclos -
The JSON parser now allows comments in files with the

`.json`

extension under the`.vscode`

and`.zed`

directories.Biome recognizes are well known JSON files that allows comments and/or trailing commas. Previously, Biome did not recognize JSON files under the

`.vscode`

and the`.zed`

directories as JSON files that allow comments. You had to configure Biome to recognize them:This override is no longer needed! Note that JSON files under the

`.vscode`

and the`.zed`

directories don’t accept trailing commas.Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
The CSS parser now accepts emoji in identifiers (3627).

The following code is now correctly parsed:

Contributed by @Conaclos

-
Fix #3287 nested selectors with pseudo-classes. Contributed by @denbezrukov

-
Fix #3349 allow CSS multiple ampersand support. Contributed by @denbezrukov

-
Fix #3410 by correctly parsing break statements containing keywords.

Contributed by @ah-yu

-
Fix #3464 by enabling JSX in

`.vue`

files that use the`lang='jsx'`

or`lang='tsx'`

attribute. Contributed by @ematipico

## v1.8.3 (2024-06-27)

Section titled “v1.8.3 (2024-06-27)”#### Bug fixes

Section titled “Bug fixes”-
Fix #3104 by suppressing node warnings when using

`biome migrate`

. Contributed by @SuperchupuDev -
Force colors to be off when using the GitHub reporter to properly create annotations in GitHub actions (#3148). Contributed by @Sec-ant

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”- Implement CSS unicode range. Contributed by @denbezrukov

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #3184 CSS formatter converts custom identifiers to lowercase. Contributed by @denbezrukov
- Fix #3256 constant crashes when editing css files #3256. Contributed by @denbezrukov

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add
`nursery/useDeprecatedReason`

rule. Contributed by @vohoanglong0107. - Add nursery/noExportedImports. Contributed by @Conaclos

#### Enhancements

Section titled “Enhancements”- Implement suggestedExtensions option for
`useImportExtensions`

rule. Contributed by @drdaemos

#### Bug fixes

Section titled “Bug fixes”`useConsistentArrayType`

and`useShorthandArrayType`

now ignore`Array`

in the`extends`

and`implements`

clauses. Fix #3247. Contributed by @Conaclos- Fixes #3066 by taking into account the dependencies declared in the
`package.json`

. Contributed by @ematipico - The code action of the
`useArrowFunction`

rule now preserves a trailing comma when there is only a single type parameter in the arrow function and JSX is enabled. Fixes #3292. Contributed by @Sec-ant

#### Enhancements

Section titled “Enhancements”-
Enhance tailwind sorting lint rule #1274 with variant support.

Every preconfigured variant is assigned a

`weight`

that concurs on establishing the output sorting order. Since nesting variants on the same utility class is possible, the resulting`weight`

is the Bitwise XOR of all the variants weight for that class. Dynamic variants (e.g.`has-[.custom-class]`

,`group-[:checked]`

) are also supported and they take the`weight`

of their base variant name the custom value attached (e.g.`has-[.custom-class]`

takes`has`

weight). Arbitrary variants (e.g.`[&nth-child(2)]`

) don’t have a weight assigned and they are placed after every known variant. Classes with the same amount of arbitrary variants follow lexicographical order. The class that has the highest number of nested arbitrary variants is placed last. Screen variants (e.g.`sm:`

,`max-md:`

,`min-lg:`

) are not supported yet.Contributed by @lutaok

## v1.8.2 (2024-06-20)

Section titled “v1.8.2 (2024-06-20)”#### Bug fixes

Section titled “Bug fixes”- Fix #3201 by correctly injecting the source code of the file when printing the diagnostics. Contributed by @ematipico
- Fix #3179 where comma separators are not correctly removed after running
`biome migrate`

and thus choke the parser. Contributed by @Sec-ant - Fix #3232 by correctly using the colors set by the user. Contributed by @ematipico

#### Enhancement

Section titled “Enhancement”-
Reword the reporter message

`No fixes needed`

to`No fixes applied`

.The former message is misleading when there’re still errors or warnings in the files that should be taken care of manually. For example:

The new message suits better in these cases.

Contributed by @Sec-ant

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”-
Don’t conceal previous overrides (#3176).

Previously, each override inherited the unset configuration of the base configuration. This means that setting a configuration in an override can be concealed by a subsequent override that inherits of the value from the base configuration.

For example, in the next example,

`noDebugger`

was disabled for the`index.js`

file.The rule is now correctly enabled for the

`index.js`

file.Contributed by @Conaclos

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #3103 by correctly resolving CSS formatter options. Contributed by @ah-yu
- Fix #3192 don’t add an extra whitespace within :has. Contributed by @denbezrukov

### JavaScript APIs

Section titled “JavaScript APIs”#### Bug fixes

Section titled “Bug fixes”- Fix a regression introduced by the release of
`v1.8.0`

### Linter

Section titled “Linter”#### New features

Section titled “New features”-
Add nursery/noSubstr. Contributed by @chansuke

-
Add nursery/useConsistentCurlyBraces. Contributed by @dyc3

-
Add nursery/useValidAutocomplete. Contributed by @unvalley

#### Enhancements

Section titled “Enhancements”- Add a code action for noUselessCatch. Contributed by @chansuke

#### Bug fixes

Section titled “Bug fixes”-
Add nursery/noShorthandPropertyOverrides. #2958 Contributed by @neokidev

-
Fix [#3084] false positive by correctly recognize parenthesized return statement. Contributed by @unvalley

-
useImportExtensions now suggests a correct fix for

`import '.'`

and`import './.'`

. Contributed by @minht11 -
Fix useDateNow false positive when new Date object has arguments

`new Date(0).getTime()`

. Contributed by @minht11. -
The

`noUnmatchableAnbSelector`

rule is now able to catch unmatchable`an+b`

selectors like`0n+0`

or`-0n+0`

. Contributed by @Sec-ant. -
The

`useHookAtTopLevel`

rule now recognizes properties named as hooks like`foo.useFoo()`

. Contributed by @ksnyder9801 -
Fix #3092, prevent warning for

`Custom properties (--*)`

. Contributed by @chansuke -
Fix a false positive in the

`useLiteralKeys`

rule. (#3160)This rule now ignores the following kind of computed member name:

Contributed by @Sec-ant

-
The noUnknownProperty rule now ignores the

`composes`

property often used in css modules. #3000 Contributed by @chansuke -
Fix false positives of the useExhaustiveDependencies rule.

The component itself is considered stable when it is used recursively inside a hook closure defined inside of it:

Also,

`export default function`

and`export default class`

are considered stable now because they can only appear at the top level of a module.Contributed by @Sec-ant

-
Fix missing

`withDefaults`

macro in vue files for globals variables. Contributed by @Shyam-Chen

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”- Fix CSS modules settings mapping. Contributed by @denbezrukov

## v1.8.1 (2024-06-10)

Section titled “v1.8.1 (2024-06-10)”#### Bug fixes

Section titled “Bug fixes”- Fix #3069, prevent overwriting paths when using
`--staged`

or`--changed`

options. Contributed by @unvalley - Fix a case where the file link inside a diagnostic wasn’t correctly displayed inside a terminal run by VSCode. Contributed by @uncenter

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”- Fix #3067, by assigning the correct default value to
`indentWidth`

. Contributed by @ematipico

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix the bug where whitespace after the & character in CSS nesting was incorrectly trimmed, ensuring proper targeting of child classes #3061. Contributed by @denbezrukov
- Fix #3068 where the CSS formatter was inadvertently converting variable declarations and function calls to lowercase. Contributed by @denbezrukov
- Fix the formatting of CSS grid layout properties. Contributed by @denbezrukov

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add noUnknownPseudoClass. Contributed by @tunamaguro

#### Bug fixes

Section titled “Bug fixes”-
The

`noEmptyBlock`

css lint rule now treats empty blocks containing comments as valid ones. Contributed by @Sec-ant -
useLiteralKeys no longer reports quoted member names (#3085).

Previously useLiteralKeys reported quoted member names that can be unquoted. For example, the rule suggested the following fix:

This conflicted with the option quoteProperties of our formatter.

The rule now ignores quoted member names.

Contributed by @Conaclos

-
noEmptyInterface now ignores empty interfaces in ambient modules (#3110). Contributed by @Conaclos

-
noUnusedVariables and noUnusedFunctionParameters no longer report the parameters of a constructor type (#3135).

Previously,

`arg`

was reported as unused in a constructor type like:Contributed by @Conaclos

-
noStringCaseMismatch now ignores escape sequences (#3134).

The following code is no longer reported by the rule:

Contributed by @Conaclos

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”- Implemented CSS Unknown At-Rule parsing, allowing the parser to gracefully handle unsupported or unrecognized CSS at-rules. Contributed by @denbezrukov
- Fix #3055 CSS: Layout using named grid lines is now correctly parsed. Contributed by @denbezrukov
- Fix #3091. Allows the parser to handle nested style rules and at-rules properly, enhancing the parser’s compatibility with the CSS Nesting Module. Contributed by @denbezrukov

## 1.8.0 (2024-06-04)

Section titled “1.8.0 (2024-06-04)”### Analyzer

Section titled “Analyzer”#### New features

Section titled “New features”- Allow suppression comments to suppress individual instances of rules. This is used for the lint rule
`useExhaustiveDependencies`

, which is now able to suppress specific dependencies. Fixes #2509. Contributed by @arendjr

#### Enhancements

Section titled “Enhancements”- Assume
`Astro`

object is always a global when processing`.astro`

files. Contributed by @minht11 - Assume Vue compiler macros are globals when processing
`.vue`

files. (#2771) Contributed by @dyc3

#### New features

Section titled “New features”-
New

`clean`

command. Use this new command to clean after the`biome-logs`

directory, and remove all the log files. -
Add two new options

`--only`

and`--skip`

to the command`biome lint`

(#58).The

`--only`

option allows you to run a given rule or rule group, For example, the following command runs only the`style/useNamingConvention`

and`style/noInferrableTypes`

rules. If the rule is disabled in the configuration, then its severity level is set to`error`

for a recommended rule or`warn`

otherwise.Passing a group does not change the severity level of the rules in the group. All the disabled rules in the group will remain disabled. To ensure that the group is run, the

`recommended`

field of the group is enabled. The`nursery`

group cannot be passed, as no rules are enabled by default in the nursery group.The

`--skip`

option allows you to skip the execution of a given group or a given rule. For example, the following command skips the`style`

group and the`suspicious/noExplicitAny`

rule.You can also use

`--only`

and`--skip`

together.`--skip`

overrides`--only`

. The following command executes only the rules from the`style`

group, but the`style/useNamingConvention`

rule.These options are compatible with other options such as

`--write`

(previously`--apply`

), and`--reporter`

.Contributed by @Conaclos

-
Add new command

`biome clean`

. Use this command to purge all the logs emitted by the Biome daemon. This command is really useful, because the Biome daemon tends log many files and contents during its lifecycle. This means that if your editor is open for hours (or even days), the`biome-logs`

folder could become quite heavy. Contributed by @ematipico -
Add support for formatting and linting CSS files from the CLI. These operations are

**opt-in**for the time being.If you don’t have a configuration file, you can enable these features with

`--css-formatter-enabled`

and`--css-linter-enabled`

:Contributed by @ematipico

-
Add new CLI options to control the CSS formatting. Check the CLI reference page for more details. Contributed by @ematipico

-
Add new options

`--write`

,`--fix`

(alias of`--write`

) and`--unsafe`

to the command`biome lint`

and`biome check`

. Add a new option`--fix`

(alias of`--write`

) to the command`biome format`

and`biome migrate`

.The

`biome <lint|check> --<write|fix>`

has the same behavior as`biome <lint|check> --apply`

. The`biome <lint|check> --<write|fix> --unsafe`

has the same behavior as`biome <lint|check> --apply-unsafe`

. The`biome format --fix`

has the same behavior as`biome format --write`

. The`biome migrate --fix`

has the same behavior as`biome migrate --write`

.This change allows these commands to write modifications in the same options. With this change, the

`--apply`

and`--apply-unsafe`

options are deprecated.Contributed by @unvalley

#### Enhancements

Section titled “Enhancements”-
Biome now executes commands (lint, format, check and ci) on the working directory by default. #2266 Contributed by @unvalley

-
`biome migrate eslint`

now tries to convert ESLint ignore patterns into Biome ignore patterns.ESLint uses gitignore patterns. Biome now tries to convert these patterns into Biome ignore patterns.

For example, the gitignore pattern

`/src`

is a relative path to the file in which it appears. Biome now recognizes this and translates this pattern to`./src`

.Contributed by @Conaclos

-
`biome migrate eslint`

now supports the`eslintIgnore`

field in`package.json`

.ESLint allows the use of

`package.json`

as an ESLint configuration file. ESLint supports two fields:`eslintConfig`

and`eslintIgnore`

. Biome only supported the former. It now supports both.Contributed by @Conaclos

-
`biome migrate eslint`

now propagates NodeJS errors to the user.This will help users to identify why Biome is unable to load some ESLint configurations.

Contributed by @Conaclos

-
Add a new

`--reporter`

called`summary`

. This reporter will print diagnostics in a different way, based on the tools (formatter, linter, etc.) that are executed. Import sorting and formatter shows the name of the files that require formatting. Instead, the linter will group the number of rules triggered and the number of errors/warnings:Contributed by @ematipico

-
`biome ci`

now enforces printing the output using colours. If you were previously using`--colors=force`

, you can remove it because it’s automatically set. Contributed by @ematipico -
Add a new

`--reporter`

called`github`

. This reporter will print diagnostics using GitHub workflow commands:Contributed by @ematipico

-
Add a new

`--reporter`

called`junit`

. This reporter will print diagnostics using GitHub workflow commands:Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”- Fix #3024, where running
`biome init`

would create`biome.json`

even if`biome.jsonc`

already exists. Contributed by @minht11

### Configuration

Section titled “Configuration”#### New features

Section titled “New features”-
Add an rule option

`fix`

to override the code fix kind of a rule (#2882).A rule can provide a safe or an

**unsafe**code**action**. You can now tune the kind of code actions thanks to the`fix`

option. This rule option takes a value among:`none`

: the rule no longer emits code actions.`safe`

: the rule emits safe code action.`unsafe`

: the rule emits unsafe code action.

The following configuration disables the code actions of

`noUnusedVariables`

, makes the emitted code actions of`style/useConst`

and`style/useTemplate`

unsafe and safe respectively.Contributed by @Conaclos

-
Add option

`javascript.linter.enabled`

to control the linter for JavaScript (and its super languages) files. Contributed by @ematipico -
Add option

`json.linter.enabled`

to control the linter for JSON (and its super languages) files. Contributed by @ematipico -
Add option

`css.linter.enabled`

to control the linter for CSS (and its super languages) files. Contributed by @ematipico -
Add option

`css.formatter`

, to control the formatter options for CSS (and its super languages) files. Contributed by @ematipico -
You can now change the severity of lint rules down to

`"info"`

. The`"info"`

severity doesn’t emit error codes, and it isn’t affected by other options like`--error-on-warnings`

:Contributed by @ematipico

#### Enhancements

Section titled “Enhancements”- The
`javascript.formatter.trailingComma`

option is deprecated and renamed to`javascript.formatter.trailingCommas`

. The corresponding CLI option`--trailing-comma`

is also deprecated and renamed to`--trailing-commas`

. Details can be checked in #2492. Contributed by @Sec-ant

#### Bug fixes

Section titled “Bug fixes”- Fix a bug where if the formatter was disabled at the language level, it could be erroneously enabled by an override that did not specify the formatter section #2924. Contributed by @dyc3
- Fix #2990, now Biome doesn’t add a trailing comma when formatting
`biome.json`

. Contributed by @dyc3

### Editors

Section titled “Editors”#### New features

Section titled “New features”- Add support for LSP Workspaces

#### Enhancements

Section titled “Enhancements”- The LSP doesn’t crash anymore when the configuration file contains errors. If the configuration contains errors, Biome now shows a pop-up to the user, and it will only parse files using the default configuration. Formatting and linting is disabled until the configuration file is fixed. Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”- Fixes #2781, by correctly computing the configuration to apply to a specific file. Contributed by @ematipico

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #2470 by avoid introducing linebreaks in single line string interpolations. Contributed by @ah-yu
- Resolve deadlocks by narrowing the scope of locks. Contributed by @mechairoi
- Fix #2782 by computing the enabled rules by taking the override settings into consideration. Contributed by @ematipico
- Fix [https://github.com/biomejs/biome/issues/2877] by correctly handling line terminators in JSX string. Contributed by @ah-yu

### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”New rules are incubated in the nursery group. Once stable, we promote them to a stable group. The following rules are promoted:

#### New features

Section titled “New features”-
Add nursery/useDateNow. Contributed by @minht11

-
Add nursery/useErrorMessage. Contributed by @minht11

-
Add nursery/useThrowOnlyError. Contributed by @minht11

-
Add nursery/useImportExtensions. Contributed by @minht11

-
useNamingConvention now supports an option to enforce custom conventions (#1900).

For example, you can enforce the use of a prefix for private class members:

Please, find more details in the rule documentation.

Contributed by @Conaclos

-
Add nursery/useNumberToFixedDigitsArgument. Contributed by @minht11

-
Add nursery/useThrowNewError. Contributed by @minht11

-
Add nursery/useTopLevelRegex, which enforces defining regular expressions at the top level of a module. #2148 Contributed by @dyc3.

-
Add nursery/noCssEmptyBlock. #2513 Contributed by @togami2864

-
Add nursery/noDuplicateAtImportRules. #2658 Contributed by @DerTimonius

-
Add nursery/noDuplicateFontNames. #2308 Contributed by @togami2864

-
Add nursery/noDuplicateSelectorsKeyframeBlock. #2534 Contributed by @isnakode

-
Add nursery/noImportantInKeyframe. #2542 Contributed by @isnakode

-
Add nursery/noInvalidPositionAtImportRule. #2717 Contributed by @t-shiratori

-
Add nursery/noUnknownFunction. #2570 Contributed by @neokidev

-
Add nursery/noUnknownMediaFeatureName. #2751 Contributed by @Kazuhiro-Mimaki

-
Add nursery/noUnknownProperty. #2755 Contributed by @chansuke

-
Add nursery/noUnknownPseudoElement. #2655 Contributed by @keita-hino

-
Add nursery/noUnknownUnit. #2535 Contributed by @neokidev

-
Add nursery/noUnmatchableAnbSelector. #2706 Contributed by @togami2864

-
Add nursery/useGenericFontNames. #2573 Contributed by @togami2864

-
Add nursery/noYodaExpression. Contributed by @michellocana

-
Add nursery/noUnusedFunctionParameters Contributed by @printfn

-
Add nursery/UseSemanticElements. Contributed by @fujiyamaorange

#### Enhancements

Section titled “Enhancements”-
Add a code action for noConfusingVoidType and improve the diagnostics.

The rule now suggests using

`undefined`

instead of`void`

in confusing places. The diagnosis is also clearer.Contributed by @Conaclos

-
Improve code action for nursery/noUselessUndefinedInitialization to handle comments.

The rule now places inline comments after the declaration statement, instead of removing them. The code action is now safe to apply.

Contributed by @lutaok

-
Make useExhaustiveDependencies report duplicate dependencies. Contributed by @tunamaguro

-
Rename

`noEvolvingAny`

into`noEvolvingTypes`

(#48). Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
noUndeclaredVariables and noUnusedImports now correctly handle import namespaces (#2796).

Previously, Biome bound unqualified type to import namespaces. Import namespaces can only be used as qualified names in a type (ambient) context.

Contributed by @Conaclos

-
noUndeclaredVariables now correctly handle ambient computed member names (#2975).

A constant can be imported as a type and used in a computed member name of a member signature. Previously, Biome was unable to bind the value imported as a type to the computed member name.

Contributed by @Conaclos

-
noUndeclaredVariables now ignores

`this`

in JSX components (#2636).The rule no longer reports

`this`

as undeclared in following code.Contributed by @printfn and @Conaclos

-
`useJsxKeyInIterable`

now handles more cases involving fragments. See the snippets below. Contributed by @dyc3

`noExcessiveNestedTestSuites`

no longer erroneously alerts on`describe`

calls that are not invoking the global`describe`

function. #2599 Contributed by @dyc3

-
`noEmptyBlockStatements`

no longer reports empty constructors using typescript parameter properties. #3005 Contributed by @dyc3 -
`noEmptyBlockStatements`

no longer reports empty private or protected constructors. Contributed by @dyc3 -
noExportsInTest rule no longer treats files with in-source testing as test files https://github.com/biomejs/biome/issues/2859. Contributed by @ah-yu

-
useSortedClasses now keeps leading and trailing spaces when applying the code action inside template literals:

-
noUndeclaredDependencies is correctly triggered when running

`biome ci`

. Contributed by @ematipico -
noUnusedVariables no longer panics when a certain combination of characters is typed. Contributed by @ematipico

-
noUndeclaredVariables no logger alerts on

`arguments`

object in a function scope. Contributed by @ah-yu

### Parser

Section titled “Parser”#### Enhancements

Section titled “Enhancements”`lang="tsx"`

is now supported in Vue Single File Components. #2765 Contributed by @dyc3

#### Bug fixes

Section titled “Bug fixes”-
The

`const`

modifier for type parameters is now accepted for TypeScript`new`

signatures (#2825).The following code is now correctly parsed:

Contributed by @Conaclos

-
Some invalid TypeScript syntax caused the Biome parser to crash.

The following invalid syntax no longer causes the Biome parser to crash:

Contributed by @Conaclos

## 1.7.3 (2024-05-06)

Section titled “1.7.3 (2024-05-06)”#### Bug fixes

Section titled “Bug fixes”-
The stdin-file-path option now works correctly for Astro/Svelte/Vue files (#2686)

Fix #2225 where lint output become empty for Vue files.

Contributed by @tasshi-me

-
`biome migrate eslint`

now correctly resolve`@scope/eslint-config`

(#2705). Contributed by @Conaclos

### Linter

Section titled “Linter”#### New features

Section titled “New features”-
Add nursery/useExplicitLengthCheck. Contributed by @minht11

-
`useExhaustiveDependencies`

now recognizes (some) dependencies that change on every render (#2374). Contributed by @arendjr

#### Bug fixes

Section titled “Bug fixes”-
noBlankTarget no longer hangs when applying a code fix (#2675).

Previously, the following code made Biome hangs when applying a code fix.

Contributed by @Conaclos

-
noRedeclare no longer panics on conditional type (#2659).

This is a regression introduced by #2394. This regression makes

`noRedeclare`

panics on every conditional types with`infer`

bindings.Contributed by @Conaclos

-
noUnusedLabels and noConfusingLabels now ignore svelte reactive statements (#2571).

The rules now ignore reactive Svelte blocks in Svelte components.

Contributed by @Conaclos

-
useExportType no longer removes leading comments (#2685).

Previously,

`useExportType`

removed leading comments when it factorized the`type`

qualifier. It now provides a code fix that preserves the leading comments:Contributed by @Conaclos

-
useJsxKeyInIterable no longer reports false positive when iterating on non-jsx items (#2590).

The following snippet of code no longer triggers the rule:

Contributed by @dyc3

-
Fix typo by renaming

`useConsistentBuiltinInstatiation`

to`useConsistentBuiltinInstantiation`

Contributed by @minht11 -
Fix the rule

`useSingleCaseStatement`

including`break`

statements when counting the number of statements in a`switch`

statement (#2696)

## 1.7.2 (2024-04-30)

Section titled “1.7.2 (2024-04-30)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”-
Import sorting now ignores side effect imports (#817).

A side effect import consists now in its own group. This ensures that side effect imports are not reordered.

Here is an example of how imports are now sorted:

Contributed by @Conaclos

-
Import sorting now adds spaces where needed (#1665) Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
`biome migrate eslint`

now handles cyclic references.Some plugins and configurations export objects with cyclic references. This causes

`biome migrate eslint`

to fail or ignore them. These edge cases are now handled correctly.Contributed by @Conaclos

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Correctly handle placement of comments inside named import clauses. #2566. Contributed by @ah-yu

### Linter

Section titled “Linter”#### New features

Section titled “New features”-
Add nursery/noReactSpecificProps. Contributed by @marvin-j97

-
Add noUselessUndefinedInitialization. Contributed by @lutaok

-
Add nursery/useArrayLiterals. Contributed by @Kazuhiro-Mimaki

-
Add nursery/useConsistentBuiltinInstatiation. Contributed by @minht11

-
Add nursery/useDefaultSwitchClause. Contributed by @michellocana

#### Bug fixes

Section titled “Bug fixes”-
noDuplicateJsonKeys no longer crashes when a JSON file contains an unterminated string (#2357). Contributed by @Conaclos

-
noRedeclare now reports redeclarations of parameters in a functions body (#2394).

The rule was unable to detect redeclarations of a parameter or a type parameter in the function body. The following two redeclarations are now reported:

Contributed by @Conaclos

-
noRedeclare no longer reports overloads in object types (#2608).

The rule no longer report redeclarations in the following code:

Contributed by @Conaclos

-
noRedeclare now merge default function export declarations and types (#2372).

The following code is no longer reported as a redeclaration:

Contributed by @Conaclos

-
noUndeclaredVariables no longer reports variable-only and type-only exports (#2637). Contributed by @Conaclos

-
noUnusedVariables no longer crash Biome when encountering a malformed conditional type (#1695). Contributed by @Conaclos

-
useConst now ignores a variable that is read before its assignment.

Previously, the rule reported the following example:

It is now correctly ignored.

Contributed by @Conaclos

-
useShorthandFunctionType now suggests correct code fixes when parentheses are required (#2595).

Previously, the rule didn’t add parentheses when they were needed. It now adds parentheses when the function signature is inside an array, a union, or an intersection.

Contributed by @Conaclos

-
useTemplate now correctly escapes strings (#2580).

Previously, the rule didn’t correctly escape characters preceded by an escaped character.

Contributed by @Conaclos

-
noMisplacedAssertion now allow these matchers

`expect.any()`

`expect.anything()`

`expect.closeTo`

`expect.arrayContaining`

`expect.objectContaining`

`expect.stringContaining`

`expect.stringMatching`

`expect.extend`

`expect.addEqualityTesters`

`expect.addSnapshotSerializer`

Contributed by @fujiyamaorange

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”-
The language parsers no longer panic on unterminated strings followed by a newline and a space (#2606, #2410).

The following example is now parsed without making Biome panics:

Contributed by @Conaclos

## 1.7.1 (2024-04-22)

Section titled “1.7.1 (2024-04-22)”### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Fix #2403 by printing the errors in the client console. Contributed by @ematipico

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”-
Add parentheses for the return expression that has leading multiline comments. #2504. Contributed by @ah-yu

-
Correctly format dangling comments of continue statements. #2555. Contributed by @ah-yu

-
Prevent comments from being eaten by the formatter #2578. Now the comments won’t be eaten for the following code:

Contributed by @ah-yu

-
Correctly format nested union type to avoid reformatting issue. #2628. Contributed by @ah-yu

### Linter

Section titled “Linter”#### Bug fixes

Section titled “Bug fixes”- Fix case where
`jsxRuntime`

wasn’t being respected by`useImportType`

rule (#2473).Contributed by @arendjr - Fix #2460, where the rule
`noUselessFragments`

was crashing the linter in some cases. Now cases like these are correctly handled: Contributed by @ematipico - Fix #2366, where
`noDuplicateJsonKeys`

incorrectly computed the kes to highlight. Contributed by @ematipico

#### Enhancements

Section titled “Enhancements”-
The rule

`noMisplacedAssertions`

now considers valid calling`expect`

inside`waitFor`

:Contributed by @ematipico

## 1.7.0 (2024-04-15)

Section titled “1.7.0 (2024-04-15)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”-
Now Biome can detect the script language in Svelte and Vue script blocks more reliably (#2245). Contributed by @Sec-ant

-
`useExhaustiveDependencies`

no longer reports recursive calls as missing dependencies (#2361). Contributed by @arendjr -
`useExhaustiveDependencies`

correctly reports missing dependencies declared using function declarations (#2362). Contributed by @arendjr -
Biome now can handle

`.svelte`

and`.vue`

files with`CRLF`

as the end-of-line sequence. Contributed by @Sec-ant -
`noMisplacedAssertion`

no longer reports method calls by`describe`

,`test`

,`it`

objects (e.g.`test.each([])()`

) (#2443). Contributed by @unvalley. -
Biome now can handle

`.vue`

files with generic components (#2456).Contributed by @Sec-ant

#### Enhancements

Section titled “Enhancements”-
Complete the well-known file lists for JSON-like files. Trailing commas are allowed in

`.jsonc`

files by default. Some well-known files like`tsconfig.json`

and`.babelrc`

don’t use the`.jsonc`

extension but still allow comments and trailing commas. While others, such as`.eslintrc.json`

, only allow comments. Biome is able to identify these files and adjusts the`json.parser.allowTrailingCommas`

option accordingly to ensure they are correctly parsed. Contributed by @Sec-ant -
Fix dedent logic inconsistent with prettier where the indent-style is space and the indent-width is not 2. Contributed by @mdm317

#### New features

Section titled “New features”-
Add a command to migrate from ESLint

`biome migrate eslint`

allows you to migrate an ESLint configuration to Biome. The command supports legacy ESLint configurations and new flat ESLint configurations. Legacy ESLint configurations using the YAML format are not supported.When loading a legacy ESLint configuration, Biome resolves the

`extends`

field. It resolves both shared configurations and plugin presets! To do this, it invokes*Node.js*.Biome relies on the metadata of its rules to determine the equivalent rule of an ESLint rule. A Biome rule is either inspired or roughly identical to an ESLint rules. By default, inspired and nursery rules are excluded from the migration. You can use the CLI flags

`--include-inspired`

and`--include-nursery`

to migrate them as well.Note that this is a best-effort approach. You are not guaranteed to get the same behavior as ESLint.

Given the following ESLint configuration:

`biome migrate eslint --write`

changes the Biome configuration as follows:Also, if the working directory contains

`.eslintignore`

, then Biome migrates the glob patterns. Nested`.eslintignore`

in subdirectories and negated glob patterns are not supported.If you find any issue, please don’t hesitate to report them.

Contributed by @Conaclos

-
Added two new options to customise the emitted output of the CLI:

`--reporter=json`

and`--reporter=json-pretty`

. With`--reporter=json`

, the diagnostics and the summary will be printed in the**terminal**in JSON format. With`--reporter=json-pretty`

, you can print the same information, but formatted using the same options of your configuration.NOTE: the shape of the JSON is considered experimental, and the shape of the JSON might change in the future.

## Example of output when running `biome format` command

```json { "summary": { "changed": 0, "unchanged": 1, "errors": 1, "warnings": 0, "skipped": 0, "suggestedFixesSkipped": 0, "diagnosticsNotPrinted": 0 }, "diagnostics": [ { "category": "format", "severity": "error", "description": "Formatter would have printed the following content:", "message": [ { "elements": [], "content": "Formatter would have printed the following content:" } ], "advices": { "advices": [ { "diff": { "dictionary": " statement();\n", "ops": [ { "diffOp": { "delete": { "range": [0, 2] } } }, { "diffOp": { "equal": { "range": [2, 12] } } }, { "diffOp": { "delete": { "range": [0, 2] } } }, { "diffOp": { "equal": { "range": [12, 13] } } }, { "diffOp": { "delete": { "range": [0, 2] } } }, { "diffOp": { "insert": { "range": [13, 15] } } } ] } } ] }, "verboseAdvices": { "advices": [] }, "location": { "path": { "file": "format.js" }, "span": null, "sourceCode": null }, "tags": [], "source": null } ], "command": "format" } ``` -
Added new

`--staged`

flag to the`check`

,`format`

and`lint`

subcommands.This new option allows users to apply the command

*only*to the files that are staged (the ones that will be committed), which can be very useful to simplify writing git hook scripts such as`pre-commit`

. Contributed by @castarco

#### Enhancements

Section titled “Enhancements”-
Improve support of

`.prettierignore`

when migrating from PrettierNow, Biome translates most of the glob patterns in

`.prettierignore`

to the equivalent Biome ignore pattern. Only negated glob patterns are not supported.Contributed by @Conaclos

-
Support JavaScript configuration files when migrating from Prettier

`biome migrate prettier`

is now able to migrate Prettier configuration files ending with`js`

,`mjs`

, or`cjs`

extensions. To do this, Biome invokes Node.js.Also, embedded Prettier configurations in

`package.json`

are now supported.Contributed by @Conaclos

-
Support

`overrides`

field in Prettier configuration files when migrating from Prettier. Contributed by @Conaclos -
Support passing a file path to the

`--config-path`

flag or the`BIOME_CONFIG_PATH`

environment variable.Now you can pass a

`.json`

/`.jsonc`

file path with any filename to the`--config-path`

flag or the`BIOME_CONFIG_PATH`

environment variable. This will disable the configuration auto-resolution and Biome will try to read the configuration from the said file path (#2265).Contributed by @Sec-ant

#### Bug fixes

Section titled “Bug fixes”-
Biome now tags the diagnostics emitted by

`organizeImports`

and`formatter`

with correct severity levels, so they will be properly filtered by the flag`--diagnostic-level`

(#2288). Contributed by @Sec-ant -
Biome now correctly filters out files that are not present in the current directory when using the

`--changed`

flag #1996. Contributed by @castarco -
Biome now skips traversing

`fifo`

or`socket`

files (#2311). Contributed by @Sec-ant -
Biome now resolves configuration files exported from external libraries in

`extends`

from the working directory (CLI) or project root (LSP). This is the documented behavior and previous resolution behavior is considered as a bug (#2231). Contributed by @Sec-ant

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”-
Now setting group level

`all`

to`false`

can disable recommended rules from that group when top level`recommended`

is`true`

or unset. Contributed by @Sec-ant -
Biome configuration files can correctly extends

`.jsonc`

configuration files now (#2279). Contributed by @Sec-ant -
Fixed the JSON schema for React hooks configuration (#2396). Contributed by @arendjr

#### Enhancements

Section titled “Enhancements”-
Biome now displays the location of a parsing error for its configuration file (#1627).

Previously, when Biome encountered a parsing error in its configuration file, it didn’t indicate the location of the error. It now displays the name of the configuration file and the range where the error occurred.

Contributed by @Conaclos

-
`options`

is no longer required for rules without any options (#2313).Previously, the JSON schema required to set

`options`

to`null`

when an object is used to set the diagnostic level of a rule without any option. However, if`options`

is set to`null`

, Biome emits an error.The schema is now fixed and it no longer requires specifying

`options`

. This makes the following configuration valid:Contributed by @Conaclos

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Biome extension is now able to parse the JSX syntax in files that associated with the
`javascript`

language identifier. This is an ad hoc fix, because in the React world,`.js`

files are allowed to include JSX syntax, and these files are often associated with the`javascript`

language identifier in most of the editors. Plus, some editor extensions will also associate`.jsx`

files with the`javascript`

language identifier. Relative links: discussion, #2085. Contributed by @Sec-ant

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #2291 by correctly handle comment placement for JSX spread attributes and JSX spread children. Contributed by @ah-yu

### JavaScript APIs

Section titled “JavaScript APIs”### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”New rules are incubated in the nursery group. Once stable, we promote them to a stable group. The following rules are promoted:

- complecity/noExcessiveNestedTestSuites
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

#### New features

Section titled “New features”-
Add a new option

`jsxRuntime`

to the`javascript`

configuration. When set to`reactClassic`

, the noUnusedImports and useImportType rules use this information to make exceptions for the React global that is required by the React Classic JSX transform.This is only necessary for React users who haven’t upgraded to the new JSX transform.

Contributed by @Conaclos and @arendjr

-
Implement #2043: The React rule

`useExhaustiveDependencies`

is now also compatible with Preact hooks imported from`preact/hooks`

or`preact/compat`

. Contributed by @arendjr -
Add rule noFlatMapIdentity to disallow unnecessary callback use on

`flatMap`

. Contributed by @isnakode -
Add rule noConstantMathMinMaxClamp, which disallows using

`Math.min`

and`Math.max`

to clamp a value where the result itself is constant. Contributed by @mgomulak

#### Enhancements

Section titled “Enhancements”-
style/useFilenamingConvention now allows prefixing a filename with

`+`

(#2341).This is a convention used by Sveltekit and Vike.

Contributed by @Conaclos

-
style/useNamingConvention now accepts

`PascalCase`

for local and top-level variables.This allows supporting local variables that hold a component or a regular class. The following code is now accepted:

Contributed by @Conaclos

-
complexity/useLiteralKeys no longer report computed properties named

`__proto__`

(#2430).In JavaScript,

`{["__proto__"]: null}`

and`{__proto__: null}`

have not the same semantic. The first code set a regular property to`null`

. The second one set the prototype of the object to`null`

. See the MDN Docs for more details.The rule now ignores computed properties named

`__proto__`

.Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
Lint rules

`useNodejsImportProtocol`

,`useNodeAssertStrict`

,`noRestrictedImports`

,`noNodejsModules`

will no longer check`declare module`

statements anymore. Contributed by @Sec-ant -
style/useNamingConvention now accepts any case for variables from object destructuring (#2332).

The following name is now ignored:

Previously, the rule renamed this variable. This led to a runtime error.

Contributed by @Conaclos

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”- Fixed an issue when Unicode surrogate pairs were encoded in JavaScript strings using an escape sequence (#2384). Contributed by @arendjr

## 1.6.4 (2024-04-03)

Section titled “1.6.4 (2024-04-03)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”- An operator with no spaces around in a binary expression no longer breaks the js analyzer (#2243). Contributed by @Sec-ant

#### Bug fixes

Section titled “Bug fixes”- Fix the printed error count (#2048). Contributed by @Sec-ant

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”- Correctly calculate enabled rules in lint rule groups. Now a specific rule belonging to a group can be enabled even if its group-level preset option
`recommended`

or`all`

is`false`

(#2191). Contributed by @Sec-ant

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Fix the unexpected code deletion and repetition when
`quickfix.biome`

is enabled and some`import`

-related rules are applied (#2222, #688, #1015). Contributed by @Sec-ant

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add nursery/noMisplacedAssertion. COntributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”-
Fix #2211. noChildrenProp should work fine when children pass as a prop in a new line. Contributed by @fireairforce

-
Fix #2248.

`lint/a11y/useButtonType`

should not trigger when button element with spread attribute. Contributed by @fireairforce -
Fix #2216.

`lint/style/useNamingConvention`

should not ignore JSX Component name binding. Contributed by @fireairforce

#### Enhancements

Section titled “Enhancements”- Add support for object property members in the rule
`useSortedClasses`

. Contributed by @ematipico

### Parser

Section titled “Parser”-
The parser doesn’t throw any error when the frontmatter of

`.astro`

files contains an illegal return:Contributed by @ematipico

## 1.6.3 (2024-03-25)

Section titled “1.6.3 (2024-03-25)”#### Bug fixes

Section titled “Bug fixes”-
Fix configuration resolution. Biome is now able to correctly find the

`biome.jsonc`

configuration file when`--config-path`

is explicitly set (#2164). Contributed by @Sec-ant -
JavaScript/TypeScript files of different variants (

`.ts`

,`.js`

,`.tsx`

,`.jsx`

) in a single workspace now have stable formatting behaviors when running the CLI command in paths of different nested levels or in different operating systems (#2080, #2109). Contributed by @Sec-ant

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”- Complete the documentation and overrides support for options
`formatter.lineEnding`

,`[language].formatter.lineEnding`

,`formatter.attributePosition`

and`javascript.formatter.attributePosition`

. Contributed by @Sec-ant

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #2172 by breaking long object destructuring patterns. Contributed by @ah-yu

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add rule noEvolvingTypes to disallow variables from evolving into
`any`

type through reassignments. Contributed by @fujiyamaorange

#### Enhancements

Section titled “Enhancements”- Rename
`noSemicolonInJsx`

to`noSuspiciousSemicolonInJsx`

. Contributed by @fujiyamaorange

#### Bug fixes

Section titled “Bug fixes”- Quickfix action no longer autofixes lint rule errors on save when
`linter`

is disabled (#2161). Contributed by @Sec-ant - Range formatting for Astro/Svelte/Vue doesn’t place code out of place, especially when formatting on paste is enabled. Contributed by @ematipico

## 1.6.2 (2024-03-22)

Section titled “1.6.2 (2024-03-22)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”-
The

`noSuperWithoutExtends`

rule now allows for calling`super()`

in derived class constructors of class expressions (#2108). Contributed by @Sec-ant -
Fix discrepancies on file source detection. Allow module syntax in

`.cts`

files (#2114). Contributed by @Sec-ant

#### Bug fixes

Section titled “Bug fixes”-
Fixes #2131, where folders were incorrectly ignored when running the command

`check`

. Now folders are correctly ignored based on their command. Contributed by @ematipico -
Smoother handling of

`"endOfLine": "auto"`

in prettier migration: falling back to`"lf"`

(#2145). Contributed by @eMerzh

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”- Fix enabled rules calculation. The precedence of individual rules,
`all`

and`recommend`

presets in top-level and group-level configs is now correctly respected. More details can be seen in (#2072) (#2028). Contributed by @Sec-ant

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #1661. Now nested conditionals are aligned with Prettier’s logic, and won’t contain mixed spaces and tabs. Contributed by @ematipico

### JavaScript APIs

Section titled “JavaScript APIs”#### Enhancements

Section titled “Enhancements”- Support applying lint fixes when calling the
`lintContent`

method of the`Biome`

class (#1956). Contributed by @mnahkies

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add nursery/noDuplicateElseIf. COntributed by @mdm317

#### Bug fixes

Section titled “Bug fixes”-
Rule

`noUndeclaredDependencies`

now also validates`peerDependencies`

and`optionalDependencies`

(#2122). Contributed by @Sec-ant -
Rule

`noUndeclaredDependencies`

won’t check`declare module`

statements anymore (#2123). Contributed by @Sec-ant -
Fix #1925. The fix for

`useOptionalChain`

would sometimes suggest an incorrect fix that discarded optional chaining operators on the left-hand side of logical expressions. These are now preserved. Contributed by @arendjr -
Rule

`noUndeclaredVariables`

now also checks for worker globals (#2121). Contributed by @Sec-ant

#### Bug fixes

Section titled “Bug fixes”-
Correctly parse

`.jsonc`

files. Contributed by @Sec-ant -
Correctly resolve external

`extends`

configs. Contributed by @Sec-ant

## 1.6.1 (2024-03-12)

Section titled “1.6.1 (2024-03-12)”#### Bug fixes

Section titled “Bug fixes”- CLI is now able to automatically search and resolve
`biome.jsonc`

(#2008). Contributed by @Sec-ant - Fix a false positive where some files were counted as “fixed” even though they weren’t modified. Contributed by @ematipico

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”`json.formatter.trailingCommas`

option now works in`overrides`

(#2009). Contributed by @Sec-ant

### Linter

Section titled “Linter”#### New features

Section titled “New features”-
Add rule noDoneCallback, this rule checks the function parameter of hooks & tests for use of the done argument, suggesting you return a promise instead. Contributed by @vasucp1207

#### Bug fixes

Section titled “Bug fixes”-
useJsxKeyInIterable now recognizes function bodies wrapped in parentheses (#2011). Contributed by @Sec-ant

-
useShorthandFunctionType now preserves type parameters of generic interfaces when applying fixes (#2015). Contributed by @Sec-ant

-
Code fixes of useImportType and useExportType now handle multiline statements (#2041). Contributed by @Conaclos

-
noRedeclare no longer reports type parameter and parameter with identical names (#1992).

The following code is no longer reported:

Contributed by @Conaclos

-
noRedeclare now reports duplicate type parameters in a same declaration.

The following type parameters are now reported as a redeclaration:

Contributed by @Conaclos

-
noUndeclaredDependencies now recognizes imports of subpath exports.

E.g., the following import statements no longer report errors if

`@mui/material`

and`tailwindcss`

are installed as dependencies:Contributed by @Sec-ant

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”-
JavaScript lexer is now able to lex regular expression literals with escaped non-ascii chars (#1941).

Contributed by @Sec-ant

## 1.6.0 (2024-03-08)

Section titled “1.6.0 (2024-03-08)”### Analyzer

Section titled “Analyzer”#### New features

Section titled “New features”-
Add partial for

`.astro`

files. Biome is able to sort imports inside the frontmatter of the Astro files. Contributed by @ematipico -
Add partial for

`.vue`

files. Biome is able to sort imports inside the script block of Vue files. Contributed by @nhedger -
Add partial for

`.svelte`

files. Biome is able to sort imports inside the script block of Svelte files. Contributed by @ematipico -
The analyzer now

**infers**the correct quote from`javascript.formatter.quoteStyle`

, if set. This means that code fixes suggested by the analyzer will use the same quote of the formatter. Contributed by @ematipico

#### Enhancements

Section titled “Enhancements”-
noUnusedVariables ignores unused rest spread siblings.

The following code is now valid:

Contributed by @ah-yu

-
Fix #1931. Built-in React hooks such as

`useEffect()`

can now be validated by the`useExhaustiveDependendies`

, even when they’re not being imported from the React library. To do so, simply configure them like any other user-provided hooks.Contributed by @arendjr

-
Implemented #1128. User-provided React hooks can now be configured to track stable results. For example:

This will allow the following to be validated:

Contributed by @arendjr

#### Bug fixes

Section titled “Bug fixes”-
Fix #1748. Now for the following case we won’t provide an unsafe fix for the

`noNonNullAssertion`

rule:Contributed by @ah-yu

-
Imports that contain the protocol

`:`

are now sorted after the`npm:`

modules, and before the`URL`

modules. Contributed by @ematipico -
Fix #1081. The

`useAwait`

rule does not report`for await...of`

. Contributed by @unvalley -
Fix #1827 by properly analyzing nested

`try-finally`

statements. Contributed by @ah-yu -
Fix #1924 Use the correct export name to sort in the import clause. Contributed by @ah-yu

-
Fix #1805 fix formatting arrow function which has conditional expression body Contributed by @mdm317

-
Fix #1781 by avoiding the retrieval of the entire static member expression for the reference if the static member expression does not start with the reference. Contributed by @ah-yu

#### New features

Section titled “New features”-
Add a new command

`biome migrate prettier`

. The command will read the file`.prettierrc`

/`prettier.json`

and`.prettierignore`

and map its configuration to Biome’s one. Due to the different nature of`.prettierignore`

globs and Biome’s globs, it’s**highly**advised to make sure that those still work under Biome. -
Now the file name printed in the diagnostics is clickable. If you run the CLI from your editor, you can

`Ctrl`/`⌘`+ Click on the file name, and the editor will open said file. If row and columns are specified e.g.`file.js:32:7`

, the editor will set the cursor right in that position. Contributed by @ematipico -
Add an option

`--linter`

to`biome rage`

. The option needs to check Biome linter configuration. Contributed by @seitarof -
Add an option

`--formatter`

to`biome rage`

. The option needs to check Biome formatter configuration. Contributed by @seitarof -
The CLI now consistently reports the number of files tha were changed, out of the total files that were analysed. Contributed by @ematipico

-
The CLI now consistently shows the number of errors and warnings emitted. Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”-
Don’t process files under an ignored directory.

Previously, Biome processed all files in the traversed hierarchy, even the files under an ignored directory. Now, it completely skips the content of ignored directories.

For now, directories cannot be ignored using

`files.include`

in the configuration file. This is a known limitation that we want to address in a future release.For instance, if you have a project with a folder

`src`

and a folder`test`

, the following configuration doesn’t completely ignore`test`

.Biome will traverse

`test`

, however all files of the directory are correctly ignored. This can result in file system errors, if Biome encounters dangling symbolic links or files with higher permissions.To avoid traversing the

`test`

directory, you should ignore the directory using`ignore`

: -
Fix #1508 by excluding deleted files from being processed. Contributed by @ematipico

-
Fix #1173. Fix the formatting of a single instruction with commented in a control flow body to ensure consistency. Contributed by @mdm317

-
Fix overriding of

`javascript.globals`

. Contributed by @arendjr -
Fix a bug where syntax rules weren’t run when pulling the diagnostics. Now Biome will emit more parsing diagnostics, e.g.

Contributed by @ematipico

-
Fix #1774 by taking into account the option

`--no-errors-on-unmatched`

when running the CLI using`--changed`

. Contributed by @antogyn

#### Enhancements

Section titled “Enhancements”-
Removed a superfluous diagnostic that was printed during the linting/check phase of a file:

Contributed by @ematipico

-
The command

`format`

now emits parsing diagnostics if there are any, and it will terminate with a non-zero exit code. Contributed by @ematipico

### Configuration

Section titled “Configuration”#### New features

Section titled “New features”-
Add the ability to resolve the configuration files defined inside

`extends`

from the`node_modules/`

directory.If you want to resolve a configuration file that matches the specifier

`@org/configs/biome`

, then your`package.json`

file must look this:And the

`biome.json`

file that “imports” said configuration, will look like this:Read the documentation to better understand how it works, expectations and restrictions.

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”-
Fix a regression where ignored files where formatted in the editor. Contributed by @ematipico

-
Fix a bug where syntax rules weren’t run when pulling the diagnostics. Now Biome will emit more parsing diagnostics, e.g.

Contributed by @ematipico

### Formatter

Section titled “Formatter”#### New features

Section titled “New features”-
Biome now allows to format the

`package.json`

file. This is now the default behaviour and users can remove their workarounds. If you rely on other tools to format`package.json`

, you’ll have to ignore it via configuration. Contributed by @pattrickrice -
New formatter option

`attributePosition`

that have similar behavior as Prettier`singleAttributePerLine`

#1706. Contributed by @octoshikari -
Add partial for

`.astro`

files. Biome is able to format the frontmatter of the Astro files. Contributed by @ematipico -
Add partial for

`.vue`

files. Biome is able to format the script block of Vue files. Contributed by @nhedger -
Add partial for

`.svelte`

files. Biome is able to format the script block of Svelte files. Contributed by @ematipico

#### Enhancements

Section titled “Enhancements”-
`composer.json`

,`deno.json`

,`jsconfig.json`

,`package.json`

and`tsconfig.json`

are no longer protected files.This means that you can now format them.

If you want to ignore these files, you can use the files.ignore configuration:

The following files are still protected, and thus ignored:

`composer.lock`

`npm-shrinkwrap.json`

`package-lock.json`

`yarn.lock`

Contributed by @pattrickrice and @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
Fix #1039. Check unicode width instead of number of bytes when checking if regex expression is a simple argument.

This no longer breaks.

Contributed by @kalleep

-
Fix #1218, by correctly preserving empty lines in member chains. Contributed by @ah-yu

-
Fix #1659 and #1662, by correctly taking into account the leading comma inside the formatter options. Contributed by @ematipico

-
Fix #1934. Fix invalid formatting of long arrow function for AsNeeded arrow parens Contributed by @fireairforce

### JavaScript APIs

Section titled “JavaScript APIs”### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”New rules are incubated in the nursery group. Once stable, we promote them to a stable group. The following rules are promoted:

- complexity/noEmptyTypeParameters
- complexity/noUselessLoneBlockStatements
- correctness/noInvalidUseBeforeDeclaration
- correctness/noUnusedImports
- correctness/noUnusedPrivateClassMembers
- security/noGlobalEval
- style/useConsistentArrayType
- style/useExportType
- style/useFilenamingConvention
- style/useForOf
- style/useImportType
- style/useNodejsImportProtocol
- style/useNumberNamespace
- style/useShorthandFunctionType
- suspicious/noEmptyBlockStatements
- suspicious/noGlobalAssign
- suspicious/noMisleadingCharacterClass
- suspicious/noThenProperty
- suspicious/useAwait

Additionally, the following rules are now recommended:

#### Removed rules

Section titled “Removed rules”-
Remove

`nursery/useGroupedTypeImport`

. The rule style/useImportType covers the behavior of this rule.Note that removing a nursery rule is not considered a breaking change according to our semantic versioning.

Contributed by @Conaclos

#### New features

Section titled “New features”-
Add the rule noSkippedTests, to disallow skipped tests:

Contributed by @ematipico

-
Add the rule noFocusedTests, to disallow skipped tests:

Contributed by @ematipico

-
Add rule useSortedClasses, to sort CSS utility classes:

Contributed by @DaniGuardiola

-
Add rule noUndeclaredDependencies, to detect the use of dependencies that aren’t present in the

`package.json`

.The rule ignores imports using a protocol such as

`node:`

,`bun:`

,`jsr:`

,`https:`

.Contributed by @ematipico and @Conaclos

-
Add rule noNamespaceImport, to report namespace imports:

Contributed by @unvalley

-
Add partial support for

`.astro`

files. Biome is able to lint and fix the frontmatter of the Astro files. Contributed by @ematipico -
Add partial support for

`.vue`

files. Biome is able to lint and fix the script block of the Vue files.Contributed by @nhedger

-
Add rule useNodeAssertStrict, which promotes the use of

`node:assert/strict`

over`node:assert`

. Contributed by @ematipico -
Add rule noExportsInTest which disallows

`export`

or`modules.exports`

in files containing test. Contributed by @ah-yu -
Add rule noSemicolonInJsx to detect possible wrong semicolons inside JSX elements.

Contributed by @fujiyamaorange

-
Add rule noBarrelFile, to report the usage of barrel file:

Contributed by @togami2864

-
Add rule noReExportAll that report

`export * from "mod"`

. Contributed by @mdm317 -
Add rule noExcessiveNestedTestSuites. Contributed by @vasucp1207

-
Add rule useJsxKeyInIterable. Contributed by @vohoanglong0107

#### Enhancements

Section titled “Enhancements”-
noUselessFragments now rule not triggered for jsx attributes when the fragment child is simple text.

Also fixes code action when the fragment child is of type

`JsxExpressionChild`

.Contributed by @vasucp1207

-
noUselessTernary now provides unsafe code fixes. Contributed by @vasucp1207

-
noApproximativeNumericConstant now provides unsafe code fixes and handle numbers without leading zero and numbers with digit separators.

The following numbers are now reported as approximated constants.

Contributed by @Conaclos

-
noPrecisionLoss no longer reports number with extra zeros.

The following numbers are now valid.

Contributed by @Conaclos

-
useNamingConvention now supports unicase letters (#1786).

unicase letters have a single case: they are neither uppercase nor lowercase. Previously, Biome reported names in unicase as invalid. It now accepts a name in unicase everywhere.

The following code is now accepted:

We still reject a name that mixes unicase characters with lowercase or uppercase characters: The following names are rejected:

Contributed by @Conaclos

-
useNamingConvention and useFilenamingConvention now provides a new option

`requireAscii`

to require identifiers to be in ASCII.To avoid any breaking change, this option is turned off by default. We intend to turn it on in the next major release of Biome (Biome 2.0).

Set the

`requireAscii`

rule option to`true`

to require identifiers to be in ASCII.Contributed by @Conaclos

-
noUnusedVariables no longer reports unused imports.

We now have a dedicated rule for reporting unused imports: noUnusedImports

Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
Fix missing link in noStaticOnlyClass documentation. Contributed by @yndajas

-
noConfusingVoidType no longer reports valid use of the void type in conditional types (#1812).

The rule no longer reports the following code:

Contributed by @lucasweng

-
noInvalidUseBeforeDeclaration no longer reports valid use of binding patterns (#1648).

The rule no longer reports the following code:

Contributed by @Conaclos

-
noUnusedVariables no longer reports used binding patterns (#1652).

The rule no longer reports

`a`

as unused the following code:Contributed by @Conaclos

-
Fix #1651. noVar now ignores TsGlobalDeclaration. Contributed by @vasucp1207

-
Fix #1640. useEnumInitializers code action now generates valid code when last member has a comment but no comma. Contributed by @kalleep

-
Fix #1653. Handle a shorthand value in

`useForOf`

to avoid the false-positive case. Contributed by @togami2864 -
Fix #1656. useOptionalChain code action now correctly handles logical and chains where methods with the same name are invoked with different arguments:

Contributed by @lucasweng

-
Fix #1704. Convert

`/`

to escaped slash`\/`

to avoid parsing error in the result of autofix. Contributed by @togami2864 -
Fix#1697. Preserve leading trivia in autofix of suppression rules. Contributed by @togami2864

-
Fix #603. Trim trailing whitespace to avoid double insertion. Contributed by @togami2864

-
Fix #1765. Now the rule

`noDelete`

doesn’t trigger when deleting a dataset:Contributed by @ematipico

-
useNamingConvention and useFilenamingConvention now reject identifiers with consecutive delimiters.

The following name is now invalid because it includes two underscores:

Note that we still allow consecutive leading and consecutive trailing underscores.

Contributed by @Conaclos

-
Fix #1932 Allow redeclaration of type parameters in different declarations. Contributed by @keita-hino

-
Fix #1945 Allow constructor with default parameters in

`noUselessConstructor`

-
Fix #1982 Change to iterate over the module item lists and ignore .d.ts files. Contributed by @togami2864

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”-
Fix #1728. Correctly parse the global declaration when the

`{`

token is on the line following the`global`

keyword.Now the following code is correctly parsed:

Contributed by @ah-yu

-
Fix #1730. Correctly parse

`delete`

expressions with operands that are not simple member expressions.Contributed by @printfn

### Website

Section titled “Website”#### Bug fixes

Section titled “Bug fixes”- Fix #1981. Identify TypeScript definition files by their file path within the playground. Contributed by @ah-yu

## 1.5.3 (2024-01-22)

Section titled “1.5.3 (2024-01-22)”#### Bug fixes

Section titled “Bug fixes”-
Fix #1584. Ensure the LSP only registers the formatter once. Contributed by @nhedger

-
Fix #1589. Fix invalid formatting of own line comments when they were at the end of an import/export list. Contributed by @spanishpear

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”-
Override correctly the recommended preset (#1349).

Previously, if unspecified, Biome turned on the recommended preset in overrides. This resulted in reporting diagnostics with a severity level set to

`off`

. This in turn caused Biome to fail.Now Biome won’t switch on the recommended preset in

`overrides`

unless told to do so.Contributed by @Conaclos

-
Don’t format

**ignored**files that are well-known JSONC files when`files.ignoreUnknown`

is enabled (#1607).Previously, Biome always formatted files that are known to be JSONC files (e.g.

`.eslintrc`

) when`files.ignoreUnknown`

was enabled.Contributed by @Conaclos

### Formatter

Section titled “Formatter”#### New features

Section titled “New features”- Add option
`json.formatter.trailingCommas`

, to provide a better control over the trailing comma in JSON/JSONC files. Its default value is`"none"`

.

#### Bug fixes

Section titled “Bug fixes”- Fix #1178, where the line ending option wasn’t correctly applied. Contributed by @ematipico
- Fix #1571. Fix invalid formatting of nested multiline comments. Contributed by @ah-yu

### Linter

Section titled “Linter”#### Bug fixes

Section titled “Bug fixes”Fix #1575. noArrayIndexKey now captures array index value inside template literals and with string concatenation. Contributed by @vasucp1207

-
Linter rules that inspect regexes now handle multibyte characters correctly (#1522).

Previously, noMisleadingCharacterClass, noMultipleSpacesInRegularExpressionLiterals, and noEmptyCharacterClassInRegex made Biome errors on multi-bytes characters. Multibyte characters are now handled correctly.

The following code no longer raises an internal error:

Contributed by @Conaclos

-
useExhaustiveDependencies no longer made Biome errors in code TypeScript import equal declarations (#1194). Contributed by @Conaclos

-
Fix typo in the diagnostic of noNodejsModules. Contributed by @huseeiin

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”-
Accept the

`const`

modifier for type parameter in method type signature (#1624).The following code is now correctly parsed:

Contributed by @magic-akari

-
Correctly parse type arguments in expression(#1184).

The following code is now correctly parsed in typescript:

Contributed by @ah-yu

### Website

Section titled “Website”- Add a page that maps the Biome rule to its source. Contributed by @ematipico

-
Generate Open Graph images based on the linked page. Contributed by @ematipico

-
Fix examples of the git hook page. Contributed by @9renpoto, @lmauromb, and @Conaclos

-
Fix dead and erroneous hyperlinks. Contributed by @Sec-ant and Conaclos

## 1.5.2 (2024-01-15)

Section titled “1.5.2 (2024-01-15)”### Bug fixes

Section titled “Bug fixes”-
Fix #1512 by skipping verbose diagnostics from the count. Contributed by @ematipico

-
Correctly handle cascading

`include`

and`ignore`

.Previously Biome incorrectly included files that were included at tool level and ignored at global level. In the following example,

`file.js`

was formatted when it should have been ignored. Now, Biome correctly ignores the directory`./src/sub/`

.Contributed by @Conaclos

-
Don’t emit verbose warnings when a protected file is ignored.

Some files, such as

`package.json`

and`tsconfig.json`

, are protected. Biome emits a verbose warning when it encounters a protected file.Previously, Biome emitted this verbose warning even if the file was ignored by the configuration. Now, it doesn’t emit verbose warnings for protected files that are ignored.

Contributed by @Conaclos

-
`overrides`

no longer affect which files are ignored. Contributed by @Conaclos -
The file

`biome.json`

can’t be ignored anymore. Contributed by @ematipico -
Fix #1541 where the content of protected files wasn’t returned to

`stdout`

. Contributed by @ematipico -
Don’t handle CSS files, the formatter isn’t ready yet. Contributed by @ematipico

### Configuration

Section titled “Configuration”#### Bug fixes

Section titled “Bug fixes”-
Fix 1440, a case where

`extends`

and`overrides`

weren’t correctly emitting the final configuration. Contributed by @arendjr -
Correctly handle

`include`

when`ignore`

is set (#1468). Contributed by @ConaclosPreviously, Biome ignored

`include`

if`ignore`

was set. Now, Biome check both`include`

and`ignore`

. A file is processed if it is included and not ignored. If`include`

is not set all files are considered included.

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”-
Fix placement of comments before

`*`

token in generator methods with decorators. #1537 Contributed by @ah-yu -
Fix #1406. Ensure comments before the

`async`

keyword are placed before it. Contributed by @ah-yu -
Fix #1172. Fix placement of line comment after function expression parentheses, they are now attached to first statement in body. Contributed by @kalleep

-
Fix #1511 that made the JavaScript formatter crash. Contributed @Conaclos

### Linter

Section titled “Linter”#### Enhancements

Section titled “Enhancements”-
Add an unsafe code fix for

`noConsoleLog`

. Contributed by @vasucp1207 -
useArrowFunction no longer reports function in

`extends`

clauses or in a`new`

expression. Contributed by @ConaclosThese cases require the presence of a prototype.

-
Add dependency variable names on error message when useExhaustiveDependencies rule shows errors. Contributed by @mehm8128

#### Bug fixes

Section titled “Bug fixes”-
The fix of useArrowFunction now adds parentheses around the arrow function in more cases where it is needed (#1524).

A function expression doesn’t need parentheses in most expressions where it can appear. This is not the case with the arrow function. We previously added parentheses when the function appears in a call or member expression. We now add parentheses in binary-like expressions and other cases where they are needed, hopefully covering all cases.

Previously:

Now:

Contributed by @Conaclos

-
Fix #1514. Fix autofix suggestion to avoid the syntax error in

`no_useless_fragments`

. Contributed by @togami2864

## 1.5.1 (2024-01-10)

Section titled “1.5.1 (2024-01-10)”#### Bug fixes

Section titled “Bug fixes”- The diagnostics
`files/missingHandler`

are now shown only when the option`--verbose`

is passed. Contributed by @ematipico - The diagnostics for protected files are now shown only when the option
`--verbose`

is passed. Contributed by @ematipico - Fix #1465, by taking in consideration the workspace folder when matching a pattern. Contributed by @ematipico
- Fix #1465, by correctly process globs that contain file names. Contributed by @ematipico

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”- Fix #1170. Fix placement of comments inside default switch clause. Now all line comments that have a preceding node will keep their position. Contributed by @kalleep

### Linter

Section titled “Linter”#### Bug fixes

Section titled “Bug fixes”Fix #1335. noUselessFragments now ignores code action on component props when the fragment is empty. Contributed by @vasucp1207

-
useConsistentArrayType was accidentally placed in the

`style`

rule group instead of the`nursery`

group. It is now correctly placed under`nursery`

.

Fix #1483. useConsistentArrayType now correctly handles its option. Contributed by @Conaclos

Fix #1502. useArrowFunction now correctly handle functions that return a (comma) sequence expression. Contributed by @Conaclos

Previously the rule made an erroneous suggestion:

Now, the rule wraps any comma sequence between parentheses:

Fix #1473: useHookAtTopLevel now correctly handles React components and hooks that are nested inside other functions. Contributed by @arendjr

## 1.5.0 (2024-01-08)

Section titled “1.5.0 (2024-01-08)”Biome now scores 97% compatibility with Prettier and features more than 180 linter rules.

### Analyzer

Section titled “Analyzer”#### New features

Section titled “New features”-
Biome now shows a diagnostic when it encounters a protected file. Contributed by @ematipico

-
The command

`biome migrate`

now updates the`$schema`

if there’s an outdated version. -
The CLI now takes in consideration the

`.gitignore`

in the home directory of the user, if it exists. Contributed by @ematipico -
The

`biome ci`

command is now able to print GitHub Workflow Commands when there are diagnostics in our code. Contributed by @nikeee This **might ** require setting the proper permissions on your GitHub action: -
The commands

`format`

,`lint`

,`check`

and`ci`

now accept two new arguments:`--changed`

and`--since`

. Use these options with the VCS integration is enabled to process only the files that were changed. Contributed by @simonxabris -
Introduced a new command called

`biome explain`

, which has the capability to display documentation for lint rules. Contributed by @kalleep -
You can use the command

`biome explain`

to print the documentation of lint rules. Contributed by @kalleep -
You can use the command

`biome explain`

to print the directory where daemon logs are stored. Contributed by @ematipico -
Removed the hard coded limit of 200 printable diagnostics. Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”-
Fix #1247, Biome now prints a **warning ** diagnostic if it encounters files that can’t handle. Contributed by @ematipico

You can ignore unknown file types using the

`files.ignoreUnknown`

configuration in`biome.json`

:Or the

`--files-ignore-unknown`

CLI option: -
Fix #709 and #805 by correctly parsing

`.gitignore`

files. Contributed by @ematipico -
Fix #1117 by correctly respecting the matching. Contributed by @ematipico

-
Fix #691 and #1190, by correctly apply the configuration when computing

`overrides`

configuration. Contributed by @ematipico

### Configuration

Section titled “Configuration”#### New features

Section titled “New features”-
Users can specify

*git ignore patterns*inside`ignore`

and`include`

properties, for example it’s possible to**allow list**globs of files using the`!`

character:

### Editors

Section titled “Editors”#### New features

Section titled “New features”-
The LSP registers formatting without the need of using dynamic capabilities from the client.

This brings formatting services to the editors that don’t support or have limited support for dynamic capabilities.

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”-
Fix #1169. Account for escaped strings when computing layout for assignments. Contributed by @kalleep

-
Fix #851. Allow regular function expressions to group and break as call arguments, just like arrow function expressions. #1003 Contributed by @faultyserver

-
Fix #914. Only parenthesize type-casted function expressions as default exports. #1023 Contributed by @faultyserver

-
Fix #1112. Break block bodies in case clauses onto their own lines and preserve trailing fallthrough comments. #1035 Contributed by @faultyserver

-
Fix

`RemoveSoftLinesBuffer`

behavior to also removed conditional expanded content, ensuring no accidental, unused line breaks are included #1032 Contributed by @faultyserver -
Fix #1024. Allow JSX expressions to nestle in arrow chains #1033 Contributed by @faultyserver

-
Fix incorrect breaking on the left side of assignments by always using fluid assignment. #1021 Contributed by @faultyserver

-
Fix breaking strategy for nested object patterns in function parameters #1054 Contributed by @faultyserver

-
Fix over-indention of arrow chain expressions by simplifying the way each chain is grouped #1036, #1136, and #1162 Contributed by @faultyserver.

-
Fix “simple” checks for calls and member expressions to correctly handle array accesses, complex arguments to single-argument function calls, and multiple-argument function calls. #1057 Contributed by @faultyserver

-
Fix text wrapping and empty line handling for JSX Text elements to match Prettier’s behavior. #1075 Contributed by @faultyserver

-
Fix leading comments in concisely-printed arrays to prevent unwanted line breaks. #1135 Contributed by @faultyserver

-
Fix

`best_fitting`

and interned elements preventing expansion propagation from sibling elements. #1141 Contributed by @faultyserver -
Fix heuristic for grouping function parameters when type parameters with constraints are present. #1153. Contributed by @faultyserver.

-
Fix binary-ish and type annotation handling for grouping call arguments in function expressions and call signatures. #1152 and #1160 Contributed by @faultyserver

-
Fix handling of nestled JSDoc comments to preserve behavior for overloads. #1195 Contributed by @faultyserver

-
Fix #1208. Fix extraction of inner types when checking for simple type annotations in call arguments. #1195 Contributed by @faultyserver

-
Fix #1220. Avoid duplicating comments in type unions for mapped, empty object, and empty tuple types. #1240 Contributed by @faultyserver

-
Fix #1356. Ensure

`if_group_fits_on_line`

content is always written in`RemoveSoftLinesBuffer`

s. #1357 Contributed by @faultyserver -
Fix #1171. Correctly format empty statement with comment inside arrow body when used as single argument in call expression. Contributed by @kalleep

-
Fix #1106. Fix invalid formatting of single bindings when Arrow Parentheses is set to “AsNeeded” and the expression breaks over multiple lines. #1449 Contributed by @faultyserver

### JavaScript APIs

Section titled “JavaScript APIs”### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”- a11y/noAriaHiddenOnFocusable
- a11y/useValidAriaRole
- complexity/useRegexLiterals
- suspicious/noImplicitAnyLet
- style/noDefaultExport

#### New features

Section titled “New features”-
Add useExportType that enforces the use of type-only exports for types. Contributed by @Conaclos

-
Add useImportType that enforces the use of type-only imports for types. Contributed by @Conaclos

Also, the rule groups type-only imports:

-
Add useFilenamingConvention, that enforces naming conventions for JavaScript and TypeScript filenames. Contributed by @Conaclos

By default, the rule requires that a filename be in

`camelCase`

,`kebab-case`

,`snake_case`

, or matches the name of an`export`

in the file. The rule provides options to restrict the allowed cases. -
Add useNodejsImportProtocol that enforces the use of the

`node:`

protocol when importing*Node.js*modules. Contributed by @2-NOW, @vasucp1207, and @Conaclos -
Add useNumberNamespace that enforces the use of the

`Number`

properties instead of the global ones. -
Add useShorthandFunctionType that enforces using function types instead of object type with call signatures. Contributed by @emab, @ImBIOS, and @seitarof

-
Add useConsistentArrayType that enforces the use of a consistent syntax for array types. Contributed by @eryue0220

This rule will replace useShorthandArrayType. It provides an option to choose between the shorthand or the generic syntax.

-
Add noEmptyTypeParameters that ensures that any type parameter list has at least one type parameter. Contributed by @togami2864

This will report the following empty type parameter lists:

-
Add noGlobalEval that reports any use of the global

`eval`

. Contributed by @you-5805 -
Add noGlobalAssign that reports assignment to global variables. Contributed by @chansuke

-
Add noMisleadingCharacterClass that disallows characters made with multiple code points in character class. Contributed by @togami2864

-
Add noThenProperty that disallows the use of

`then`

as property name. Adding a`then`

property makes an object*thenable*that can lead to errors with Promises. Contributed by @togami2864 -
Add noUselessTernary that disallows conditional expressions ( ternaries) when simpler alternatives exist.

#### Enhancements

Section titled “Enhancements”-
noEmptyInterface ignores empty interfaces that extend a type. Address #959 and #1157. Contributed by @Conaclos

This allows supporting interface augmentation in external modules as demonstrated in the following example:

-
Preserve more comments in the code fix of useExponentiationOperator. Contributed by @Conaclos

The rule now preserves comments that follow the (optional) trailing comma.

For example, the rule now suggests the following code fix:

-
`<svg>`

element is now considered as a non-interactive HTML element (#1095). Contributed by @chansuke

This affects the following rules: - noAriaHiddenOnFocusable - noInteractiveElementToNoninteractiveRole - noNoninteractiveElementToInteractiveRole - noNoninteractiveTabindex - useAriaActivedescendantWithTabindex

-
noMultipleSpacesInRegularExpressionLiterals has a safe code fix. Contributed by @Conaclos

-
useArrowFunction ignores expressions that use

`new.target`

. Contributed by @Conaclos -
noForEach now reports only calls that use a callback with

`0`

or`1`

parameter. Address #547. Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”Fix #1061. noRedeclare
no longer reports overloads of `export default function`

. Contributed by @Conaclos

The following code is no longer reported:

Fix #651, useExhaustiveDependencies no longer reports out of scope dependencies. Contributed by @kalleep

The following code is no longer reported:

Fix #1191. noUselessElse
now preserve comments of the `else`

clause. Contributed by @Conaclos

For example, the rule suggested the following fix:

Now the rule suggests a fix that preserves the comment of the `else`

clause:

Fix #1383. noConfusingVoidType
now accepts the `void`

type in type parameter lists.

The rule no longer reports the following code:

Fix #728. useSingleVarDeclarator no longer outputs invalid code. Contributed by @Conaclos

Fix #1167. useValidAriaProps
no longer reports `aria-atomic`

as invalid. Contributed by @unvalley

Fix #1192. useTemplate now correctly handles parenthesized expressions and respects type coercions. Contributed by @n-gude

These cases are now properly handled:

Fix #1456. useTemplate now reports expressions with an interpolated template literal and non-string expressions. Contributed by @n-gude

The following code is now reported:

Fix #1436. useArrowFunction now applies a correct fix when a function expression is used in a call expression or a member access. Contributed by @Conaclos

For example, the rule proposed the following fix:

It now proposes a fix that adds the needed parentheses:

Fix #696. useHookAtTopLevel now correctly detects early returns before the calls to the hook.

-
The code fix of noUselessTypeCOnstraint now adds a trailing comma when needed to disambiguate a type parameter list from a JSX element. COntributed by @Conaclos

Fix #578. useExhaustiveDependencies
now correctly recognizes hooks namespaced under the `React`

namespace. Contributed by @XiNiHa

Fix #910. noSvgWithoutTitle
now ignores `<svg>`

element with `aria-hidden="true"`

. COntributed by @vasucp1207

### Parser

Section titled “Parser”#### BREAKING CHANGES

Section titled “BREAKING CHANGES”-
The representation of imports has been simplified. Contributed by @Conaclos

The new representation is closer to the ECMAScript standard. It provides a single way of representing a namespace import such as

`import * as ns from ""`

. It rules out some invalid states that was previously representable. For example, it is no longer possible to represent a combined import with a`type`

qualifier such as`import type D, { N } from ""`

.See #1163 for more details.

#### New features

Section titled “New features”-
Imports and exports with both an

*import attribute*and a`type`

qualifier are now reported as parse errors.

#### Bug fixes

Section titled “Bug fixes”-
Fix #1077 where parenthesized identifiers in conditional expression were being parsed as arrow expressions. Contributed by @kalleep

These cases are now properly parsed:

*JavaScript*:*TypeScript*:*JSX*: -
Allow empty type parameter lists for interfaces and type aliases (#1237). COntributed by @togami2864

*TypeScript*allows interface declarations and type aliases to have empty type parameter lists. Previously Biome didn’t handle this edge case. Now, it correctly parses this syntax:

### Crates

Section titled “Crates”#### BREAKING CHANGES

Section titled “BREAKING CHANGES”- Rename the
`biome_js_unicode_table`

crate to`biome_unicode_table`

(#1302). COntributed by @chansuke

## 1.4.1 (2023-11-30)

Section titled “1.4.1 (2023-11-30)”### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Fix #933. Some files are properly ignored in the LSP too. E.g.
`package.json`

,`tsconfig.json`

, etc. - Fix #1394, by inferring the language extension from the internal saved files. Now newly created files JavaScript correctly show diagnostics.

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”-
Fix some accidental line breaks when printing array expressions within arrow functions and other long lines #917. Contributed by @faultyserver

-
Match Prettier’s breaking strategy for

`ArrowChain`

layouts #934. Contributed by @faultyserver -
Fix double-printing of leading comments in arrow chain expressions #951. Contributed by @faultyserver

### Linter

Section titled “Linter”#### Bug fixes

Section titled “Bug fixes”- Fix #910, where the rule
`noSvgWithoutTitle`

should skip elements that have`aria-hidden`

attributes. Contributed by @vasucp1207

#### New features

Section titled “New features”- Add useForOf rule. The rule recommends a for-of loop when the loop index is only used to read from an array that is being iterated. Contributed by @victor-teles

#### Enhancement

Section titled “Enhancement”-
Address #924 and #920. noUselessElse now ignores

`else`

clauses that follow at least one`if`

statement that doesn’t break early. Contributed by @ConaclosFor example, the following code is no longer reported by the rule:

#### Bug fixes

Section titled “Bug fixes”Fix #918. useSimpleNumberKeys no longer reports false positive on comments. Contributed by @kalleep

-
Fix #953. noRedeclare no longer reports type parameters with the same name in different mapped types as redeclarations. Contributed by @Conaclos

Fix #608. useExhaustiveDependencies no longer reports missing dependencies for React hooks without dependency array. Contributed by @kalleep

### Parser

Section titled “Parser”## 1.4.0 (2023-11-27)

Section titled “1.4.0 (2023-11-27)”-
Remove the CLI options from the

`lsp-proxy`

, as they were never meant to be passed to that command. Contributed by @ematipico -
Add option

`--config-path`

to`lsp-proxy`

and`start`

commands. It’s now possible to tell the Daemon server to load`biome.json`

from a custom path. Contributed by @ematipico -
Add option

`--diagnostic-level`

. It lets users control the level of diagnostics printed by the CLI. Possible values are:`"info"`

,`"warn"`

, and`"hint"`

. Contributed by @simonxabris -
Add option

`--line-feed`

to the`format`

command. Contributed by @SuperchupuDev -
Add option

`--bracket-same-line`

to the`format`

command. Contributed by @faultyserver -
Add option

`--bracket-spacing`

to the`format`

command. Contributed by @faultyserver

#### Bug fixes

Section titled “Bug fixes”- Fix the command
`format`

, now it returns a non-zero exit code when if there pending diffs. Contributed by @ematipico

### Formatter

Section titled “Formatter”#### New features

Section titled “New features”-
Add the configuration

`formatter.lineFeed`

. It allows changing the type of line endings. Contributed by @SuperchupuDev -
Add the configuration

`javascript.formatter.bracketSameLine`

. It allows controlling whether ending`>`

of a multi-line*JSX*element should be on the last attribute line or not. #627. Contributed by @faultyserver -
Add the configuration

`javascript.formatter.bracketSpacing`

. It allows controlling whether spaces are inserted around the brackets of object literals. #627. Contributed by @faultyserver

#### Bug fixes

Section titled “Bug fixes”-
Fix #832, the formatter no longer keeps an unnecessary trailing comma in type parameter lists. Contributed by @Conaclos

-
Fix #301, the formatter should not break before the

`in`

keyword. Contributed by @ematipico

### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”- a11y/noInteractiveElementToNoninteractiveRole
- complexity/noThisInStatic
- complexity/useArrowFunction
- correctness/noEmptyCharacterClassInRegex
- correctness/noInvalidNewBuiltin
- style/noUselessElse
- style/useAsConstAssertion
- style/useShorthandAssign
- suspicious/noApproximativeNumericConstant
- suspicious/noMisleadingInstantiator
- suspicious/noMisrefactoredShorthandAssign

The following rules are now recommended:

The following rules are now deprecated:

- correctness/noNewSymbol The rule is replaced by correctness/noInvalidNewBuiltin

#### New features

Section titled “New features”-
Add noDefaultExport which disallows

`export default`

. Contributed by @Conaclos -
Add noAriaHiddenOnFocusable which reports hidden and focusable elements. Contributed by @vasucp1207

-
Add noImplicitAnyLet that reports variables declared with

`let`

and without initialization and type annotation. Contributed by @TaKO8Ki and @b4s36t4 -
Add useAwait that reports

`async`

functions that don’t use an`await`

expression. -
Add useValidAriaRole. Contributed by @vasucp1207

-
Add useRegexLiterals that suggests turning call to the regex constructor into regex literals. COntributed by @Yuiki

#### Enhancements

Section titled “Enhancements”- Add an unsafe code fix for a11y/useAriaActivedescendantWithTabindex

#### Bug fixes

Section titled “Bug fixes”-
Fix #639 by ignoring unused TypeScript’s mapped key. Contributed by @Conaclos

-
Fix #565 by handling several

`infer`

with the same name in extends clauses of TypeScript’s conditional types. Contributed by @Conaclos

Fix #653. noUnusedImports
now correctly removes the entire line where the unused `import`

is. Contributed by @Conaclos

-
Fix #607

`useExhaustiveDependencies`

, ignore optional chaining, Contributed by @msdlisper -
Fix #676, by using the correct node for the

`"noreferrer"`

when applying the code action. Contributed by @ematipico -
Fix #455. The CLI can now print complex emojis to the console correctly.

Fix #727. noInferrableTypes
now correctly keeps type annotations when the initialization expression is `null`

. Contributed by @Conaclos

Fix #784, noSvgWithoutTitle
fixes false-positives to `aria-label`

and reports svg’s role attribute is implicit. Contributed by @unvalley

-
Fix #834 that made noUselessLoneBlockStatements reports block statements of switch clauses. Contributed by @vasucp1207

-
Fix #783 that made noUselessLoneBlockStatements reports block statements of

`try-catch`

structures. Contributed by @hougesen -
Fix #69 that made correctness/noUnnecessaryContinue incorrectly reports a

`continue`

used to break a switch clause. Contributed by @TaKO8Ki -
Fix #664 by improving the diagnostic of style/useNamingConvention when double capital are detected in strict camel case mode. Contributed by @vasucp1207

-
Fix #643 that erroneously parsed the option of complexity/useExhaustiveDependencies. Contributed by @arendjr

### Parser

Section titled “Parser”#### Bug fixes

Section titled “Bug fixes”- Fix #846 that erroneously parsed
`<const T,>() => {}`

as a JSX tag instead of an arrow function when both TypeScript and JSX are enabled.

### VSCode

Section titled “VSCode”## 1.3.3 (2023-10-31)

Section titled “1.3.3 (2023-10-31)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”- Fix #604 which made noConfusingVoidType report false positives when the
`void`

type is used in a generic type parameter. Contributed by @unvalley

#### Bug fixes

Section titled “Bug fixes”- Fix how
`overrides`

behave. Now`ignore`

and`include`

apply or not the override pattern, so they override each other. Now the options inside`overrides`

override the top-level options. - Bootstrap the logger only when needed. Contributed by @ematipico
- Fix how
`overrides`

are run. The properties`ignore`

and`include`

have different semantics and only apply/not apply an override. Contributed by @ematipico

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Fix #592, by changing binary resolution in the IntelliJ plugin. Contributed by @Joshuabaker2

### Formatter

Section titled “Formatter”#### Bug fixes

Section titled “Bug fixes”-
Apply the correct layout when the right hand of an assignment expression is an

`await`

expression or a yield expression. Contributed by @ematipico -
Fix #303, where nested arrow functions didn’t break. Contributed by @victor-teles

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add noUnusedPrivateClassMembers rule. The rule disallow unused private class members. Contributed by @victor-teles

#### Bug fixes

Section titled “Bug fixes”-
Fix #175 which made noRedeclare report index signatures using the name of a variable in the parent scope.

-
Fix #557 which made noUnusedImports report imported types used in

`typeof`

expression. Contributed by @Conaclos -
Fix #576 by removing some erroneous logic in noSelfAssign. Contributed by @ematipico

-
Fix #861 that made noUnusedVariables always reports the parameter of a non-parenthesize arrow function as unused.

-
Fix #595 by updating unsafe-apply logic to avoid unexpected errors in noUselessFragments. Contributed by @nissy-dev

-
Fix #591 which made noRedeclare report type parameters with identical names but in different method signatures. Contributed by @Conaclos

-
Support more a11y roles and fix some methods for a11y lint rules Contributed @nissy-dev

-
Fix #609

`useExhaustiveDependencies`

, by removing`useContext`

,`useId`

and`useSyncExternalStore`

from the known hooks. Contributed by @msdlisper -
Fix

`useExhaustiveDependencies`

, by removing`useContext`

,`useId`

and`useSyncExternalStore`

from the known hooks. Contributed by @msdlisper -
Fix #871 and #610. Now

`useHookAtTopLevel`

correctly handles nested functions. Contributed by @arendjr -
The options of the rule

`useHookAtTopLevel`

are deprecated and will be removed in Biome 2.0. The rule now determines the hooks using the naming convention set by React.

### Parser

Section titled “Parser”#### Enhancements

Section titled “Enhancements”- Support RegExp v flag. Contributed by @nissy-dev
- Improve error messages. Contributed by @ematipico

## 1.3.1 (2023-10-20)

Section titled “1.3.1 (2023-10-20)”#### Bug fixes

Section titled “Bug fixes”- Fix
`rage`

command, now it doesn’t print info about running servers. Contributed by @ematipico

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Fix #552, where the formatter isn’t correctly triggered in Windows systems. Contributed by @victor-teles

### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add noThisInStatic rule. Contributed by @ditorodev and @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
Fix #548 which made noSelfAssign panic.

-
Fix #555, by correctly map

`globals`

into the workspace.

## 1.3.0 (2023-10-19)

Section titled “1.3.0 (2023-10-19)”### Analyzer

Section titled “Analyzer”#### Enhancements

Section titled “Enhancements”-
Import sorting is safe to apply now, and it will be applied when running

`check --apply`

instead of`check --apply-unsafe`

. -
Import sorting now handles Bun imports

`bun:<name>`

, absolute path imports`/<path>`

, and Node’s subpath imports`#<name>`

. See our documentation for more details. Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”- Fix #319. The command
`biome lint`

now shows the correct options. Contributed by @ematipico - Fix #312. Running
`biome --version`

now exits with status code`0`

instead of`1`

. Contributed by @nhedger - Fix a bug where the
`extends`

functionality doesn’t carry over`organizeImports.ignore`

. Contributed by @ematipico - The CLI now returns the original content when using
`stdin`

and the original content doesn’t change. Contributed by @ematipico

#### New features

Section titled “New features”-
Add support for

`BIOME_BINARY`

environment variable to override the location of the binary. Contributed by @ematipico -
Add option

`--indent-width`

, and deprecated the option`--indent-size`

. Contributed by @ematipico -
Add option

`--javascript-formatter-indent-width`

, and deprecated the option`--javascript-formatter-indent-size`

. Contributed by @ematipico -
Add option

`--json-formatter-indent-width`

, and deprecated the option`--json-formatter-indent-size`

. Contributed by @ematipico -
Add option

`--daemon-logs`

to`biome rage`

. The option is required to view Biome daemon server logs. Contributed by @unvalley -
Add support for logging. By default, Biome doesn’t log anything other than diagnostics. Logging can be enabled with the new option

`--log-level`

:There are four different levels of logging, from the most verbose to the least verbose:

`debug`

,`info`

,`warn`

and`error`

. Here’s how an`INFO`

log will look like:You can customize how the log will look like with a new option

`--log-kind`

. The supported kinds are:`pretty`

,`compact`

and`json`

.`pretty`

is the default logging. Here’s how a`compact`

log will look like:

#### Enhancements

Section titled “Enhancements”- Deprecated the environment variable
`ROME_BINARY`

. Use`BIOME_BINARY`

instead. Contributed by @ematipico - Biome doesn’t check anymore the presence of the
`.git`

folder when VCS support is enabled. Contributed by @ematipico `biome rage`

doesn’t print the logs of the daemon, use`biome rage --daemon-logs`

to print them. Contributed by @unvalley

### Configuration

Section titled “Configuration”#### New features

Section titled “New features”-
Add option

`formatter.indentWidth`

, and deprecated the option`formatter.indentSize`

. Contributed by @ematipico -
Add option

`javascript.formatter.indentWidth`

, and deprecated the option`javascript.formatter.indentSize`

. Contributed by @ematipico -
Add option

`json.formatter.indentWidth`

, and deprecated the option`json.formatter.indentSize`

. Contributed by @ematipico -
Add option

`include`

to multiple sections of the configuration`files.include`

;`formatter.include`

;`linter.include`

;`organizeImports.include`

; When`include`

and`ignore`

are both specified,`ignore`

takes**precedence**over`include`

-
Add option

`overrides`

, where users can modify the behaviour of the tools for certain files or paths.For example, it’s possible to modify the formatter

`lineWidth`

, and even`quoteStyle`

for certain files that are included in glob path`generated/**`

:Or, you can disable certain rules for certain path, and disable the linter for other paths:

### Bug fixes

Section titled “Bug fixes”- Fix #343,
`extends`

was incorrectly applied to the`biome.json`

file. Contributed by @ematipico

### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”-
Fix #404. Biome intellij plugin now works on Windows. Contributed by @victor-teles

-
Fix #402. Biome

`format`

on intellij plugin now recognize biome.json. Contributed by @victor-teles

### Formatter

Section titled “Formatter”#### Enhancements

Section titled “Enhancements”- Use
`OnceCell`

for the Memoized memory because that’s what the`RefCell<Option>`

implemented. Contributed by @denbezrukov

### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”- complexity/noExcessiveCognitiveComplexity
- complexity/noVoid
- correctness/useExhaustiveDependencies
- correctness/useHookAtTopLevel
- performance/noAccumulatingSpread
- style/useCollapsedElseIf
- suspicious/noConfusingVoidType
- suspicious/noFallthroughSwitchClause
- suspicious/noGlobalIsFinite
- suspicious/noGlobalIsNan
- suspicious/useIsArray

The following rules are now recommended:

#### New features

Section titled “New features”-
Add noEmptyCharacterClassInRegex rule. The rule reports empty character classes and empty negated character classes in regular expression literals. Contributed by @Conaclos

-
Add noMisleadingInstantiator rule. The rule reports the misleading use of the

`new`

and`constructor`

methods. Contributed by @unvalley -
Add noUselessElse rule. The rule reports

`else`

clauses that can be omitted because their`if`

branches break. Contributed by @Conaclos -
Add noUnusedImports rule. The rule reports unused imports and suggests removing them. Contributed by @Conaclos

noUnusedVariables reports also unused imports, but don’t suggest their removal. Once noUnusedImports stabilized, noUnusedVariables will not report unused imports.

-
Add useShorthandAssign rule. The rule enforce use of shorthand operators that combine variable assignment and some simple mathematical operations. For example, x = x + 4 can be shortened to x += 4. Contributed by @victor-teles

-
Add useAsConstAssertion rule. The rule enforce use of

`as const`

assertion to infer literal types. Contributed by @unvalley -
Add noMisrefactoredShorthandAssign rule. The rule reports shorthand assigns when variable appears on both sides. For example

`x += x + b`

Contributed by @victor-teles -
Add noApproximativeNumericConstant rule. Contributed by @nikeee

Add noInteractiveElementToNoninteractiveRole rule. The rule enforces the non-interactive ARIA roles are not assigned to interactive HTML elements. Contributed by @nissy-dev

-
Add useAriaActivedescendantWithTabindex rule. The rule enforces that

`tabIndex`

is assigned to non-interactive HTML elements with`aria-activedescendant`

. Contributed by @nissy-dev -
Add noUselessLoneBlockStatements rule. The rule reports standalone blocks that don’t include any lexical scoped declaration. Contributed by @emab

-
Add noInvalidNewBuiltin rule. The rule reports use of

`new`

on`Symbol`

and`BigInt`

. Contributed by @lucasweng

#### Enhancements

Section titled “Enhancements”-
The following rules have now safe code fixes:

-
noAccumulatingSpread makes more check in order to reduce potential false positives. Contributed by @Vivalldi

-
noConstAssign now provides an unsafe code fix that replaces

`const`

with`let`

. Contributed by @vasucp1207 -
noExcessiveComplexity default complexity threshold is now

`15`

. Contributed by @arendjr -
noPositiveTabindexValue now provides an unsafe code fix that set to

`0`

the tab index. Contributed by @vasucp1207 -
noUnusedLabels no longer reports unbreakable labeled statements. Contributed by @Conaclos

-
noUnusedVariables now reports unused TypeScript’s type parameters. Contributed by @Conaclos

-
useAnchorContent now provides an unsafe code fix that removes the `aria-hidden“ attribute. Contributed by @vasucp1207

-
useValidAriaProps now provides an unsafe code fix that removes invalid properties. Contributed by @vasucp1207

-
`noExcessiveComplexity`

was renamed to`noExcessiveCognitiveComplexity`

#### Bug fixes

Section titled “Bug fixes”Fix #294. noConfusingVoidType no longer reports false positives for return types. Contributed by @b4s36t4

Fix #313. noRedundantUseStrict now keeps leading comments.

Fix #383. noMultipleSpacesInRegularExpressionLiterals now provides correct code fixes when consecutive spaces are followed by a quantifier. Contributed by @Conaclos

Fix #397. useNumericLiterals now provides correct code fixes for signed numbers. Contributed by @Conaclos

-
Fix 452. The linter panicked when it met a malformed regex (a regex not ending with a slash).

-
Fix #104. We now correctly handle types and values with the same name.

-
Fix #243 a false positive case where the incorrect scope was defined for the

`infer`

type in rule noUndeclaredVariables. Contributed by @denbezrukov -
Fix #322, now noSelfAssign correctly handles literals inside call expressions.

-
Changed how noSelfAssign behaves. The rule is not triggered anymore on function calls. Contributed by @ematipico

### Parser

Section titled “Parser”-
Enhance diagnostic for infer type handling in the parser. The ‘infer’ keyword can only be utilized within the ’ extends’ clause of a conditional type. Using it outside this context will result in an error. Ensure that any type declarations using ‘infer’ are correctly placed within the conditional type structure to avoid parsing issues. Contributed by @denbezrukov

-
Add support for parsing trailing commas inside JSON files:

Contributed by @nissy-dev

### VSCode

Section titled “VSCode”## 1.2.2 (2023-09-16)

Section titled “1.2.2 (2023-09-16)”#### Bug fixes

Section titled “Bug fixes”- Fix a condition where import sorting wasn’t applied when running
`biome check --apply`

## 1.2.1 (2023-09-15)

Section titled “1.2.1 (2023-09-15)”### Configuration

Section titled “Configuration”- Fix an edge case where the formatter language configuration wasn’t picked.
- Fix the configuration schema, where
`json.formatter`

properties weren’t transformed in camel case.

## 1.2.0 (2023-09-15)

Section titled “1.2.0 (2023-09-15)”#### New features

Section titled “New features”- Add new options to customize the behaviour the formatter based on the language of the file
`--json-formatter-enabled`

`--json-formatter-indent-style`

`--json-formatter-indent-size`

`--json-formatter-line-width`

`--javascript-formatter-enabled`

`--javascript-formatter-indent-style`

`--javascript-formatter-indent-size`

`--javascript-formatter-line-width`

#### Bug fixes

Section titled “Bug fixes”- Fix a bug where
`--errors-on-warning`

didn’t work when running`biome ci`

command.

### Configuration

Section titled “Configuration”#### New features

Section titled “New features”- Add new options to customize the behaviour of the formatter based on the language of the file
`json.formatter.enabled`

`json.formatter.indentStyle`

`json.formatter.indentSize`

`json.formatter.lineWidth`

`javascript.formatter.enabled`

`javascript.formatter.indentStyle`

`javascript.formatter.indentSize`

`javascript.formatter.lineWidth`

### Linter

Section titled “Linter”#### Promoted rules

Section titled “Promoted rules”- a11y/noAriaUnsupportedElements
- a11y/noNoninteractiveTabindex
- a11y/noRedundantRoles
- a11y/useValidAriaValues
- complexity/noBannedTypes
- complexity/noStaticOnlyClass
- complexity/noUselessEmptyExport
- complexity/noUselessThisAlias
- correctness/noConstantCondition
- correctness/noNonoctalDecimalEscape
- correctness/noSelfAssign
- style/useLiteralEnumMembers
- style/useNamingConvention
- suspicious/noControlCharactersInRegex
- suspicious/noUnsafeDeclarationMerging
- suspicious/useGetterReturn

#### New rules

Section titled “New rules”- Add noConfusingVoidType rule. The rule reports the unusual use of the
`void`

type. Contributed by @shulandmimi

#### Removed rules

Section titled “Removed rules”-
Remove

`noConfusingArrow`

Code formatters, such as prettier and Biome, always adds parentheses around the parameter or the body of an arrow function. This makes the rule useless.

Contributed by @Conaclos

#### Enhancements

Section titled “Enhancements”-
noFallthroughSwitchClause now relies on control flow analysis to report most of the switch clause fallthrough. Contributed by @Conaclos

-
noAssignInExpressions no longer suggest code fixes. Most of the time the suggestion didn’t match users’ expectations. Contributed by @Conaclos

-
noUselessConstructor no longer emits safe code fixes. Contributed by @Conaclos

All code fixes are now emitted as unsafe code fixes. Removing a constructor can change the behavior of a program.

-
useCollapsedElseIf now only provides safe code fixes. Contributed by @Conaclos

-
noUnusedVariables now reports more cases.

The rule is now able to ignore self-writes. For example, the rule reports the following unused variable:

The rule is also capable of detecting an unused declaration that uses itself. For example, the rule reports the following unused interface:

Finally, the rule now ignores all

*TypeScript*declaration files, including global declaration files.Contributed by @Conaclos

#### Bug fixes

Section titled “Bug fixes”-
Fix #182, making useLiteralKeys retains optional chaining. Contributed by @denbezrukov

-
Fix #168, fix useExhaustiveDependencies false positive case when stable hook is on a new line. Contributed by @denbezrukov

-
Fix #137, fix noRedeclare false positive case with TypeScript module declaration:

Contributed by @denbezrukov

-
Fix #258, fix noUselessFragments the case where the rule removing an assignment. Contributed by @denbezrukov

-
Fix #266, where

`complexity/useLiteralKeys`

emitted a code action with an invalid AST. Contributed by @ematipico -
Fix #105, removing false positives reported by noUnusedVariables.

The rule no longer reports the following used variable:

Contributed by @Conaclos

### VSCode

Section titled “VSCode”#### Enhancements

Section titled “Enhancements”-
Improve server binary resolution when using certain package managers, notably pnpm.

The new strategy is to point to

`node_modules/.bin/biome`

path, which is consistent for all package managers.

## 1.1.2 (2023-09-07)

Section titled “1.1.2 (2023-09-07)”### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- Fix a case where an empty JSON file would cause the LSP server to crash. Contributed by @ematipico

### Linter

Section titled “Linter”#### Enhancements

Section titled “Enhancements”-
useNamingConvention now accepts import namespaces in

*PascalCase*and rejects export namespaces in*CONSTANT_CASE*.The following code is now valid:

And the following code is now invalid:

Contributed by @Conaclos

-
noUselessConstructor now ignores decorated classes and decorated parameters. The rule now gives suggestions instead of safe fixes when parameters are annotated with types. Contributed by @Conaclos

## 1.1.1 (2023-09-07)

Section titled “1.1.1 (2023-09-07)”### Analyzer

Section titled “Analyzer”#### Bug fixes

Section titled “Bug fixes”- The diagnostic for
`// rome-ignore`

suppression comment should not be a warning. A warning could block the CI, marking a gradual migration difficult. The code action that changes`// rome-ignore`

to`// biome-ignore`

is disabled as consequence. Contributed by @ematipico

## 1.1.0 (2023-09-06)

Section titled “1.1.0 (2023-09-06)”### Analyzer

Section titled “Analyzer”#### Enhancements

Section titled “Enhancements”- Add a code action to replace
`rome-ignore`

with`biome-ignore`

. Use`biome check --apply-unsafe`

to update all the comments. The action is not bulletproof, and it might generate unwanted code, that’s why it’s unsafe action. Contributed by @ematipico

#### Enhancements

Section titled “Enhancements”- Biome now reports a diagnostics when a
`rome.json`

file is found. `biome migrate --write`

creates`biome.json`

from`rome.json`

, but it won’t delete the`rome.json`

file. Contributed by @ematipico

#### Bug fixes

Section titled “Bug fixes”- Biome uses
`biome.json`

first, then it attempts to use`rome.json`

. - Fix a case where Biome couldn’t compute correctly the ignored files when the VSC integration is enabled. Contributed by @ematipico

### Configuration

Section titled “Configuration”### Editors

Section titled “Editors”#### Bug fixes

Section titled “Bug fixes”- The LSP now uses its own socket and won’t rely on Biome’s socket. This fixes some cases where users were seeing multiple servers in the
`rage`

output.

### Formatter

Section titled “Formatter”#### Enhancements

Section titled “Enhancements”- You can use
`// biome-ignore`

as suppression comment. - The
`// rome-ignore`

suppression is deprecated.

### JavaScript APIs

Section titled “JavaScript APIs”### Linter

Section titled “Linter”#### New features

Section titled “New features”- Add useCollapsedElseIf rule. This new rule requires merging an
`else`

and an`if`

, if the`if`

statement is the only statement in the`else`

block. Contributed by @n-gude

#### Enhancements

Section titled “Enhancements”-
useTemplate now reports all string concatenations.

Previously, the rule ignored concatenation of a value and a newline or a backquote. For example, the following concatenation was not reported:

The rule now reports these cases and suggests the following code fixes:

Contributed by @Conaclos

-
useExponentiationOperator suggests better code fixes.

The rule now preserves any comment preceding the exponent, and it preserves any parenthesis around the base or the exponent. It also adds spaces around the exponentiation operator

`**`

, and always adds parentheses for pre- and post-updates.Contributed by @Conaclos

-
You can use

`// biome-ignore`

as suppression comment. -
The

`// rome-ignore`

suppression is deprecated.

#### Bug fixes

Section titled “Bug fixes”-
Fix #80, making noDuplicateJsxProps case-insensitive.

Some frameworks, such as Material UI, rely on the case-sensitivity of JSX properties. For example, TextField has two properties with the same name, but distinct cases:

Contributed by @Conaclos

-
Fix #138

noCommaOperator now correctly ignores all use of comma operators inside the update part of a

`for`

loop. The following code is now correctly ignored:Contributed by @Conaclos

-
Fix rome#4713.

Previously, useTemplate made the following suggestion:

This breaks code where

`a`

and`b`

are numbers.Now, the rule makes the following suggestion:

Contributed by @Conaclos

-
Fix rome#4109

Previously, useTemplate suggested an invalid code fix when a leading or trailing single-line comment was present:

Now, the rule correctly handles this case:

As a sideeffect, the rule also suggests the removal of any inner comments.

Contributed by @Conaclos

-
Fix rome#3850

Previously useExponentiationOperator suggested invalid code in a specific edge case:

Now, the rule properly adds parentheses:

Contributed by @Conaclos

-
Fix #106

noUndeclaredVariables now correctly recognizes some TypeScript types such as

`Uppercase`

.Contributed by @Conaclos

-
Fix rome#4616

Previously noUnreachableSuper reported valid codes with complex nesting of control flow structures.

Contributed by @Conaclos

## 1.0.0 (2023-08-28)

Section titled “1.0.0 (2023-08-28)”### Analyzer

Section titled “Analyzer”#### BREAKING CHANGES

Section titled “BREAKING CHANGES”-
The organize imports feature now groups import statements by “distance”.

Modules “farther” from the user are put on the top, and modules “closer” to the user are placed on the bottom. Check the documentation for more information about it.

-
The organize imports tool is enabled by default. If you don’t want to use it, you need to disable it explicitly:

#### BREAKING CHANGES

Section titled “BREAKING CHANGES”-
The CLI now exists with an error when there’s an error inside the configuration.

Previously, biome would raise warnings and continue the execution by applying its defaults.

This could have been better for users because this could have created false positives in linting or formatted code with a configuration that wasn’t the user’s.

-
The command

`biome check`

now shows formatter diagnostics when checking the code.The diagnostics presence will result in an error code when the command finishes.

This aligns with semantic and behaviour meant for the command

`biome check`

. -
`init`

command emits a`biome.json`

file;

#### Other changes

Section titled “Other changes”-
Fix #4670, don’t crash at empty default export.

-
Fix #4556, which correctly handles new lines in the

`.gitignore`

file across OS. -
Add a new option to ignore unknown files

`--files-ignore-unknown`

:Doing so, Biome won’t emit diagnostics for files that doesn’t know how to handle.

-
Add the new option

`--no-errors-on-unmatched`

:Biome doesn’t exit with an error code if no files were processed in the given paths.

-
Fix the diagnostics emitted when running the

`biome format`

command. -
Biome no longer warns when discovering (possibly infinite) symbolic links between directories.

This fixes #4193 which resulted in incorrect warnings when a single file or directory was pointed at by multiple symbolic links. Symbolic links to other symbolic links do still trigger warnings if they are too deeply nested.

-
Introduced a new command called

`biome lint`

, which will only run lint rules against the code base. -
Biome recognizes known files as “JSON files with comments allowed”:

`typescript.json`

;`tsconfig.json`

;`jsconfig.json`

;`tslint.json`

;`babel.config.json`

;`.babelrc.json`

;`.ember-cli`

;`typedoc.json`

;`.eslintrc.json`

;`.eslintrc`

;`.jsfmtrc`

;`.jshintrc`

;`.swcrc`

;`.hintrc`

;`.babelrc`

;

-
Add support for

`biome.json`

;

### Configuration

Section titled “Configuration”#### Other changes

Section titled “Other changes”-
Add a new option to ignore unknown files:

Doing so, Biome won’t emit diagnostics for file that it doesn’t know how to handle.

-
Add a new

`"javascript"`

option to support the unsafe/experimental parameter decorators: -
Add a new

`"extends"`

option, useful to split the configuration file in multiple files:The resolution of the files is file system based, Biome doesn’t know how to resolve dependencies yet.

-
The commands

`biome check`

and`biome lint`

now show the remaining diagnostics even when`--apply-safe`

or`--apply-unsafe`

are passed. -
Fix the commands

`biome check`

and`biome lint`

, they won’t exit with an error code if no error diagnostics are emitted. -
Add a new option

`--error-on-warnings`

, which instructs Biome to exit with an error code when warnings are emitted. -
Add a configuration to enable parsing comments inside JSON files:

### Editors

Section titled “Editors”#### Other changes

Section titled “Other changes”-
The Biome LSP can now show diagnostics belonging to JSON lint rules.

-
The Biome LSP no longer applies unsafe quickfixes on-save when

`editor.codeActionsOnSave.quickfix.biome`

is enabled. -
Fix #4564; files too large don’t emit errors.

-
The Biome LSP sends client messages when files are ignored or too big.

### Formatter

Section titled “Formatter”-
Add a new option called

`--jsx-quote-style`

.This option lets you choose between single and double quotes for JSX attributes.

-
Add the option

`--arrow-parentheses`

.This option allows setting the parentheses style for arrow functions.

-
The

*JSON*formatter can now format`.json`

files with comments.

### Linter

Section titled “Linter”#### Removed rules

Section titled “Removed rules”-
Remove

`complexity/noExtraSemicolon`

(#4553)The

*Biome*formatter takes care of removing extra semicolons. Thus, there is no need for this rule. -
Remove

`useCamelCase`

Use useNamingConvention instead.

#### New rules

Section titled “New rules”-
Add noGlobalIsFinite

This rule recommends using

`Number.isFinite`

instead of the global and unsafe`isFinite`

that attempts a type coercion. -
Add noGlobalIsNan

This rule recommends using

`Number.isNaN`

instead of the global and unsafe`isNaN`

that attempts a type coercion. -
Add noUnsafeDeclarationMerging

This rule disallows declaration merging between an interface and a class.

-
This rule disallows useless aliasing of

`this`

in arrow functions. -
Add useArrowFunction

This rule proposes turning function expressions into arrow functions. Function expressions that use

`this`

are ignored. -
This rule disallow duplicate keys in a JSON object.

-
Add noVoid

This rule disallows the use of

`void`

. -
This rule disallows

`\8`

and`\9`

escape sequences in string literals. -
This rule disallows useless

`export {}`

. -
Add useIsArray

This rule proposes using

`Array.isArray()`

instead of`instanceof Array`

. -
Add useGetterReturn

This rule enforces the presence of non-empty return statements in getters. This makes the following code incorrect:

#### Promoted rules

Section titled “Promoted rules”New rules are promoted, please check #4750 for more details:

- a11y/useHeadingContent
- complexity/noForEach
- complexity/useLiteralKeys
- complexity/useSimpleNumberKeys
- correctness/useIsNan
- suspicious/noConsoleLog
- suspicious/noDuplicateJsxProps

The following rules are now recommended:

#### Other changes

Section titled “Other changes”-
Add new TypeScript globals (

`AsyncDisposable`

,`Awaited`

,`DecoratorContext`

, and others) 4643. -
noRedeclare: allow redeclare of index signatures are in different type members #4478

Improve noConsoleLog, noGlobalObjectCalls, useIsNan, and useNumericLiterals by handling
`globalThis`

and `window`

namespaces.

For instance, the following code is now reported by `noConsoleLog`

:

-
Improve noDuplicateParameters to manage constructor parameters.

-
Improve noInnerDeclarations

Now, the rule doesn’t report false-positives about ambient

*TypeScript*declarations. For example, the following code is no longer reported by the rule: -
Improve useEnumInitializers

The rule now reports all uninitialized members of an enum in a single diagnostic.

Moreover, ambient enum declarations are now ignored. This avoids reporting ambient enum declarations in

*TypeScript*declaration files. -
Relax noBannedTypes and improve documentation

The rule no longer reports a user type that reuses a banned type name. The following code is now allowed:

The rule now allows the use of the type

`{}`

to denote a non-nullable generic type:And in a type intersection for narrowing a type to its non-nullable equivalent type:

-
Improve noConstantCondition

The rule now allows

`while(true)`

. This recognizes a common pattern in the web community: -
Improve the diagnostic and the code action of useDefaultParameterLast.

The diagnostic now reports the last required parameter which should precede optional and default parameters.

The code action now removes any whitespace between the parameter name and its initialization.

-
Relax

`noConfusingArrow`

All arrow functions that enclose its parameter with parenthesis are allowed. Thus, the following snippet no longer trigger the rule:

The following snippet still triggers the rule:

-
Relax useLiteralEnumMembers

Enum members that refer to previous enum members are now allowed. This allows a common pattern in enum flags like in the following example:

Arbitrary numeric constant expressions are also allowed:

-
Improve useLiteralKeys.

Now, the rule suggests simplifying computed properties to string literal properties:

It also suggests simplifying string literal properties to static properties:

These suggestions are made in object literals, classes, interfaces, and object types.

-
Improve noNewSymbol.

The rule now handles cases where

`Symbol`

is namespaced with the global`globalThis`

or`window`

. -
The rules useExhaustiveDependencies and useHookAtTopLevel accept a different shape of options

Old configuration:

New configuration:

-
noRedundantUseStrict check only

`'use strict'`

directive to resolve false positive diagnostics.React introduced new directives, “use client” and “use server”. The rule raises false positive errors about these directives.

-
Fix a crash in the NoParameterAssign rule that occurred when there was a bogus binding. #4323

-
Fix useExhaustiveDependencies in the following cases #4330:

- when the first argument of hooks is a named function
- inside an export default function
- for
`React.use`

hooks

-
Fix noInvalidConstructorSuper that erroneously reported generic parents #4624.

-
Fix noDuplicateCase that erroneously reported as equals the strings literals

`"'"`

and`'"'`

#4706. -
Fix NoUnreachableSuper’s false positive diagnostics (#4483) caused to nested if statement.

The rule no longer reports

`This constructor calls super() in a loop`

when using nested if statements in a constructor. -
Fix useHookAtTopLevel’s false positive diagnostics (#4637)

The rule no longer reports false positive diagnostics when accessing properties directly from a hook and calling a hook inside function arguments.

-
Fix noUselessConstructor which erroneously reported constructors with default parameters rome#4781

-
Fix noUselessFragments’s panics when running

`biome check --apply-unsafe`

(#4637)This rule’s code action emits an invalid AST, so I fixed using JsxString instead of JsStringLiteral

-
Fix noUndeclaredVariables’s false positive diagnostics (#4675)

The semantic analyzer no longer handles

`this`

reference identifier. -
Fix noUnusedVariables’s false positive diagnostics (#4688)

The semantic analyzer handles ts export declaration clause correctly.

### Parser

Section titled “Parser”-
Add support for decorators in class method parameters, example:

This syntax is only supported via configuration, because it’s a non-standard syntax.

-
Add support for parsing comments inside JSON files:

-
Add support for the new

`using`

syntax

Copyright (c) 2023-present Biome Developers and Contributors.
