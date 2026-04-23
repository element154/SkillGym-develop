# HTML Rules

Below the list of rules supported by Biome, divided by group. Here’s a legend of the emojis:

- The icon indicates that the rule is part of the recommended rules.
- The icon indicates that the rule provides a code action (fix) that is
**safe**to apply. - The icon indicates that the rule provides a code action (fix) that is
**unsafe**to apply. - The icon indicates that the rule has been implemented and scheduled for the next release.

| Rule name | Description | Properties |
|---|---|---|
| noAccessKey | Enforce that the `accesskey` attribute is not used on any HTML element. | |
| noAutofocus | Enforce that the `autofocus` attribute is not used on elements. | |
| noDistractingElements | Enforces that no distracting elements are used. | |
| noHeaderScope | The scope prop should be used only on `<th>` elements. | |
| noPositiveTabindex | Prevent the usage of positive integers on `tabindex` attribute. | |
| noRedundantAlt | Enforce `img` alt prop does not contain the word “image”, “picture”, or “photo”. | |
| noSvgWithoutTitle | Enforces the usage of the `title` element for the `svg` element. | |
| useAltText | Enforce that all elements that require alternative text have meaningful information to relay back to the end user. | |
| useAnchorContent | Enforce that anchors have content and that the content is accessible to screen readers. | |
| useAriaPropsForRole | Enforce that elements with ARIA roles must have all required ARIA attributes for that role. | |
| useButtonType | Enforces the usage and validity of the attribute `type` for the element `button` | |
| useHtmlLang | Enforce that `html` element has `lang` attribute. | |
| useIframeTitle | Enforces the usage of the attribute `title` for the element `iframe` . | |
| useMediaCaption | Enforces that `audio` and `video` elements must have a `track` for captions. | |
| useValidAriaRole | Elements with ARIA roles must use a valid, non-abstract ARIA role. | |
| useValidLang | Ensure that the attribute passed to the `lang` attribute is a correct ISO language and/or country. |

`nursery`

Section titled “nursery”| Rule name | Description | Properties |
|---|---|---|
| noAmbiguousAnchorText | Disallow ambiguous anchor descriptions. | |
| noDuplicateAttributes | Disallow duplication of attributes. | |
| noInlineStyles | Disallow the use of inline styles. | |
| noScriptUrl | Disallow `javascript:` URLs in HTML. | |
| noSyncScripts | Prevent the usage of synchronous scripts. | |
| noVueVIfWithVFor | Disallow using `v-if` and `v-for` directives on the same element. | |
| useScopedStyles | Enforce that `<style>` blocks in Vue SFCs have the `scoped` attribute and that `<style>` blocks in Astro components do not have the `is:global` directive. | |
| useVueConsistentVBindStyle | Enforce a consistent style for `v-bind` in Vue templates. | |
| useVueConsistentVOnStyle | Enforce a consistent style for `v-on` in Vue templates. | |
| useVueHyphenatedAttributes | Enforce hyphenated (kebab-case) attribute names in Vue templates. | |
| useVueVForKey | Enforce that elements using `v-for` also specify a unique `key` . | |
| useVueValidTemplateRoot | Enforce valid Vue `<template>` root usage. | |
| useVueValidVBind | Forbids `v-bind` directives with missing values or invalid modifiers. | |
| useVueValidVCloak | Enforce valid `v-cloak` Vue directives. | |
| useVueValidVElse | Enforce valid usage of v-else. | |
| useVueValidVElseIf | Enforce valid `v-else-if` directives. | |
| useVueValidVHtml | Enforce valid `v-html` directives. | |
| useVueValidVIf | Enforces valid `v-if` usage for Vue templates. | |
| useVueValidVOn | Enforce valid `v-on` directives with proper arguments, modifiers, and handlers. | |
| useVueValidVOnce | Enforce valid `v-once` Vue directives. | |
| useVueValidVPre | Enforce valid `v-pre` Vue directives. | |
| useVueValidVText | Enforce valid `v-text` Vue directives. | |
| useVueVapor | Enforce opting in to Vue Vapor mode in `<script setup>` blocks. |

## Recommended rules

Section titled “Recommended rules”- noAccessKey (Severity: error)
- noAutofocus (Severity: error)
- noDistractingElements (Severity: error)
- noHeaderScope (Severity: error)
- noPositiveTabindex (Severity: error)
- noRedundantAlt (Severity: error)
- noSvgWithoutTitle (Severity: error)
- useAltText (Severity: error)
- useAnchorContent (Severity: error)
- useAriaPropsForRole (Severity: error)
- useButtonType (Severity: error)
- useHtmlLang (Severity: error)
- useIframeTitle (Severity: error)
- useMediaCaption (Severity: error)
- useValidAriaRole (Severity: error)
- useValidLang (Severity: error)

Missing a rule? Help us by contributing to the analyzer or create a rule suggestion here.

Copyright (c) 2023-present Biome Developers and Contributors.
