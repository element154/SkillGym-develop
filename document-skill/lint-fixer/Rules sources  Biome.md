# Rules sources

## Biome exclusive rules

Section titled “Biome exclusive rules”- noAccumulatingSpread
- noConstEnum
- noDelete
- noDynamicNamespaceImportAccess
- noEmptyTypeParameters
- noEnum
- noEvolvingTypes
- noExportedImports
- noGlobalIsFinite
- noGlobalIsNan
- noImplicitAnyLet
- noInlineStyles
- noMisleadingReturnType
- noRedundantDefaultExport
- noRedundantUseStrict
- noRenderReturnValue
- noShoutyConstants
- noSuspiciousSemicolonInJsx
- noSvgWithoutTitle
- noUnusedFunctionParameters
- noUnusedTemplateLiteral
- noUselessCatchBinding
- noUselessContinue
- noUselessEscapeInString
- noUselessStringRaw
- noVoidTypeReturn
- noVueOptionsApi
- useDisposables
- useImportExtensions
- useJsonImportAttributes
- useNodeAssertStrict
- useSimpleNumberKeys
- useSimplifiedLogicExpression
- useSortedClasses
- useStaticResponseMethods
- useStrictMode
- useTopLevelRegex
- useUniqueElementIds

## Rules from other sources

Section titled “Rules from other sources”### @e18e/eslint-plugin

Section titled “@e18e/eslint-plugin”| @e18e/eslint-plugin Rules name | Biome Rules name |
|---|---|
| prefer-array-at | useAtIndex |
| prefer-date-now | useDateNow |
| prefer-exponentiation-operator | useExponentiationOperator |
| prefer-object-has-own | noPrototypeBuiltins |
| prefer-spread-syntax | useObjectSpread (inspired) |

### @eslint-react/eslint-plugin

Section titled “@eslint-react/eslint-plugin”### @mysticatea/eslint-plugin

Section titled “@mysticatea/eslint-plugin”| @mysticatea/eslint-plugin Rules name | Biome Rules name |
|---|---|
| no-this-in-static | noThisInStatic |

### @next/eslint-plugin-next

Section titled “@next/eslint-plugin-next”### @stylistic/eslint-plugin

Section titled “@stylistic/eslint-plugin”| @stylistic/eslint-plugin Rules name | Biome Rules name |
|---|---|
| jsx-self-closing-comp | useSelfClosingElements |

### @vitest/eslint-plugin

Section titled “@vitest/eslint-plugin”| @vitest/eslint-plugin Rules name | Biome Rules name |
|---|---|
| consistent-test-it | useConsistentTestIt (inspired) |
| expect-expect | useExpect |
| max-nested-describe | noExcessiveNestedTestSuites |
| no-conditional-expect | noConditionalExpect |
| no-disabled-tests | noSkippedTests (inspired) |
| no-done-callback | noDoneCallback |
| no-duplicate-hooks | noDuplicateTestHooks (inspired) |
| no-focused-tests | noFocusedTests (inspired) |
| no-standalone-expect | noMisplacedAssertion (inspired) |

### Clippy

Section titled “Clippy”### Deno Lint

Section titled “Deno Lint”| Deno Lint Rules name | Biome Rules name |
|---|---|
| no-process-global | noProcessGlobal |

### ESLint

Section titled “ESLint”### eslint-plugin-barrel-files

Section titled “eslint-plugin-barrel-files”| eslint-plugin-barrel-files Rules name | Biome Rules name |
|---|---|
| avoid-barrel-files | noBarrelFile (inspired) |
| avoid-namespace-import | noNamespaceImport |
| avoid-re-export-all | noReExportAll |

### eslint-plugin-drizzle

Section titled “eslint-plugin-drizzle”| eslint-plugin-drizzle Rules name | Biome Rules name |
|---|---|
| enforce-delete-with-where | noDrizzleDeleteWithoutWhere |
| enforce-update-with-where | noDrizzleUpdateWithoutWhere |

### eslint-plugin-import

Section titled “eslint-plugin-import”### eslint-plugin-import-access

Section titled “eslint-plugin-import-access”| eslint-plugin-import-access Rules name | Biome Rules name |
|---|---|
| eslint-plugin-import-access | noPrivateImports |

### eslint-plugin-jest

