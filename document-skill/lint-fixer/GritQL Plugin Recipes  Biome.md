# GritQL Plugin Recipes

This page provides a collection of practical GritQL plugin examples that you can use directly in your projects. Each example is designed to demonstrate a specific GritQL feature while solving a real-world linting problem.

For an introduction to GritQL syntax and the plugin system, see the Linter Plugins and GritQL reference pages first.

To use any of the examples below, save the GritQL snippet to a `.grit`

file in
your project and register it in your configuration:

Alternatively, you can navigate the playground link attached to each example.

## JavaScript / TypeScript

Section titled “JavaScript / TypeScript”Below, there’s a collection of examples for JavaScript/TypeScript language.

### Enforce strict equality except against `null`

Section titled “Enforce strict equality except against null”GritQL patterns can have **conditions** attached via the `where`

clause. Inside
a `where`

block, the **match operator** `<:`

tests whether a variable matches a
given pattern, and the ** not** keyword negates that test. Multiple conditions
separated by commas must all be true for the pattern to match.

Here we match any `==`

comparison, then use two conditions with `not`

to skip
cases where either operand is the literal `null`

— since `== null`

is the one
idiomatic use of loose equality:

Matched — neither side is `null`

:

Not matched — one side is `null`

, so loose equality is acceptable:

Try this example in the Playground

### Ban `forEach`

— prefer `for...of`

Section titled “Ban forEach — prefer for...of”The **spread metavariable** `$...`

matches zero or more arguments (or list
elements) without binding them. The ** as** keyword binds the entire matched
node to a variable, so you can reference it later — typically to set the
diagnostic

`span`

.We use `$...`

to match `.forEach()`

regardless of how many arguments are passed,
and `as $call`

to capture the full expression for the diagnostic span:

Both `.forEach()`

calls are matched (lines 2 and 3). The `for...of`

loop on
line 6 is not affected.

Try this example in the Playground

### No restricted imports

Section titled “No restricted imports”The ** or** operator matches if any of its child patterns match. Here we use
it to list multiple banned package names. The

**anonymous metavariable**

`$_`

matches any node without creating a named binding — useful when you don’t care
about the value.We match any `import`

statement, ignore the imported bindings with `$_`

, and
check whether the source string matches any of the banned packages:

Lines 1, 3, and 4 are matched. Line 2 (`dayjs`

) is not in the banned list.

Try this example in the Playground

You can also catch `require()`

calls in the same file by using a **top-level
or** to match both import styles:

Both `import`

and `require()`

forms are matched for banned packages. `dayjs`

on
line 2 is not in the list.

Try this example in the Playground

### Ban `new Date()`

— use a date library

Section titled “Ban new Date() — use a date library”When a code snippet contains `$...`

as the only argument, it matches
**zero or more arguments**. When you add a named metavariable before it like
`$first, $...`

, the pattern requires **at least one argument** — `$first`

must
bind to something.

Here `$first`

requires at least one argument, so `new Date()`

(getting “now”)
is allowed while `new Date("2024-01-15")`

and similar parsing calls are
flagged:

Line 1 (`new Date()`

with no args) is not matched. Lines 2-4 all have at least
one argument, so they trigger the diagnostic.

Try this example in the Playground

### Ban `eval()`

and `Function()`

constructor

Section titled “Ban eval() and Function() constructor”A **top-level or** lets you combine unrelated syntax patterns into a single
plugin rule. Each arm can use

`as $match`

to **unify the variable name**so that the shared

`where`

clause can reference it consistently — even though the
arms match completely different syntax shapes.Here we combine `eval()`

calls and `new Function()`

constructors into one rule:

Lines 1 and 2 are matched. Line 3 is not — `JSON.parse`

is a different pattern
entirely.

Try this example in the Playground

### No nested ternaries

Section titled “No nested ternaries”Instead of matching source code snippets, you can match against **Biome’s
concrete syntax tree (CST) nodes** directly. Each node type has a unique
`PascalCase`

name like `JsConditionalExpression`

