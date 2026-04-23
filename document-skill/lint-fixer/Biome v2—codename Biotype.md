# Biome v2—codename: Biotype

We are happy to announce that Biome v2 is officially out! 🍾 Biome v2—codename: Biotype, the *first* JavaScript and TypeScript linter that provides
**type-aware linting rules that doesn’t rely on the TypeScript compiler**! This means that you can lint your project
without necessarily installing the `typescript`

package.

With this release, the Core Contributors of the project want to show to the whole community and web ecosystem that Biome is here to stay and deserves to earn its place as the next-generation toolchain for the web. No other tools have achieved this great milestone in such a short amount of time (two years) and resources. This has been possible thanks to the companies and people who believed in the project, with a special shoutout to Vercel for sponsoring the type inference work.

Preliminary testing shows that our `noFloatingPromises`

rule, which is based on our new type inference work, can detect floating promises in about 75% of the cases that would be detected by using `typescript-eslint`

, at a fraction of the performance impact. And needless to say, we have plenty of ideas on how to improve this metric even further.

Keep in mind that your mileage may vary, as these early numbers are based on a limited set of use cases. Nevertheless, we look forward to people trying it out and reporting their experiences so that we can quickly reach a level of confidence that would be sufficient for most projects.

## Installation and migration

Section titled “Installation and migration”Install or update the `@biomejs/biome`

package. If you upgrade the package, run the `migrate`

command.

The `migrate`

command will take care of all the breaking changes of the configuration, so you don’t have to. However, there are
some other changes that we couldn’t automate. We created a migration guide that explains them,
together with manual migration paths, if applicable. Please get accustomed to the changes, as some of them fundamentally
change some of the core functionalities of Biome (for the better!).

## Relevant features

Section titled “Relevant features”Biome is packed with new features, some big and some small. We will focus on the ones that we believe are worth mentioning. For a complete list of the new features, refer to the web version of the changelog.

### Multi-file analysis and type inference

Section titled “Multi-file analysis and type inference”These two features are closely related. You can’t create a type inference engine without the ability to query types imported from other modules.

Before version 2.0, Biome lint rules could only operate on one file at a time. This brought us far, but many of the more interesting rules require information from other files too.

To accomplish this, we have added a *file scanner* to Biome that scans all the files in your project and indexes them, similar to what an LSP service might do in your IDE.

A file scanner comes with its baggage: slowness. We acknowledge that many users choose Biome for its speed. During the beta period, users raised some concerns about how this could affect their workflow.

As for this release, the file scanner has the following characteristics:

- It’s
**opt-in**; which means migrating from v1 to v2 won’t significantly affect the performance of formatting and linting your projects. - By default, the scanner is only used for discovering nested configuration files. This should be very fast, although a slight increase compared to v1 may be experienced.
- A
**full scan**(which scans all your project files**and**`node_modules`

) is performed*only*when project rules are enabled. - Users can control the scanned files using
`files.includes`

, with the exception of`node_modules`

. - Lint rules that need to collect types or query the module graph
**will never be recommended**outside the`project`

domain. We put speed and performance first, and users have control over the rules.

### Monorepo Support

Section titled “Monorepo Support”We’ve significantly improved our support for monorepos. This means that lint rules that rely on information from `package.json`

files will now use the `package.json`

from the right package. But perhaps more importantly: **We now support nested configuration files.**

Every project should still have a single `biome.json`

or `biome.jsonc`

at its root, similar to Biome v1. But projects are allowed to have any number of nested `biome.json`

/`biome.jsonc`

files in subdirectories. Nested configuration files must be explicitly marked as such, in one of two ways.

The first looks like this:

By setting the `root`

field to `false`

, you tell Biome this is a nested file. This is important, because if you run Biome inside the nested folder, it will know that the configuration is part of a bigger project and continue looking for the root configuration as well.

It is important to stress that the settings within the nested folder **do not** inherit from the root settings by default. Rather, we still want you to use the `extends`

field that already existed in Biome v1 if you want to extend from another configuration.

Which brings us to the second way a nested configuration can be defined:

This is a convenient micro-syntax that sets both the `root`

field to `false`

, and will tell Biome that this nested configuration extends from the root configuration.

Say goodbye to wonky relative paths such as `"extends": ["../../biome.json"]`

👋

We prepared a small guide that should help you set everything up.

### Plugins

Section titled “Plugins”Biome 2.0 comes with our first iteration of Linter Plugins.

These plugins are still limited in scope: They only allow you to match code snippets and report diagnostics on them.

Here is an example of a plugin that reports on all usages of `Object.assign()`

:

It’s a first step, but we have plenty of ideas for making them more powerful, and we’re eager to hear from our users about what they would like to see prioritised.

As for now, we intentionally left out the distribution method of plugin for different reasons. However, we would like to hear from you. Please join the discussion and share your ideas with us.

### Import Organizer Revamp

