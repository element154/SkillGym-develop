# Biome v1.9 Anniversary Release

Today we’re excited to announce the release of Biome v1.9 and to celebrate the first anniversary of Biome 🎊 Let’s take a look back at the first year of Biome and then explore the new features in Biome 1.9.

## One year of Biome

Section titled “One year of Biome”We officially announced Biome on 29 August 2023. From its inception, Biome has been a free open source software driven by its community. We have a governance and a solid base of contributors to ensure the longevity of the project.

In October 2023, one of the creators of Prettier launched the Prettier challenge that rewarded any project written in Rust that passes at least 95% of the Prettier tests for JavaScript. The aim of this challenge was to create a fast competitor to Prettier in order to stimulate improvements in Prettier’s performance. We quickly organized ourselves to get there as soon as possible. By the end of November, we surpassed this goal by passing 97% of the Prettier tests for JavaScript, as well as TypeScript, JSX and TSX! The Biome formatter is really fast: it can format a large code base in less than 1 second. In the process, we identified several formatting issues in Prettier. This has also pushed contributions to Prettier that greatly improved its performance. This challenge was a win for the whole web ecosystem!

By winning the challenge, we brought Biome to light. Many developers were excited to discover a fast alternative to Prettier, but also a fast alternative to ESLint! The approach of bundling both a formatter and a linter in one tool provides a unified and consistent experience with minimal configuration. Biome has been quickly adopted by many projects, including big ones such as Ant Design, Astro, Sentry, daisyUI, Refine, Discord, Pulumi, Label Studio, Spicetify, Apify, Slint, Rspack, FluidFramework, and others. Biome surpassed 2.7 million monthly NPM downloads in August 2024.

We also gained many new contributors. Contributors who have made a significant contribution are regularly invited to join the Biome team. We started with a team of 5 core contributors, and we are now a team of 8 core contributors and 10 maintainers.

In June 2024, Biome won the JSNation’s productivity booster Open Source Award.

## Biome v1.9

Section titled “Biome v1.9”As we celebrate Biome’s first year, we’re pleased to announce the release of Biome 1.9, which brings many new features and bug fixes.

Once you have upgraded to Biome v1.9.0, migrate your Biome configuration to the new version by running the `migrate`

command:

### Stable CSS formatter and linter

Section titled “Stable CSS formatter and linter”We are thrilled to announce that Biome’s CSS formatter and linter are now considered stable and are **enabled by default**. Do note that Biome only parses **standard CSS syntax** so far, and doesn’t yet handle CSS dialects such as SCSS. As this is brand new functionality, you may also still run into some rough edges. Please report any problems you encounter!

The CSS linter provides 15 stable lint rules that were ported from stylelint:

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

It also provides the following nursery lint rules:

- nursery/noDuplicateCustomProperties
- nursery/noIrregularWhitespace
- nursery/noUnknownPseudoClass
- nursery/noUnknownPseudoElement
- nursery/noValueAtRule

If you don’t want Biome to format and lint your CSS files, you can disable the CSS formatter and linter in the Biome configuration file:

or on the command line:

Special thanks to Denis Bezrukov @denbezrukov, Jon Egeland @faultyserver and Yoshiaki Togami @togami2864 for coordinating and implementing most of the features related to CSS.

### Stable GraphQL formatter and linter

Section titled “Stable GraphQL formatter and linter”Another brand new feature: Biome now formats and lints GraphQL files by default.

For now, Biome provides only two nursery lint rules:

If you don’t want Biome to format and lint your GraphQL files, you can disable the GraphQL formatter and linter in the Biome configuration file:

or on the command line:

Special thanks to Swan that funded the implementation of the GraphQL formatter and to Võ Hoàng Long @vohoanglong0107 for implementing most of the features related to GraphQL.

### Search command

Section titled “Search command”Back in February, one of our Core Contributors published a proposal for plugin support. One of the highlights was the use of GritQL as a foundation for our plugin system.

GritQL is a powerful query language that lets you do structural searches on your codebase. This means that trivia such as whitespace or even the type of string quotes used will be ignored in your search query. It also has many features for querying the structure of your code, making it much more elegant for searching code than regular expressions.

