# Differences with Prettier

In some cases, Biome has intentionally decided to format code in a way that doesn’t match Prettier’s output. These divergences are explained below.

## Prettier doesn’t unquote some object properties that are valid JavaScript identifiers.

Section titled “Prettier doesn’t unquote some object properties that are valid JavaScript identifiers.”Prettier and Biome unquote object and class properties that are valid JavaScript identifiers. Prettier unquotes only valid ES5 identifiers.

This is a legacy restriction in an ecosystem where ES2015 is now widespread. Thus, we decided to diverge here by un-quoting all valid JavaScript identifiers in ES2015+.

A possible workaround would be to introduce a configuration to set the ECMAScript version a project uses.
We could then adjust the un-quoting behaviour based on that version.
Setting the ECMAScript version to `ES5`

could match Prettier’s behaviour.

Diff

## Prettier has an inconsistent behavior for assignment in computed keys.

Section titled “Prettier has an inconsistent behavior for assignment in computed keys.”Prettier and Biome enclose some assignment expressions between parentheses, particularly in conditionals. This allows Biome to identify an expression that should be a comparison.

Prettier has inconsistent behaviour because it adds parentheses for an assignment in a computed key of an object property and doesn’t for a computed key of a class property, as demonstrated by the following example:

Input

Diff

To be consistent, we decided to diverge and omit the parentheses. Alternatively, we could enclose any assignment in a computed key of an object or of a class.

## Prettier adds a trailing comma to type parameters of arrow functions even when it is not required.

Section titled “Prettier adds a trailing comma to type parameters of arrow functions even when it is not required.”In some specific cases, a type parameter list of an arrow function requires a trailing comma to distinguish it from a JSX element. When a default type is provided, this trailing comma is not required. Here, we diverge from Prettier because we think it better respects the original intent of Prettier, which was to add a trailing comma only when required.

Input

Diff

## Prettier has an inconsistent behavior for parenthesized non-null-asserted optional chains

Section titled “Prettier has an inconsistent behavior for parenthesized non-null-asserted optional chains”In *TypeScript*, the non-null assertion operator `!`

allows asserting that a value is non-null.
When applied on an optional chain, the assertion applies to the entire chain regardless of the presence of parentheses,
making equivalent `(a.?.b)!`

and `a.?.b!`

.

The previous code examples are already well-formatted, according to Prettier. Prettier is used to enforce the presence or the absence of parentheses. This looks like a missed opportunity to normalize the code.

Moreover, Prettier doesn’t remove the parentheses even when they enclose the non-null assertion. Instead, it moves the operator outside the parentheses.

Input:

Diff

## Prettier formats invalid syntaxes

Section titled “Prettier formats invalid syntaxes”Prettier’s Babel-based parsing for JavaScript and TypeScript is very loose and allows multiple errors to be ignored. Biome’s parser is intentionally stricter than the Prettier parser. It correctly identifies the following syntax errors:

- A function cannot have duplicate modifiers
- invalid order of properties’ modifiers
- Function declarations are not allowed to have bodies
- non-abstract classes cannot have abstract properties
- An optional chain cannot be assigned
- The
`const`

modifier cannot be set on a type parameter of an interface - top-level return
- etc.

In Prettier, these errors aren’t considered parse errors, and the AST is still built “correctly” with the appropriate nodes. When formatting, Prettier treats these nodes as normal and formats them accordingly.

In Biome, the parsing errors result in `Bogus`

nodes, which may contain any number of valid nodes, invalid nodes, and/or raw characters.
When formatting, Biome treats bogus nodes as effectively plain text, printing them out verbatim into the resulting code without any formatting since attempting to format them could be incorrect and cause semantic changes.

For class properties, Prettier’s current parsing strategy also uses boolean fields for modifiers, meaning only one of each kind of modifier can ever be present (accessibility modifiers are stored as a single string). When printing, Prettier looks at the list of booleans and decides which modifiers to print out again. Biome instead keeps a list of modifiers, meaning duplicates are kept around and can be analyzed (hence the parsing error messages about duplicate modifiers and ordering). When printing out the bogus nodes, this list is kept intact, and printing out the unformatted text results in those modifiers continuing to exist.

There are ways that Biome can address this. One possibility is to try to interpret the Bogus nodes when formatting and construct valid nodes out of them. If a valid node can be built, then it would just format that node like normal, otherwise, it prints the bogus text verbatim as it does currently. However, this is messy and introduces a form of parsing logic into the formatter that is not meaningful.

Another option is to introduce some form of “syntactically-valid bogus node” into the parser, which accepts these kinds of purely semantic errors (duplicate modifiers, abstract properties in non-abstract classes).

It would continue to build the nodes like normal (effectively matching the behavior in Prettier) but store them inside of a new kind of bogus node, including the diagnostics along with it.
When formatting, these particular bogus nodes would just attempt to format the inner node and then fallback if there’s an error (the existing `format_or_verbatim`

utility would do this already).
This keeps the parsing and formatting logic separate from each other but introduces more complexity to the parser, allowing invalid states to be considered semi-valid.

### Duplicate modifiers on class properties

Section titled “Duplicate modifiers on class properties”Input

Diff

### Assignment to an optional chain

Section titled “Assignment to an optional chain”Input

Diff

### Incorrect modifier for the type parameters of an interface

Section titled “Incorrect modifier for the type parameters of an interface”Input

Diff

### Top-level return

Section titled “Top-level return”### Erroneous self-increment and self-decrement

Section titled “Erroneous self-increment and self-decrement”Input

### Use of `abstract`

modifier in non-abstract classes

Section titled “Use of abstract modifier in non-abstract classes”Input

Diff

## Prettier has inconsistencies between TypeScript and Babel parsing

Section titled “Prettier has inconsistencies between TypeScript and Babel parsing”Prettier supports a number of different parsers for JavaScript and TypeScript code, all of which are meant to be compatible with the `estree`

spec. Most of the time, Prettier uses Babel as the default parser for JavaScript code, but when parsing TypeScript, it will try to use TypeScript’s own parser first and only fall back to Babel with TypeScript enabled afterward. While the TypeScript parser is generally compatible with `estree`

, it’s not exact, and this can lead to some inconsistencies that affect the output that Prettier creates. In general, these are considered bugs in Prettier itself, since the output should be the same regardless of which parser is used.

Biome implements its own parsing that handles all forms of JavaScript and TypeScript code, meaning there should not be any inconsistencies between the two. However, when migrating a TypeScript codebase from Prettier to Biome, it’s possible that some formatting will appear to have changed because of those discrepancies between parsers from Prettier.

These cases are not considered bugs or incompatibilities in Biome. If formatted code only appears different using the `typescript`

parser setting in Prettier, but matches when using `babel`

and/or `babel-ts`

, then Biome considers the output to be compatible.

As an example, consider this case, formatted using Biome and Prettier 3.1.0 with the `typescript`

parser:

Input

Diff

Prettier with the TypeScript parser chooses to write the `isEqual`

call on a single line, while Biome matches the output of Prettier with the `babel`

and `babel-ts`

parsers. As such, this is *not* considered an incompatibility with Biome and is instead considered a bug in Prettier.

Copyright (c) 2023-present Biome Developers and Contributors.
