# useFlatMap

## Summary

Section titled “Summary”- Rule available since:
`v1.0.0`

- Diagnostic Category:
`lint/complexity/useFlatMap`

- This rule is
**recommended**, meaning it is enabled by default. - This rule has a
**safe**fix. - The default severity of this rule is
**information**. - Sources:
- Same as
`unicorn/prefer-array-flat-map`

- Same as
`map_flatten`

- Same as

## How to configure

Section titled “How to configure”## Description

Section titled “Description”Promotes the use of `.flatMap()`

when `map().flat()`

are used together.

## Examples

Section titled “Examples”### Invalid

Section titled “Invalid”`code-block.js:2:1 lint/complexity/useFlatMap FIXABLE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`

**ℹ** The call chain **.map().flat()** can be replaced with a single **.flatMap()** call.

**1 │ **const array = [“split”, “the text”, “into words”];

**>** **2 │ **array.map(sentence => sentence.split(’ ‘)).flat();

** │ ****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^**

**3 │ **

**ℹ** Safe fix: Replace the chain with **.flatMap()**.

**1** **1**** │ ** const array = [“split”, “the text”, “into words”];

**2** ** │ **- **a****r****r****a****y****.****m****a****p**(sentence·=>·sentence.split(’·‘**)**)**.****f****l****a****t****(**);

**2**** │ **+ **a****r****r****a****y****.****f****l****a****t****M****a****p**(sentence·=>·sentence.split(’·’));

**3** **3**** │ **

`code-block.js:2:1 lint/complexity/useFlatMap FIXABLE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`

**ℹ** The call chain **.map().flat()** can be replaced with a single **.flatMap()** call.

**1 │ **const array = [“split”, “the text”, “into words”];

**>** **2 │ **array.map(sentence => sentence.split(’ ‘)).flat(1);

** │ ****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^****^**

**3 │ **

**ℹ** Safe fix: Replace the chain with **.flatMap()**.

**1** **1**** │ ** const array = [“split”, “the text”, “into words”];

**2** ** │ **- **a****r****r****a****y****.****m****a****p**(sentence·=>·sentence.split(’·‘)**)****.****f****l****a****t****(****1**);

**2**** │ **+ **a****r****r****a****y****.****f****l****a****t****M****a****p**(sentence·=>·sentence.split(’·’));

**3** **3**** │ **

## Related links

Section titled “Related links”Copyright (c) 2023-present Biome Developers and Contributors.