. The ** contains** modifier
searches the entire subtree of a matched node, catching nested structures at
any depth.

Here we find any ternary that contains another ternary nested inside it:

Line 1 has a single (non-nested) ternary and is not matched. Lines 2 and 3 each contain a ternary inside another ternary.

Try this example in the Playground

### Limit function parameters

Section titled “Limit function parameters”We match ** JsParameters()** and use a

**regex**to check whether the parameter list contains 3 or more commas — meaning 4 or more parameters:

`ok`

has 3 parameters and is fine. `tooMany`

and `arrow`

both have 4+ parameters
and are matched.

Try this example in the Playground

### No empty catch blocks

Section titled “No empty catch blocks”CST nodes can be **nested** in the pattern to express structural constraints.
Here we match a `JsCatchClause`

whose `body`

field is a `JsBlockStatement`

with
an empty `statements`

list (`[]`

). This reads almost like a type assertion: “a
catch clause containing a block with no statements.”

The first `catch`

block (line 3) is empty and matched. The second one has a
statement inside and is not.

Try this example in the Playground

### Disallow `any`

type annotation

Section titled “Disallow any type annotation”Some CST nodes are specific to **TypeScript**. The `TsAnyType`

node represents
the `any`

keyword wherever it appears as a type annotation. By matching this
node directly, you catch every occurrence — in variable declarations, function
parameters, return types, and generic arguments.

Every `any`

annotation on lines 1-3 is matched. The `unknown`

on line 4 is a
different type and is not affected.

Try this example in the Playground

### Enforce `const`

over `let`

Section titled “Enforce const over let”Since `let`

is a keyword rather than a syntax node, we match
** JsVariableStatement()** and filter with a

**regex**to select only statements whose text starts with

`let`

:Both `let`

statements (lines 1 and 2) are matched. The `const`

on line 3 is
not — its text starts with `const`

, so the regex `let.*`

doesn’t match.

Try this example in the Playground

### Ban `dangerouslySetInnerHTML`

Section titled “Ban dangerouslySetInnerHTML”GritQL snippet patterns work inside JSX. Here we match the
`dangerouslySetInnerHTML`

prop regardless of the element it’s on or the value
passed to it:

Matched — any element using the prop:

Not matched — no `dangerouslySetInnerHTML`

:

Try this example in the Playground

### No inline `style`

props

Section titled “No inline style props”The same approach works for banning inline `style`

props. This encourages
the use of CSS classes or CSS-in-JS solutions instead of inline styles:

Matched — inline `style`

prop:

Not matched — using `className`

instead:

Try this example in the Playground

### Disallow `!important`

Section titled “Disallow !important”By default, GritQL patterns target JavaScript. The ** engine biome(1.0)** and

**directives at the top of a**

`language css`

`.grit`

file switch to Biome’s CSS
syntax tree. The `!important`

modifier is represented as a
**node, so we use**

`CssDeclarationImportant()`

**to find any declaration that includes it:**

`contains`

Lines 2 and 6 contain `!important`

declarations and are matched.

Try this example in the Playground

### Ban hardcoded colors — use CSS custom properties

Section titled “Ban hardcoded colors — use CSS custom properties”**Regex patterns** use the `r"..."`

syntax. They match against the text content
of a node rather than its syntactic structure. This is useful for matching
values like hex color codes that don’t have a dedicated syntax node.

Here we use a regex to match any hex color value in `color`

declarations:

Lines 2 and 6 use hardcoded hex colors and are matched. The `var()`

reference
on line 3 is not a hex value and passes.

Try this example in the Playground

To also catch `rgb()`

and `hsl()`

functions, combine multiple regex patterns
with `or`

:

Matched — hex, `rgb()`

, and `hsl()`

values:

The `var()`

references on lines 3 and 12 don’t match any of the regex patterns and pass.

Try this example in the Playground

### Disallow specific CSS properties

Section titled “Disallow specific CSS properties”A top-level ** or** lists alternative snippet patterns. Each arm matches
independently, so you can ban multiple CSS properties by listing them
explicitly:

