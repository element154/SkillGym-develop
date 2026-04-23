# Domains

## Drizzle

Section titled “Drizzle”Use this domain with projects using Drizzle.

### Drizzle activation

Section titled “Drizzle activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Drizzle dependencies

Section titled “Drizzle dependencies”Enabled when the following dependencies are declared:

`drizzle-orm`

:`>=0.9.0`

### Drizzle rules

Section titled “Drizzle rules”Rules that belong to the domain:

Use this domain inside Next.js projects.

### Next activation

Section titled “Next activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Next dependencies

Section titled “Next dependencies”Enabled when the following dependencies are declared:

`next`

:`>=14.0.0`

### Next rules

Section titled “Next rules”Rules that belong to the domain:

- noNextAsyncClientComponent
- useExhaustiveDependencies (recommended)
- useHookAtTopLevel (recommended)
- noBeforeInteractiveScriptOutsideDocument (nursery)
- noSyncScripts (nursery)
- useInlineScriptId (nursery)
- noImgElement (recommended)
- noUnwantedPolyfillio (recommended)
- useGoogleFontPreconnect (recommended)
- noHeadElement (recommended)
- noDocumentImportInPage (recommended)
- noHeadImportInDocument (recommended)

## Playwright

Section titled “Playwright”Use this domain inside Playwright test projects. This domain enables rules that help enforce best practices and catch common mistakes when writing Playwright tests.

### Playwright activation

Section titled “Playwright activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Playwright dependencies

Section titled “Playwright dependencies”Enabled when the following dependencies are declared:

`@playwright/test`

:`>=1.0.0`

### Playwright globals

Section titled “Playwright globals”When enabled, the following global bindings are recognised by Biome:

`test`

`expect`

### Playwright rules

Section titled “Playwright rules”Rules that belong to the domain:

- noPlaywrightElementHandle (nursery)
- noPlaywrightEval (nursery)
- noPlaywrightForceOption (nursery)
- noPlaywrightMissingAwait (nursery)
- noPlaywrightNetworkidle (nursery)
- noPlaywrightPagePause (nursery)
- noPlaywrightUselessAwait (nursery)
- noPlaywrightWaitForNavigation (nursery)
- noPlaywrightWaitForSelector (nursery)
- noPlaywrightWaitForTimeout (nursery)
- usePlaywrightValidDescribeCallback (nursery)

## Project

Section titled “Project”This domain contains rules that perform project-level analysis. This includes our module graph for dependency resolution. When enabling rules that belong to this domain, Biome will scan the entire project. The scanning phase will have a performance impact on the linting process. See the documentation on our scanner to learn more about the scanner.

### Project activation

Section titled “Project activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Project rules

Section titled “Project rules”Rules that belong to the domain:

- noPrivateImports (recommended)
- noUndeclaredDependencies
- noUnresolvedImports
- useImportExtensions
- useJsonImportAttributes
- noDeprecatedImports
- noImportCycles
- noUntrustedLicenses (nursery)

Use this domain inside Qwik projects. This domain enables rules that are specific to Qwik projects.

### Qwik activation

Section titled “Qwik activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Qwik dependencies

Section titled “Qwik dependencies”Enabled when the following dependencies are declared:

`@builder.io/qwik`

:`>=1.0.0`

`@qwik.dev/core`

:`>=2.0.0`

### Qwik rules

Section titled “Qwik rules”Rules that belong to the domain:

- noQwikUseVisibleTask (recommended)
- useImageSize (recommended)
- useJsxKeyInIterable (recommended)
- useQwikClasslist (recommended)
- useQwikMethodUsage (recommended)
- useQwikValidLexicalScope (recommended)
- useQwikLoaderLocation (nursery)
- noReactSpecificProps (recommended)

Use this domain inside React projects. It enables a set of rules that can help catching bugs and enforce correct practices. This domain enable rules that might conflict with the Solid domain.

### React activation

Section titled “React activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### React dependencies

Section titled “React dependencies”Enabled when the following dependencies are declared:

`react`

:`>=16.0.0`

### React rules

Section titled “React rules”Rules that belong to the domain:

- noChildrenProp (recommended)
- noNestedComponentDefinitions
- noReactPropAssignments
- noRenderReturnValue (recommended)
- useExhaustiveDependencies (recommended)
- useHookAtTopLevel (recommended)
- useJsxKeyInIterable (recommended)
- useUniqueElementIds
- noComponentHookFactories (nursery)
- noDuplicatedSpreadProps (nursery)
- noJsxNamespace (nursery)
- noJsxPropsBind (nursery)
- noLeakedRender (nursery)
- noSyncScripts (nursery)
- noUnknownAttribute (nursery)
- useReactAsyncServerFunction (nursery)
- noDangerouslySetInnerHtml (recommended)
- noDangerouslySetInnerHtmlWithChildren (recommended)
- useComponentExportOnlyModules
- useReactFunctionComponents
- noArrayIndexKey (recommended)
- noReactForwardRef

