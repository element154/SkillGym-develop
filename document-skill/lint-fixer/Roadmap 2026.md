# Roadmap 2026

**In this article, we want to share with you all our roadmap for 2026!**

The roadmap is a collection of ideas and interests that the maintainers of the project collect from various sources: user’s feedback, personal interests, time available to dedicate to the project, user’s proposal from GitHub discussions.

The roadmap represents the overall direction that we want to take; however, things can change overtime.

## 2025 achievements

Section titled “2025 achievements”- We shipped Biome v2, which brought amazing new features to the ecosystem:
- Support for nested configuration files, and better support in monorepos.
- First tool to ship type-aware lint rules that don’t rely on the TypeScript compiler (commonly known as
`tsc`

), thanks to its inference engine, sponsored by Vercel. - Support for project lint rules, such as
`noImportCycle`

. - Shipped the new concept of linter domains, a way to group different rules under different umbrellas, and a way to turn on those rules automatically based on your dependencies.
- Added support for plugins via GritQL. Throughout the year the plugin engine has become even more powerful, allowing users to
**query the Biome CST**and report custom diagnostics. - Shipped the new JavaScript import and export organizer that provides advanced features like import merging, and custom import groups.

- We shipped
**three new minors**after v2, which have added many new features:- Support for Tailwind syntax in CSS files
- Experimental full support of parsing, formatting, linting for Vue, Svelte, and Astro. The language capabilities of Biome have improved and allow them to inspect multiple languages in the same document.
- We improved and fixed many bugs around the Biome watcher and scanner. Some of those bugs caused some memory leaks, causing Biome to be unusable for some users.

- We have surpassed 15 million monthly downloads.
- GritQL has now become part of the Biome organization.

### Past mistakes

Section titled “Past mistakes”Of course, Biome and team are far from being perfect, so we want to acknowledge some of our past mistakes that we hope to address this year. We want to address them moving forward.

#### Monorepo out of the box

Section titled “Monorepo out of the box”Biome is able to discover nested ignore files and nested configuration files out of the box, without any particular configuration. While this provides an optimal DX, it uncovered some undesired situations where memory leaks get out of hand. Also, in some cases, users don’t have enough control over the folders that are real libraries.

#### Difficult to debug

Section titled “Difficult to debug”With so many features, we overlooked the debugging capabilities of the tool. With the rise of tools such as `ultracite`

, big monorepos, `overrides`

, `extends`

, and more, it has become difficult to understand and debug a complex configuration file. This is frustrating for both maintainers and users.

#### Poor communication

Section titled “Poor communication”Later last year, we announced the experimental full support of Vue, Svelte, and Astro. Many users weren’t happy about how we framed the announcement, especially after some users rightfully complained about the poor support of the Svelte files.

## 2026 roadmap

Section titled “2026 roadmap”I can’t stress enough that Biome is a community-driven project, all the features we want to implement are driven by our passions and needs. We can’t promise that all of these features will be implemented. Alas, we will try our best to stay aligned and deliver what’s listed below.

-
**JavaScript embedded languages**: improve the DX of the embedded languages in JavaScript, such as CSS and GraphQL. -
**Stabilize everything around HTML**- Improve HTML formatting so that its formatting matches Prettier’s as much as possible.
- Enhance existing lint rules so that they work for HTML-ish languages too, notably Vue, Svelte, and Astro

-
**Cross-language lint rules**: we want to explore and deliver lint rules that work across languages. Now that Biome has the infrastructure to do so, we might be able to achieve it. What’s a cross-language lint rule, you ask? Here’s an example: have you ever discovered a CSS class not used anywhere? What if there was a lint rule able to discover all your CSS styles, and check if they are actually used inside JSX/HTML-ish files? That’s where a cross-language lint rule comes into play! -
**Opt-in, improved**: this is mostly an idea, but we want to address the poor DX introduced by monorepo-out-the-box, by making it opt-in and offer better control. For example, we envision a solution where the configuration might look like this:`workspaces`

With a configuration like this, Biome knows where to look for possible nested configuration files. We believe a solution like this

**might improve the DX and the performance of the tool**. -
**SCSS support**: we want to ship SCSS support. It was our most wanted. We recently closed it, and started the works. -
**More lint rules and assist actions**: keep shipping new lint rules, and assist actions. We recently started implementing Accessibility lint rules for HTML-ish languages. -
**Improve LSP features**: we want to explore and ship more LSP features. Internally, Biome has a module graph that can analyze and link with each other different files, such as JavaScript, CSS, and more. We want to explore and ship more IDE capabilities, such as the ability to highlight a reference such as a CSS class inside a JSX snippet, and allow users to navigate to its declaration inside the CSS file with a click. -
**Stabilize YAML**: our YAML parser is almost ready! Once the parsing is stable enough, formatting is just right there.

### Markdown

Section titled “Markdown”We really wish to implement the parsing of Markdown; however, we don’t have enough time and resources to look into it. If there’s someone who wishes to help, please let us know on Discord! We’re looking for **a champion** who would help with the implementation **and the reviews**.

## Can I help move Biome’s roadmap forward?

Section titled “Can I help move Biome’s roadmap forward?”We’re glad you asked! Biome is a project led by volunteers who like programming, open-source, and who embrace the Biome philosophy, so any help is welcome 😁

### Chat with us

Section titled “Chat with us”Join our Discord server, and engage with the community. You may always ask around if there’s something you can help with.

We also have a GitHub umbrella issue that you can check out, but please be cautious to not start any work until you’ve engaged with the community first. This way we can be mindful of your contributions too.

### Financial help

Section titled “Financial help”If you believe in the long-term vision of Biome, you can also help with a financial contribution, via Open Collective or GitHub Sponsors.

Additionally, the project provides an enterprise support program that companies can use to contract a core contributor to work on a specific aspect of the Biome toolchain.

Copyright (c) 2023-present Biome Developers and Contributors.