Integrating a query language such as GritQL is no easy feat, and throughout the year we published multiple status updates. Today, we release the first product of this effort: A new `biome search`

command.

While we believe this command may already be useful to users in some situations (especially when it gets integrated in our IDE extensions!), this command is really a stepping stone towards our plugin efforts. By allowing our users to try it out in a first iteration, we hope to gain insight into the type of queries you want to do, as well as the bugs we need to focus on.

For now, the `search`

command is explicitly marked as **EXPERIMENTAL**, since many limitations are yet to be fixed or explored. Keep this in mind when you try it out, and please let us know what you think!
For an overview of specific limitations, please see the dedicated issue.

Even though there are still plenty of limitations, we do believe the integration has progressed far enough that we can shift our focus towards the integration of actual plugins. We cannot yet promise a timeline, but we’ll keep you posted!

PS.: GritQL escapes code snippets using backticks, but most shells interpret backticks as command invocations. To avoid this, it’s best to put single quotes around your Grit queries. For instance, the following command search for all `console.log`

invocations:

```
./benchmark/bench.js:38:3 search ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```**38 │ console.info(`\n⌛ repository: ${name}`);**
./packages/@biomejs/js-api/scripts/update-nightly-version.mjs:27:1 search ━━━━━━━━━━━━━━
**27 │ console.log(`version=${version}`);**
Searched 67 files in 1034ms. Found 2 matches.

Special thanks to Grit for open-sourcing GritQL, Arend van Beelen @arendjr for integrating the GritQL engine into Biome, and to @BackupMiles for implementing the formatting of search results in the `biome search`

command!

`.editorconfig`

support

Section titled “.editorconfig support”Biome is now able to take the `.editorconfig`

of your project into account. This is an opt-in feature. You have to turn it on in your Biome configuration file:

Note that all options specified in the Biome configuration file override the ones specified in `.editorconfig`

. For now, only the `.editorconfig`

at the root of your project is taken into account.

Special thanks to Carson McManus @dyc3 for implementing this feature!

### JavaScript formatter and linter

Section titled “JavaScript formatter and linter”We updated the JavaScript formatter to match Prettier v3.3. The most significant change is adding parentheses around nullish coalescing in ternaries. This change adds clarity to operator precedence.

Regarding the linter, we stabilized the following lint rules:

- a11y/noLabelWithoutControl
- a11y/useFocusableInteractive
- accessibility/useSemanticElements
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

We added the following new rules:

- nursery/noCommonJs
- nursery/noDuplicateCustomProperties
- nursery/noDynamicNamespaceImportAccess
- nursery/noEnum
- nursery/noIrregularWhitespace
- nursery/noRestrictedTypes
- nursery/noSecrets
- nursery/noUselessEscapeInRegex
- nursery/useConsistentMemberAccessibility
- nursery/useTrimStartEnd

And we deprecated the following rules:

`correctness/noInvalidNewBuiltin`

. Use correctness/noInvalidBuiltinInstantiation instead.`style/useSingleCaseStatement`

. Use correctness/noSwitchDeclarations instead.`suspicious/noConsoleLog`

. Use suspicious/noConsole instead.

Our linter has now more than 250 rules! Most of the ESLint rules and rules from some plugins have been ported. We are close to completing the port of ESLint.

### And more!

Section titled “And more!”For the full list of changes, please refer to our changelog.

## What’s next

Section titled “What’s next”### VSCode plugin v3

Section titled “VSCode plugin v3”Nicolas Hedger @nhedger is working on a new version of our first-party VSCode plugin. This new version will improve workspace support and fix some long-standing issues.

### Biome 2.0

Section titled “Biome 2.0”During this first year, we have discovered a number of issues that cannot be solved without introducing small breaking changes. For example, we rely on a glob library that sometimes doesn’t behave as users expect. We feel it is time to address these long-standing issues. Following our versioning philosophy, these small breaking changes cannot be made without releasing a major release. Therefore, the next release of Biome will be a major release: Biome 2.0. We will use this opportunity to remove deprecated features. We will make the migration smooth by using the `biome migrate`

command.

Copyright (c) 2023-present Biome Developers and Contributors.
