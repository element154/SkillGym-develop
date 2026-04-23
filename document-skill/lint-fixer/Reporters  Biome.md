Biome’s CLI accepts a `--reporter`

argument that allows to change how diagnostics and summary are printed to terminal.

biome check --reporter=summary

reporter/parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

i The following files have parsing errors.

reporter/format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

i The following files needs to be formatted.

reporter/violations ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

i Some lint rules or assist actions reported some violations.

lint/correctness/noUnknownFunction 14 (2 error(s), 12 warning(s), 0 info(s))

lint/suspicious/noImplicitAnyLet 16 (12 error(s), 4 warning(s), 0 info(s))

lint/suspicious/noDoubleEquals 8 (8 error(s), 0 warning(s), 0 info(s))

assist/source/organizeImports 2 (2 error(s), 0 warning(s), 0 info(s))

lint/suspicious/noRedeclare 12 (12 error(s), 0 warning(s), 0 info(s))

lint/suspicious/noDebugger 8 (8 error(s), 0 warning(s), 0 info(s))

It emits the summary and diagnostics in a JSON format.

Same as `--reporter=json`

, it emits the summary and diagnostics in a JSON format, and the output is formatted using the current JSON formatting options (configuration file or defaults).

biome ci --reporter=json-pretty

Use this reporter in a GitHub workflow. When properly configured in a PR workflow, GitHub will print a message for each info/warning/error emitted.

biome ci --reporter=github

::error title=lint/suspicious/noDoubleEquals,file=main.ts,line=4,endLine=4,col=3,endColumn=5::Use === instead of ==

::error title=lint/suspicious/noDebugger,file=main.ts,line=6,endLine=6,col=1,endColumn=9::This is an unexpected use of the debugger statement.

::error title=lint/nursery/noEvolvingAny,file=main.ts,line=8,endLine=8,col=5,endColumn=6::This variable's type is not allowed to evolve implicitly, leading to potential any types.

biome check --reporter=junit

<? xml version = " 1.0 " encoding = " UTF-8 " ?>

< testsuites name = " Biome " tests = " 16 " failures = " 16 " errors = " 20 " time = " <TIME> " >

< testsuite name = " main.ts " tests = " 1 " disabled = " 0 " errors = " 0 " failures = " 1 " package = " org.biome " >

< testcase name = " org.biome.lint.suspicious.noDoubleEquals " line = " 4 " column = " 3 " >

< failure message = " Use === instead of ==. == is only allowed when comparing against `null` " > line 3, col 2, Use === instead of ==. == is only allowed when comparing against `null` </ failure >

< testsuite name = " main.ts " tests = " 1 " disabled = " 0 " errors = " 0 " failures = " 1 " package = " org.biome " >

< testcase name = " org.biome.lint.suspicious.noDebugger " line = " 6 " column = " 1 " >

< failure message = " This is an unexpected use of the debugger statement. " > line 5, col 0, This is an unexpected use of the debugger statement. </ failure >

< testsuite name = " main.ts " tests = " 1 " disabled = " 0 " errors = " 0 " failures = " 1 " package = " org.biome " >

< testcase name = " org.biome.lint.nursery.noEvolvingAny " line = " 8 " column = " 5 " >

< failure message = " This variable's type is not allowed to evolve implicitly, leading to potential any types. " > line 7, col 4, This variable's type is not allowed to evolve implicitly, leading to potential any types. </ failure >

biome check --reporter=gitlab

"description" : " Several of these imports are unused. " ,

"check_name" : " lint/correctness/noUnusedImports " ,

"fingerprint" : " 15587197597897976171 " ,

"description" : " This variable f is unused. " ,

"check_name" : " lint/correctness/noUnusedVariables " ,

"fingerprint" : " 11560602666260894730 " ,

"description" : " Using == may be unsafe if you are relying on type coercion. " ,

"check_name" : " lint/suspicious/noDoubleEquals " ,

"fingerprint" : " 9497329216962766751 " ,

Use this reporter to emit diagnostics that follow tine Checkstyle format .

biome check --reporter=checkstyle

<? xml version = " 1.0 " encoding = " utf-8 " ?>

< checkstyle version = " 4.3 " >

< error line = " 1 " column = " 8 " severity = " warning " message = " This import is unused. " source = " lint/correctness/noUnusedImports " />

< error line = " 2 " column = " 10 " severity = " warning " message = " Several of these imports are unused. " source = " lint/correctness/noUnusedImports " />

