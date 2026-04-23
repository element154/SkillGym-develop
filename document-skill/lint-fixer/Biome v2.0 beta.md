# Biome v2.0 beta

After hard work from our team, Biome’s long-awaited 2.0 release is nearing completion. It will be packed with many large features, so we would like your help testing it with a public beta!

If you would like to try it out, you can update Biome and migrate your configuration using the following commands:

Also, make sure you use the prereleases of our IDE extensions. The stable versions of our extensions are not yet prepared for Biome 2.0!

Documentation for the upcoming release can be found at https://next.biomejs.dev/.

## New features

Section titled “New features”While the final 2.0 release may still have small changes in its final feature set, here’s what you can expect in the beta:

**Plugins:**You can write custom lint rules using GritQL.**Domains:**Domains help to group lint rules by technology, framework, or well, domain. Thanks to domains, your default set of recommended lint rules will only include those that are relevant to your project.**Multi-file analysis:**Lint rules can now apply analysis based on information from other files, enabling rules such as`noImportCycles`

.Still a proof-of-concept, but our first type-aware lint rule is making an appearance.`noFloatingPromises`

:- Our
**Import Organizer**has seen a major revamp. **Assists:**Biome Assist can provide actions without diagnostics, such as sorting object keys.**Improved suppressions:**Suppress a rule in an entire file using`// biome-ignore-all`

, or suppress a range using`// biome-ignore-start`

and`// biome-ignore-end`

.**HTML formatter:**Still in preview, this is the first time we ship an HTML formatter.- Many,
**many**, fixes, new lint rules, and other improvements.

### Plugins

Section titled “Plugins”Biome 2.0 comes with our first iteration of Linter Plugins.

These plugins are still limited in scope: They allow for matching code snippets and reporting diagnostics on them.

Here is an example of a plugin that reports on all usages of `Object.assign()`

:

It’s a first step, but we have plenty of ideas for making them more powerful, and we’ll eagerly hear from our users on what they would like to see prioritised.

### Domains

Section titled “Domains”We’ve introduced a new linter feature: Domains.

Domains are a new way to organise lint rules by technology, framework, or well, domain. Right now, we have identified four domains:

`next`

: Rules related to Next.js.`react`

: Rules related to React.`solid`

: Rules related to Solid.js.`test`

: Rules related to testing, regardless of framework or library.

You can enable and disable rules that belong to a domain together:

But it gets better: Biome will automatically inspect your `package.json`

and determine which domains should be enabled by default. For instance, if you have `react`

defined as one of your dependencies, the default setting for the `react`

domain automatically becomes `recommended`

.

This way, Biome’s total set of recommended rules should be most relevant to your specific project needs.

And finally, domains can add global variables to the `javascript.globals`

setting. This should make Biome even easier to setup.

### Multi-file analysis

Section titled “Multi-file analysis”Before version 2.0, Biome lint rules could only operate on one file at a time. This brought us far, but many of the more interesting rules require information from other files too.

To accomplish this, we have added a *file scanner* to Biome that scans all the files in your project and indexes them, similar to what an LSP service might do in your IDE. We’re not going to beat around the bush: Scanning projects means that Biome has become slower for many projects. But we do believe the ability to do multi-file analysis is worth it. And without a scanner, multi-file analysis would become *even slower*, as rules would need to perform ad-hoc file system access individually.

That said, this is a beta, and there are certainly more opportunities to improve our scanner and its performance. If you have a repository where you feel our performance became unacceptably slow, please reach out and file an issue.

For now, we have a few interesting rules that can make use of our multi-file analysis:

`noImportCycles`

is able to look at import statements and detect cycles between them.`noPrivateImports`

is a new rule based on the`useImportRestrictions`

nursery rule from Biome 1.x, and inspired by ESLint’s`plugin-import-access`

. It forbids importing symbols with an`@private`

JSDoc tag from other modules, and forbids importing symbols with an`@package`

tag if the importing file is not in the same folder or one of its subfolders.`useImportExtensions`

has been improved because it can now determine the actual extension that needs to be used for an import, instead of guessing based on heuristics.

Finally, we’ve also designed the multi-file analysis with monorepos in mind. While full monorepo support may not make it in time for the 2.0 release, we expect to be able to deliver more on this front soon.

`noFloatingPromises`

Section titled “noFloatingPromises”With Biome’s linter we have always strived to provide a battery-included approach to linting. This means we’re not just aiming to replace ESLint, but also its plugins. One of the hardest plugins to replace is ** typescript-eslint**.

Biome has featured some rules from `typescript-eslint`

for a while now, but we could never replace all rules, because they relied on type information for their analysis. And in order to get type information, `typescript-eslint`

relies on `tsc`

itself, which is rather slow and also complicates setup.

This is about to change. With Biome 2.0, we’re introducing a first version of the `noFloatingPromises`

rule, one of the most-requested rules that relies on type information. In fairness, we should not consider it more than a proof-of-concept right now, because there are some notable limitations to its capabilities:

- It doesn’t understand complex types yet.
- It cannot do type inference yet.
- It can currently only analyse types that occur in the same file.

Still, its capabilities are sufficient to catch some of the low-hanging fruit. Consider this small snippet:

It will trigger the following diagnostic:

As you can guess, we intend to expand this rule’s capabilities over time. And with our new multi-file analysis in place, we expect to be able to make serious strides with this. Stay tuned for more announcements on this front!

### Import Organizer Revamp

Section titled “Import Organizer Revamp”In Biome 1.x, our Import Organizer had several limitations:

-
Groups of imports or exports would be considered separate

*chunks*, meaning they would be sorted independently. This meant the following**didn’t work**as expected:It would correctly sort

`"library1"`

to be placed above`"./utils.js"`

, but it wouldn’t be able to carry it over the newline to the top. What we got was this:But instead, what we really wanted was this:

-
Separate imports from the same module wouldn’t be merged. Consider the following example:

Nothing would be done to merge these import statements, whereas what we would have wanted was this:

-
No custom ordering could be configured. Maybe you didn’t really like the default approach of ordering by “distance” from the source file that you’re importing from. Maybe you wanted to organise like this:

In Biome 2.0, all these limitations are lifted. In fact, if you look at the examples above, all snippets labeled `organizer_v2.js`

can be produced just like that by our new import organizer.

Other improvements include support for organizing `export`

statements, support for “detached” comments for explicitly separating import chunks if necessary, and import attribute sorting.

You can find the documentation on the new import organizer at https://next.biomejs.dev/assist/actions/organize-imports/.

### Assists

Section titled “Assists”The Import Organizer was always a bit of a special case in Biome. It was neither part of the linter, nor of the formatter. This was because we didn’t want it to show diagnostics the way the linter does, while its organizing features went beyond what we expect from the formatter.

In Biome 2.0, we have generalised such use cases in the form of Biome Assist. The assist is meant to provide **actions**, which are similar to the *fixes* in lint rules, but without the diagnostics.

The Import Organizer has become an assist, but we’ve started using this approach for new assists too: `useSortedKeys`

can sort keys in object literals, while `useSortedAttributes`

can sort attributes in JSX.

For more information about assists, see: https://next.biomejs.dev/assist/

### Improved suppressions

Section titled “Improved suppressions”In addition to the `// biome-ignore`

comments we already supported, we now support `// biome-ignore-all`

for suppressing a lint rule or the formatter in an entire file.

We also added support for suppression ranges using `// biome-ignore-start`

and `// biome-ignore-end`

. Note that `// biome-ignore-end`

is optional in case you want to let a range run until the end of the file.

For more information about suppressions, see: https://next.biomejs.dev/linter/#suppress-lint-rules

### HTML formatter

Section titled “HTML formatter”After a few months of hard work, we are happy to announce that the HTML formatter is now ready for users to try out and start reporting bugs! This is a huge step towards Biome fully supporting HTML-ish templating languages used in frameworks like Vue and Svelte.

The HTML formatter only touches actual `.html`

files for now, so no formatting of html in `.vue`

or `.svelte`

files yet. It also won’t format embedded languages like JavaScript or CSS yet. HTML’s options like `attributePosition`

, `bracketSameLine`

, and `whitespaceSensitivity`

have been implemented.

The HTML formatter is still pretty experimental, so it will remain **disabled by default for the full 2.0 release**. At the time of writing, Biome is able to parse the grand majority of Prettier’s HTML tests, and format 46/124 of them correctly. Despite not matching Prettier yet, we’re pretty confident that it *should* output documents that are formatted adequately without destroying anything. If you find a case where it doesn’t, please let us know!

You can enable the HTML formatter by adding the following to your config file:

### New rules

Section titled “New rules”Several new rules have added since v1.9:

`noAwaitInLoop`

`noBitwiseOperators`

`noDestructuredProps`

`noFloatingPromises`

`noImportCycles`

`noPrivateImports`

`noTsIgnore`

`noUnwantedPolyfillio`

`useConsistentObjectDefinition`

`useForComponent`

### Miscellaneous

Section titled “Miscellaneous”**BREAKING:**The configuration fields`include`

and`ignore`

have been replaced with a single`includes`

field.**BREAKING:**Reworked some recommended rules recommended to be less pedantic and blocking. This is a breaking change if your project relied on those rules to block the CI in case of violations. If you used the`migrate`

command, the behaviour should remain as before.**BREAKING:**The`style`

rules aren’t recommended anymore. If you used the`migrate`

command, the behaviour should remain as before.**BREAKING:**Removed deprecated rules:`noConsoleLog`

`noInvalidNewBuiltin`

`noNewSymbol`

`useShorthandArrayType`

`useSingleCaseStatement`

**BREAKING:**Many deprecated options, including some that still referenced the old Rome name, have been removed.- Added a new option
`javascript.parser.jsxEverywhere`

to control whether Biome should expect JSX syntax in`.js`

/`.mjs`

/`.cjs`

files. - Improved monorepo support: The rule
`noUndeclaredDependencies`

now works correctly in monorepos by using the nearest`package.json`

file, instead of only the root one. - We have enabled support for
`.editorconfig`

files by default. - Changed default formatting of
`package.json`

to align better with formatting by package managers.

### And more!

Section titled “And more!”For the full list of changes, please refer to our changelog.

Copyright (c) 2023-present Biome Developers and Contributors.