`float`

on line 2 and `clear`

on line 6 are matched. The `.modern`

rule uses
`display: grid`

which is not in the banned list.

Try this example in the Playground

### Enforce JSON key naming conventions

Section titled “Enforce JSON key naming conventions”The ** language json** directive (used with

`engine biome(1.0)`

) targets JSON
files. Since JSON snippets with metavariables aren’t supported, use the CST node
**to match any key. Combined with**

`JsonMemberName()`

**regex**and

**, this lets you enforce naming conventions.**

`or`

Here we flag any key that contains an underscore or starts with an uppercase letter — both violate camelCase:

`user_name`

(snake_case) and `UserAge`

(PascalCase) are matched by the regex
alternatives. `userName`

and `email`

are valid camelCase and not matched.

Try this example in the Playground

## Advanced Patterns

Section titled “Advanced Patterns”### Combine multiple related rules in one file

Section titled “Combine multiple related rules in one file”You can group **multiple independent rules** into a single `.grit`

file using a
top-level `or`

. Each arm has its own pattern, conditions, and diagnostic. The
`where`

clause can be placed inside each arm independently, giving each rule
its own severity and message.

Here we combine three debug-related checks into one plugin:

Lines 1, 2, 3, and 5 are matched by different arms of the `or`

. Line 4
(`console.error`

) is not in the `log`

, `debug`

, `trace`

list and passes.

Try this example in the Playground

## Discovering CST Node Names

Section titled “Discovering CST Node Names”Several examples above use Biome’s CST node names like `JsConditionalExpression`

or `TsAnyType`

. Here’s how to find the right node name for the code you want to
match.

### Using the Biome Playground

Section titled “Using the Biome Playground”- Open the Biome Playground.
- Paste or type the code snippet you want to match.
- Switch to the
**Syntax**tab in the output panel on the right. - The syntax tree is displayed with every node labeled by its type name. Expand nodes to see their children and fields.
- Use the node name you find in your GritQL pattern:
`NodeName()`

for any instance, or`NodeName(field = ...)`

to match specific children.

### Common node names

Section titled “Common node names”Here are some frequently useful Biome CST node names for JavaScript/TypeScript:

| Node Name | Matches |
|---|---|
`JsIfStatement` | `if (...) { ... }` |
`JsConditionalExpression` | `a ? b : c` |
`JsForStatement` | `for (...; ...; ...) { ... }` |
`JsForOfStatement` | `for (... of ...) { ... }` |
`JsCallExpression` | `fn()` , `obj.method()` |
`JsNewExpression` | `new Foo()` |
`JsArrowFunctionExpression` | `() => { ... }` |
`JsFunctionDeclaration` | `function foo() { ... }` |
`JsCatchClause` | `catch (e) { ... }` |
`JsBlockStatement` | `{ ... }` (block of statements) |
`JsFormalParameter` | A single function parameter |
`JsParameters` | The parameter list `(a, b, c)` |
`JsVariableDeclaration` | `const x = 1` , `let y = 2` |
`TsAnyType` | `: any` type annotation |
`TsTypeAlias` | `type Foo = ...` |
`TsInterfaceDeclaration` | `interface Foo { ... }` |
`JsxElement` | `<div>...</div>` |
`JsxSelfClosingElement` | `<img />` |
`JsxAttribute` | `className="test"` , `disabled` |

For CSS:

| Node Name | Matches |
|---|---|
`CssDeclarationWithSemicolon` | `property: value;` |
`CssComplexSelector` | `div > .class` |

### Header directives for CST patterns

Section titled “Header directives for CST patterns”When using CST node names, your `.grit`

file should include the engine and
language directives:

The `engine biome(1.0)`

directive tells GritQL to use Biome’s syntax tree (as
opposed to Tree-sitter’s). The `language`

directive specifies which language
grammar to match against — without it, JavaScript is assumed.

Copyright (c) 2023-present Biome Developers and Contributors.
