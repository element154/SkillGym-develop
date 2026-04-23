# Roadmap 2025 and Biome 2.0

Today we’re happy to share our plans for Biome 2.0 as well as the rest of our roadmap for 2025. But before we dive into what’s coming, let’s do a quick recap of the major developments in 2024.

## 🎆 Recap: Biome in 2024

Section titled “🎆 Recap: Biome in 2024”2024 was a great year for Biome. Let’s see what happened:

- We released 4 new “minor” Biome versions, from 1.6 through 1.9, with plenty of useful features:
- New
`biome search`

and`biome explain`

commands, while the`biome migrate`

command was significantly expanded to help users coming from ESLint and Prettier. - Added support for
**CSS**and**GraphQL**formatting and linting. - Partial support for
**Astro**,**Svelte**and**Vue**files. - The ability to let configuration files extend from one another, which is especially useful in monorepo and larger organizational setups.
- Custom reporters for better CI integration and machine-readable output.
- Support for
`.editorconfig`

. - We added countless new lint rules and miscellaneous fixes and improvements, with a special shoutout to
`useSortedClasses`

that marks the beginning of dedicated**Tailwind**support.

- New
- Our team of maintainers has grown from 10 members at the start of 2024 to 18 today.
- We won the
**Productivity Booster**award of the OS Awards 2024. - We gained several new sponsors.
- We improved our IDE support on multiple fronts:
- A new Zed extension has been contributed to the project.
- Our VS Code extension has seen an overhaul that’s currently in Pre-Release.
- And even though this happened after the new year, we shouldn’t neglect to mention that our IDEA plugin has seen a major update too, which is now available in the nightly channel.

## 💳 Enterprise Support

Section titled “💳 Enterprise Support”One more thing that we are happy to announce is that as of January 2025, we are also offering Enterprise Support for Biome. Hopefully this will allow some of our contributors to spend more of their time and effort towards Biome!

## ⏭️ Biome 2.0

Section titled “⏭️ Biome 2.0”Right now our team is busy preparing for the Biome 2.0 release. Because our project is still run by volunteer contributors, we do not have an ETA for you. But we can share some of the goodies that will be coming:

**Plugins**. A long-requested feature, we started the development of Biome plugins after an RFC process that started in January 2024. Biome 2.0 will feature the first fruits of this labor: Users will be able to create their own lint rules using GritQL.**Domains**. Domains are a configuration feature that makes it easy for users to enable or disable all rules related to a specific domain, such as React, Next.js or testing frameworks. It also allows Biome to automatically enable recommended domain-specific rules based on the dependencies listed in your`package.json`

.**Monorepo Support**. While support for monorepos was already improved with our`extends`

feature in`biome.json`

, many weak spots remained. Biome 2.0 has an improved architecture based on an internal`ProjectLayout`

that should resolve most of these.**Suppressions**. Biome already allowed*suppression*of linter diagnostics through the use of`// biome-ignore`

suppression comments. With Biome 2.0 we’re adding support for`// biome-ignore-all`

and`// biome-ignore-start`

/`biome-ignore-end`

comments.**Multi-file analysis**. Last but not least, we’re adding true Multi-file support to Biome 2.0. This means that our lint rules will be able to query information from other files, which will enable much more powerful lint rules.

## 🌌 2025 roadmap

Section titled “🌌 2025 roadmap”Again, we should preface a disclaimer here: We’re a community-driven project, so we cannot promise to deliver any of the features below. But that doesn’t mean we don’t have a wishlist of things we would like to work on in 2025 😉

This year we will focus on:

**HTML support**. No toolchain for the web is complete without it, and we’re already working on it!**Embedded languages**. CSS or GraphQL snippets inside a template literal in a JavaScript file? JavaScript or CSS inside an HTML file? Biome should be able to handle these as well, and we’ll try to make it happen. This should also lead to better support for**Astro**,**Svelte**, and**Vue**than we have today.**Type inference**. This was already a wish for 2024, and we’re busy filling in the prerequisites such as multi-file analysis. There’s even an early proof-of-concept for a`noFloatingPromises`

rule. This year we want to ship a real version of`noFloatingPromises`

, and hopefully dabble further into type inference.**.d.ts generation**. While we’re on the subject of types, we would also like to create our first transformation: generating`.d.ts`

files from TypeScript sources. Initially we would only focus on TypeScript using Isolated Modules.**JSDoc support**. Can we use JSDoc comments as a source of type information too? If we are able to do type inference, this seems an opportunity we cannot pass on.**Markdown support**. Some work has already started for it and it would be a nice addition to round out our language support.**More plugins**. While Biome 2.0 will launch with the ability to create lint rules in GritQL, that’s only the tip of the iceberg. We know our users want more, and we certainly have ideas for more types of plugins. We’ll first collect feedback from the 2.0 release, and then we’ll decide which plugin area we’ll focus on next.

## ❤️ Your Support

Section titled “❤️ Your Support”We would like to thank our users and sponsors alike for their amazing support in 2024! Without you, this project would not be what it is today.

Hopefully we can also count on your support for the coming year. If you would like to help out, you can:

- Become a contributor. Please help us to build those features!
- Improve our documentation. Write guides or recipes, or help to keep our translations up-to-date for non-English speakers.

Copyright (c) 2023-present Biome Developers and Contributors.