< error line = " 8 " column = " 5 " severity = " warning " message = " This variable f is unused. " source = " lint/correctness/noUnusedVariables " />

< error line = " 9 " column = " 7 " severity = " warning " message = " This variable f is unused. " source = " lint/correctness/noUnusedVariables " />

< error line = " 1 " column = " 1 " severity = " error " message = " The imports and exports are not sorted. " source = " assist/source/organizeImports " />

< error line = " 4 " column = " 3 " severity = " error " message = " Using == may be unsafe if you are relying on type coercion. " source = " lint/suspicious/noDoubleEquals " />

< error line = " 6 " column = " 1 " severity = " error " message = " This is an unexpected use of the debugger statement. " source = " lint/suspicious/noDebugger " />

< error line = " 8 " column = " 5 " severity = " error " message = " This variable implicitly has the any type. " source = " lint/suspicious/noImplicitAnyLet " />

< error line = " 9 " column = " 7 " severity = " error " message = " This variable implicitly has the any type. " source = " lint/suspicious/noImplicitAnyLet " />

< error line = " 2 " column = " 10 " severity = " error " message = " Shouldn ' t redeclare ' z ' . Consider to delete it or rename it. " source = " lint/suspicious/noRedeclare " />

< error line = " 9 " column = " 7 " severity = " error " message = " Shouldn ' t redeclare ' f ' . Consider to delete it or rename it. " source = " lint/suspicious/noRedeclare " />

< error line = " 0 " column = " 0 " severity = " error " message = " Formatter would have printed the following content: " source = " format " />

< error line = " 1 " column = " 8 " severity = " warning " message = " This import is unused. " source = " lint/correctness/noUnusedImports " />

< error line = " 2 " column = " 10 " severity = " warning " message = " Several of these imports are unused. " source = " lint/correctness/noUnusedImports " />

< error line = " 8 " column = " 5 " severity = " warning " message = " This variable f is unused. " source = " lint/correctness/noUnusedVariables " />

< error line = " 9 " column = " 7 " severity = " warning " message = " This variable f is unused. " source = " lint/correctness/noUnusedVariables " />

< error line = " 1 " column = " 1 " severity = " error " message = " The imports and exports are not sorted. " source = " assist/source/organizeImports " />

< error line = " 4 " column = " 3 " severity = " error " message = " Using == may be unsafe if you are relying on type coercion. " source = " lint/suspicious/noDoubleEquals " />

< error line = " 6 " column = " 1 " severity = " error " message = " This is an unexpected use of the debugger statement. " source = " lint/suspicious/noDebugger " />

< error line = " 8 " column = " 5 " severity = " error " message = " This variable implicitly has the any type. " source = " lint/suspicious/noImplicitAnyLet " />

< error line = " 9 " column = " 7 " severity = " error " message = " This variable implicitly has the any type. " source = " lint/suspicious/noImplicitAnyLet " />

< error line = " 2 " column = " 10 " severity = " error " message = " Shouldn ' t redeclare ' z ' . Consider to delete it or rename it. " source = " lint/suspicious/noRedeclare " />

< error line = " 9 " column = " 7 " severity = " error " message = " Shouldn ' t redeclare ' f ' . Consider to delete it or rename it. " source = " lint/suspicious/noRedeclare " />

< error line = " 0 " column = " 0 " severity = " error " message = " Formatter would have printed the following content: " source = " format " />

Use this reporter to emit diagnostics that follow the RDJSON format .

biome check --reporter=rdjson

"url" : " https://biomejs.dev "

"url" : " https://biomejs.dev/linter/rules/no-unused-imports " ,

"value" : " lint/correctness/noUnusedImports "

"message" : " This import is unused. "

"url" : " https://biomejs.dev/linter/rules/no-unused-imports " ,

"value" : " lint/correctness/noUnusedImports "

"message" : " Several of these imports are unused. "

Use this reporter to emit diagnostics that follow the SARIF format .

biome check --reporter=sarif

"$schema" : " https://json.schemastore.org/sarif-2.1.0.json " ,

"informationUri" : " https://biomejs.dev " ,

"id" : " lint/correctness/noUnusedImports " ,

"text" : " Disallow unused imports. "

"helpUri" : " https://biomejs.dev/linter/rules/no-unused-imports "

"ruleId" : " lint/correctness/noUnusedImports " ,

"text" : " This import is unused. "
