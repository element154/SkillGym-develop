Fast

Built with Rust and an innovative architecture inspired by rust-analyzer.

Format, lint, and more in a fraction of a second.

**Biome is a fast formatter** for *JavaScript*,
*TypeScript*, *JSX*, *TSX*, *JSON*, *HTML*, *CSS* and *GraphQL* that scores **97% compatibility with
Prettier**,

Biome can even **format malformed code** as you write it in your favorite editor.

CODE

OUTPUT

PERFORMANCE

Biome

Prettier

~35x

Faster than Prettier when formatting 171,127 lines of code in 2,104 files with an Intel Core i7 1270P.

Try the Biome formatter on the playground or directly on your project:

**Biome is a performant linter** for *JavaScript*,
*TypeScript*, *JSX*, *CSS* and *GraphQL* that features **479 rules** from ESLint,
TypeScript ESLint, and other sources.

**Biome outputs detailed and contextualized diagnostics** that help you to improve your code and become a better
programmer!

```
complexity/useFlatMap.js:2:1 lint/complexity/useFlatMap FIXABLE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```** ****✖** The call chain **.map().flat()** can be replaced with a single **.flatMap()** call.
**1 │ **const array = ["split", "the text", "into words"];
** ****>** **2 │ **array.map(sentence => sentence.split(' ')).flat();
** │ ****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^**
**3 │ **
** ****ℹ** Safe fix: Replace the chain with **.flatMap()**.
**1** **1**** │ ** const array = ["split", "the text", "into words"];
**2** ** │ **- **a****r****r****a****y****.****m****a****p**(sentence·=>·sentence.split('·'**)**)**.****f****l****a****t****(**);
**2**** │ **+ **a****r****r****a****y****.****f****l****a****t****M****a****p**(sentence·=>·sentence.split('·'));
**3** **3**** │ **

Try the Biome linter on the playground or directly on your project:

Not only can you format and lint your code separately, you can do it **all at once with a single command**!

Every tool integrates seamlessly with others to create **a cohesive toolchain** for web projects.

Run all tools with the `check`

command:

Fast

Built with Rust and an innovative architecture inspired by rust-analyzer.

Simple

Zero configuration needed to get started. Extensive options available for when you need them.

Scalable

Designed to handle codebases of any size. Focus on growing product instead of your tools.

Actionable & Informative

Avoid obscure error messages, when we tell you something is wrong, we tell you exactly where the problem is and how to fix it.

Batteries Included

Out of the box support for all the language features you use today. First class support for TypeScript and JSX.

Enterprise Support

We offer commercial support to organizations that need it through our community of contributors.

Install Biome using your preferred package manager AND integrate it in your editor.

Install with package manager

Integrate Biome in your editor

Join thousands of developers and companies using Biome in production

AWS

Canonical

Cloudflare

Coinbase

Comcast

Discord

Google

Microsoft

n8n

Node.js

Slack

Socket

Uniswap

Vercel

Astro

Copyright (c) 2023-present Biome Developers and Contributors.