Use this domain inside Solid projects. This domain enables rules that might conflict with the React domain.

### Solid activation

Section titled “Solid activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Solid dependencies

Section titled “Solid dependencies”Enabled when the following dependencies are declared:

`solid`

:`>=1.0.0`

### Solid rules

Section titled “Solid rules”Rules that belong to the domain:

- noSolidDestructuredProps
- noDuplicatedSpreadProps (nursery)
- useSolidForComponent
- noReactSpecificProps (recommended)

Use this domain when linting test files. It enables a set of rules that are library agnostic, and can help to catch possible misuse of the test APIs.

### Test activation

Section titled “Test activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Test dependencies

Section titled “Test dependencies”Enabled when the following dependencies are declared:

`jest`

:`>=26.0.0`

`mocha`

:`>=8.0.0`

`ava`

:`>=2.0.0`

`vitest`

:`>=1.0.0`

### Test globals

Section titled “Test globals”When enabled, the following global bindings are recognised by Biome:

`after`

`afterAll`

`afterEach`

`before`

`beforeEach`

`beforeAll`

`context`

`describe`

`it`

`expect`

`run`

`setup`

`specify`

`suite`

`suiteSetup`

`suiteTeardown`

`teardown`

`test`

`xcontext`

`xdescribe`

`xit`

`xspecify`

### Test rules

Section titled “Test rules”Rules that belong to the domain:

- noExcessiveNestedTestSuites
- noConditionalExpect (nursery)
- noIdenticalTestTitle (nursery)
- useConsistentTestIt (nursery)
- useExpect (nursery)
- noDuplicateTestHooks (recommended)
- noExportsInTest (recommended)
- noFocusedTests (recommended)
- noSkippedTests

## Turborepo

Section titled “Turborepo”Use this domain inside Turborepo projects. This domain enables rules that are specific to Turborepo projects.

### Turborepo activation

Section titled “Turborepo activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Turborepo dependencies

Section titled “Turborepo dependencies”Enabled when the following dependencies are declared:

`turbo`

:`>=1.0.0`

### Turborepo rules

Section titled “Turborepo rules”Rules that belong to the domain:

This domain contains rules that perform project-level analysis. This includes our module graph for dependency resolution. When enabling rules that belong to this domain, Biome will scan the entire project, *and it will enable the inference engine to resolve and flat types*. The scanning phase will have a performance impact on the linting process. See the documentation on our scanner to learn more about the scanner.

### Types activation

Section titled “Types activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Types rules

Section titled “Types rules”Rules that belong to the domain:

- noFloatingPromises (nursery)
- noMisleadingReturnType (nursery)
- noMisusedPromises (nursery)
- noUnnecessaryConditions (nursery)
- noUnsafePlusOperands (nursery)
- noUselessTypeConversion (nursery)
- useArraySortCompare (nursery)
- useAwaitThenable (nursery)
- useConsistentEnumValueType (nursery)
- useDisposables (nursery)
- useExhaustiveSwitchCases (nursery)
- useFind (nursery)
- useNullishCoalescing (nursery)
- useRegexpExec (nursery)
- useStringStartsEndsWith (nursery)

Use this domain inside Vue projects. This domain enables rules that are specific to Vue projects.

### Vue activation

Section titled “Vue activation”Enable the **recommended, non-nursery** rules of the domain:

Enabled the **all** rules of the domain:

**Disable** all rules of the domain:

### Vue dependencies

Section titled “Vue dependencies”Enabled when the following dependencies are declared:

`vue`

:`>=3.0.0`

### Vue rules

Section titled “Vue rules”Rules that belong to the domain:

- noVueDataObjectDeclaration (recommended)
- noVueDuplicateKeys (recommended)
- noVueReservedKeys (recommended)
- noVueReservedProps (recommended)
- noVueSetupPropsReactivityLoss
- noVueArrowFuncInWatch (nursery)
- noVueOptionsApi (nursery)
- noVueRefAsOperand (nursery)
- useVueConsistentDefinePropsDeclaration (nursery)
- useVueDefineMacrosOrder (nursery)
- useVueMultiWordComponentNames (nursery)
- noVueVIfWithVFor (nursery)
- useScopedStyles (nursery)
- useVueConsistentVBindStyle (nursery)
- useVueConsistentVOnStyle (nursery)
- useVueHyphenatedAttributes (nursery)
- useVueVForKey (nursery)
- useVueValidTemplateRoot (nursery)
- useVueValidVBind (nursery)
- useVueValidVCloak (nursery)
- useVueValidVElse (nursery)
- useVueValidVElseIf (nursery)
- useVueValidVHtml (nursery)
- useVueValidVIf (nursery)
- useVueValidVOn (nursery)
- useVueValidVOnce (nursery)
- useVueValidVPre (nursery)
- useVueValidVText (nursery)
- useVueVapor (nursery)

Copyright (c) 2023-present Biome Developers and Contributors.