Section titled “eslint-plugin-jest”| eslint-plugin-jest Rules name | Biome Rules name |
|---|---|
| consistent-test-it | useConsistentTestIt (inspired) |
| expect-expect | useExpect |
| max-nested-describe | noExcessiveNestedTestSuites |
| no-conditional-expect | noConditionalExpect |
| no-disabled-tests | noSkippedTests (inspired) |
| no-done-callback | noDoneCallback |
| no-duplicate-hooks | noDuplicateTestHooks (inspired) |
| no-export | noExportsInTest (inspired) |
| no-focused-tests | noFocusedTests (inspired) |
| no-standalone-expect | noMisplacedAssertion (inspired) |

### eslint-plugin-jsdoc

Section titled “eslint-plugin-jsdoc”| eslint-plugin-jsdoc Rules name | Biome Rules name |
|---|---|
| no-multi-asterisks | useSingleJsDocAsterisk |

### eslint-plugin-jsx-a11y

Section titled “eslint-plugin-jsx-a11y”### eslint-plugin-n

Section titled “eslint-plugin-n”| eslint-plugin-n Rules name | Biome Rules name |
|---|---|
| no-process-env | noProcessEnv |

### eslint-plugin-no-secrets

Section titled “eslint-plugin-no-secrets”| eslint-plugin-no-secrets Rules name | Biome Rules name |
|---|---|
| no-secrets | noSecrets (inspired) |

### eslint-plugin-playwright

Section titled “eslint-plugin-playwright”### eslint-plugin-promise

Section titled “eslint-plugin-promise”| eslint-plugin-promise Rules name | Biome Rules name |
|---|---|
| no-nesting | noNestedPromises |

### eslint-plugin-qwik

Section titled “eslint-plugin-qwik”### eslint-plugin-react

Section titled “eslint-plugin-react”### eslint-plugin-react-dom

Section titled “eslint-plugin-react-dom”### eslint-plugin-react-hooks

Section titled “eslint-plugin-react-hooks”| eslint-plugin-react-hooks Rules name | Biome Rules name |
|---|---|
| exhaustive-deps | useExhaustiveDependencies |
| react-compiler | noReactPropAssignments |
| rules-of-hooks | useHookAtTopLevel |

### eslint-plugin-react-jsx

Section titled “eslint-plugin-react-jsx”| eslint-plugin-react-jsx Rules name | Biome Rules name |
|---|---|
| no-children-prop | noChildrenProp |
| no-useless-fragment | noUselessFragments |

### eslint-plugin-react-prefer-function-component

Section titled “eslint-plugin-react-prefer-function-component”| eslint-plugin-react-prefer-function-component Rules name | Biome Rules name |
|---|---|
| react-prefer-function-component | useReactFunctionComponents |

### eslint-plugin-react-refresh

Section titled “eslint-plugin-react-refresh”| eslint-plugin-react-refresh Rules name | Biome Rules name |
|---|---|
| only-export-components | useComponentExportOnlyModules (inspired) |

### eslint-plugin-react-x

Section titled “eslint-plugin-react-x”### eslint-plugin-regexp

Section titled “eslint-plugin-regexp”| eslint-plugin-regexp Rules name | Biome Rules name |
|---|---|
| no-useless-backreference | noUselessRegexBackrefs |
| prefer-regexp-exec | useRegexpExec |

### eslint-plugin-solid

Section titled “eslint-plugin-solid”| eslint-plugin-solid Rules name | Biome Rules name |
|---|---|
| jsx-no-script-url | noScriptUrl |
| no-destructure | noSolidDestructuredProps (inspired) |
| no-react-specific-props | noReactSpecificProps |
| prefer-for | useSolidForComponent (inspired) |

### eslint-plugin-sonarjs

Section titled “eslint-plugin-sonarjs”| eslint-plugin-sonarjs Rules name | Biome Rules name |
|---|---|
| cognitive-complexity | noExcessiveCognitiveComplexity |
| prefer-while | useWhile |

### eslint-plugin-turbo

Section titled “eslint-plugin-turbo”| eslint-plugin-turbo Rules name | Biome Rules name |
|---|---|
| no-undeclared-env-vars | noUndeclaredEnvVars |

### eslint-plugin-unicorn

Section titled “eslint-plugin-unicorn”### eslint-plugin-unused-imports

Section titled “eslint-plugin-unused-imports”| eslint-plugin-unused-imports Rules name | Biome Rules name |
|---|---|
| no-unused-imports | noUnusedImports |
| no-unused-vars | noUnusedVariables |

### eslint-plugin-vue

Section titled “eslint-plugin-vue”### typescript-eslint

Section titled “typescript-eslint”Missing a rule? Help us by contributing to the analyzer or create a rule suggestion here.

Copyright (c) 2023-present Biome Developers and Contributors.
