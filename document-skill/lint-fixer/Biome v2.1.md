# Biome v2.1

Biome 2.0 was released less than a month ago, and since then we have seen an amazing uptake! Our Discord is buzzing, our downloads are spiking, and bugs are rolling in :)

## Faster scanner

Section titled “Faster scanner”Probably the main point of contention is that Biome 2.0 introduced a new scanner, which we use for discovering nested configuration files as well as for populating our module graph, if project rules are enabled. The reason for this contention is that having a scanner makes things slower, while people want Biome to be fast.

To mitigate the impact, we already made the project rules opt-in for 2.0, so
that users can choose between features and speed for themselves. But ideally,
we’d have both. And unfortunately, even without project rules, the scanner still
caused *some* noticeable overhead.

For Biome 2.1 we’re changing the logic for how the “light scanner” (the one where project rules are disabled) works. Previously, it would always scan the entire project from its root, whereas now it will use the files and folders that you ask Biome to operate on as a hint for which parts of the project should be scanned.

This means if you run Biome without any arguments from the project root, you are not going to notice a difference. But if you specify specific files to check, or if you run Biome inside a nested folder, the scanner will know which parts of the project you are interested in, and only scan those.

Note that if you have enabled project rules, these improvements don’t apply.
This is because project rules often need to pull information from other files,
*including ones you didn’t specify*, so we still scan the entire project for
now.

## Improved type inference

Section titled “Improved type inference”When we released Biome 2.0, we mentioned that our type inference was able to
detect ~75% of cases that our
`noFloatingPromises`

rule
should ideally detect. Since then, we’ve been able to improve this to ~85%, and
cases such as these can now be successfully inferred:

Additionally, we have added support for getters, call signatures, comma operators, and more. Our goal is for you to not have to worry about which parts of TypeScript are supported, and the vast majority of cases to “just work”. It’s still a work in progress, but we’re happy with the progress we are seeing.

And finally we have also added the related rule
`noMisusedPromises`

.

## Rule updates

Section titled “Rule updates”The following new rules have been added in 2.1.0:

`noAlert`

`noImplicitCoercion`

`noMagicNumbers`

`noMisusedPromises`

`noUnassignedVariables`

`useReadonlyClassProperties`

`useUnifiedTypeSignature`

Other notable change:

- The rule
`noUnusedFunctionParameters`

has been enhanced with an`ignoreRestSiblings`

option.

## Notable bug fixes

Section titled “Notable bug fixes”- If you ignore a nested configuration file from your root configuration, it will now be properly ignored.
- When extending a configuration from another, we now correctly ignore the
`root`

of the other configuration. This one led to some confusion in several use cases.

## What’s next

Section titled “What’s next”It’s still early days in our 2.x journey. Both the scanner are type inference are likely to see further improvements. Additionally, our Core Contributors will focus on moving forward the Roadmap for 2025, and focus on the following features:

- Make HTML support stable.
- Expand HTML to support other frameworks such as Vue, Svelte, Astro and, hopefully, Angular too.
- Work on Markdown support, starting from the parser.
- and more!

## Installation and migration

Section titled “Installation and migration”Install or update the `@biomejs/biome`

package. If you upgrade the package, run
the `migrate`

command.

The `migrate`

command takes care of breaking changes of the configuration, so
you don’t have to.

## I like where this is going, how can I help?

Section titled “I like where this is going, how can I help?”Biome is a project led by volunteers who like programming, open-source, and embrace the Biome philosophy, so any help is welcome 😁

### Translations

Section titled “Translations”If you are familiar with Biome and would like to contribute to its outreach, you can assist us by translating the website into your native language. In this dashboard, you can check the supported languages and if they are up to date.

### Chat with us

Section titled “Chat with us”### Code contributions

Section titled “Code contributions”If you like the technical aspects of the project, and you want to make your way into the Rust language, or practice your knowledge around parsers, compilers, analysers, etc., Biome is the project that does for you!

- Create new lint rules! We have so many rules that we haven’t implemented yet (ESLint, ESLint plugins, Next.js, Solid, etc.). We have an extensive technical guide.

### Financial help

Section titled “Financial help”Additionally, the project provides an enterprise support program where as a company you can contract one of the core contributors to work on a specific aspect of the Biome toolchain.

Copyright (c) 2023-present Biome Developers and Contributors.