Section titled “Import Organizer Revamp”In Biome 1.x, our Import Organizer had several limitations:

-
Groups of imports separated by a blank line were considered separate

*chunks*, meaning they were sorted independently. This meant the following**didn’t work**as expected:It would correctly sort

`"library1"`

to be placed above`"./utils.js"`

, but it wouldn’t be able to carry it over the blank line to the top. This is what we got:But instead, what we really wanted was this:

-
Imports from the same module were not merged. Consider the following example:

What we wanted was this:

-
No custom ordering could be configured. Perhaps you didn’t really like the default approach of ordering by “distance” from the source that you’re importing from. Perhaps you wanted to organise the imports like this:

In Biome 2.0, all these limitations are lifted. In fact, if you look at the examples above, all snippets labeled `organizer_v2.js`

can be produced just like that by our new import organizer.

Other improvements include support for organizing `export`

statements, support for “detached” comments to explicitly separate import chunks if necessary, and import attribute sorting.

You can find more in the documentation of the action.

### Assists

Section titled “Assists”The Import Organizer has always been a bit of a special case in Biome. It was neither part of the linter, nor of the formatter. This was because we didn’t want it to show diagnostics like the linter does, and its organizing features exceeded what we expect from the formatter.

In Biome 2.0, we have generalised such use cases in the form of Biome Assist. Assist provides **actions**, which are similar to the *fixes* in lint rules, but without the diagnostics.

The Import Organizer has become an assist, but we’ve started using this approach for new assists too: `useSortedKeys`

can sort keys in object literals, while `useSortedAttributes`

can sort attributes in JSX.

For more information about assists, see the relative page.

### Improved suppressions

Section titled “Improved suppressions”In addition to the `// biome-ignore`

comments we already supported, we now support `// biome-ignore-all`

for suppressing a lint rule or the formatter in an entire file.

We also added support for suppression ranges using `// biome-ignore-start`

and `// biome-ignore-end`

. Note that `// biome-ignore-end`

is optional in case you want to let a range run until the end of the file.

For more information about suppressions, see the relative page.

### HTML formatter

Section titled “HTML formatter”After several months of hard work, we are pleased to announce that the HTML formatter is now ready for users to try out and report bugs! This is a huge step towards Biome fully supporting HTML-ish templating languages used in frameworks such as Vue and Svelte.

For now, the HTML formatter only touches actual `.html`

files, so it doesn’t format HTML in `.vue`

or `.svelte`

files yet. It also won’t format embedded languages like JavaScript or CSS yet. HTML’s options like `attributePosition`

, `bracketSameLine`

, and `whitespaceSensitivity`

have been implemented.

The HTML formatter is still in the experimental stage, so it will remain **disabled by default for the full 2.0 release**. At the time of writing, Biome can parse most of the Prettier’s HTML test suite, and format 46/124 of them correctly. Despite not matching Prettier yet, we’re pretty confident that it *should* output adequately formatted documents without destroying anything. If you find a case where it doesn’t, please let us know!

You can enable the HTML formatter by adding the following to your config file:

## Shout-outs

Section titled “Shout-outs”And now, let’s give credits where credits are due!

Congratulations to Core Contributor @siketyan , who recently became a Core Contributor of the project! Thanks to their contributions, the JetBrains extension is now stable and supports multiple workspaces.

Thanks to Core Contributor @conaclos for their massive work in implementing many features such as the Import Organizer revamping, the new glob engine, many new linting rules.

Thanks to Core Contributor @arendjr for creating the multi-file architecture, the continuous work on the type inference, plugins, and miscellaneous improvements.

Props to Core Contributor @nhedger for authoring the GitHub Action, and shipping the new version of the VS Code extension.

Thanks to Core Contributor @dyc3 for leading the work on the HTML parser and formatter. They are both very complex pieces of software, especially when it comes to matching Prettier’s formatting experience.

Last but not least, a great thanks to all our other sponsors and contributors as well!

## What’s next

Section titled “What’s next”No software is exempt from bugs, so we will ensure that we squash them and release patches.

The Core Contributors will focus on moving forward the Roadmap for 2025, and focus on the following features:

- Make HTML support stable.
- Expand HTML to support other frameworks such as Vue, Svelte, and Astro.
- Work on Markdown support, starting from the parser.
- Continue working on the inference infrastructure, so we can cover more cases and add new rules.
- and more!

### I like where this is going, how can I help?

Section titled “I like where this is going, how can I help?”I want to remind you that Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome 😁

#### Translations

Section titled “Translations”#### Chat with us

Section titled “Chat with us”#### Code contributions

Section titled “Code contributions”If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project that does for you!

#### Financial help

Section titled “Financial help”Additionally, the project provides an enterprise support program where a company you can employ one of the core contributors to work a specific aspect of the Biome toolchain.

Copyright (c) 2023-present Biome Developers and Contributors.
