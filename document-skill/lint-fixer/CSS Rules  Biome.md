# CSS Rules

Below the list of rules supported by Biome, divided by group. Here’s a legend of the emojis:

- The icon indicates that the rule is part of the recommended rules.
- The icon indicates that the rule provides a code action (fix) that is
**safe**to apply. - The icon indicates that the rule provides a code action (fix) that is
**unsafe**to apply. - The icon indicates that the rule has been implemented and scheduled for the next release.

| Rule name | Description | Properties |
|---|---|---|
| useGenericFontNames | Disallow a missing generic family keyword within font families. |

`complexity`

Section titled “complexity”| Rule name | Description | Properties |
|---|---|---|
| noImportantStyles | Disallow the use of the `!important` style. |

`correctness`

Section titled “correctness”| Rule name | Description | Properties |
|---|---|---|
| noInvalidDirectionInLinearGradient | Disallow non-standard direction values for linear gradient functions. | |
| noInvalidGridAreas | Disallows invalid named grid areas in CSS Grid Layouts. | |
| noInvalidPositionAtImportRule | Disallow the use of `@import` at-rules in invalid positions. | |
| noMissingVarFunction | Disallow missing var function for css variables. | |
| noUnknownFunction | Disallow unknown CSS value functions. | |
| noUnknownMediaFeatureName | Disallow unknown media feature names. | |
| noUnknownProperty | Disallow unknown properties. | |
| noUnknownPseudoClass | Disallow unknown pseudo-class selectors. | |
| noUnknownPseudoElement | Disallow unknown pseudo-element selectors. | |
| noUnknownTypeSelector | Disallow unknown type selectors. | |
| noUnknownUnit | Disallow unknown CSS units. | |
| noUnmatchableAnbSelector | Disallow unmatchable An+B selectors. |

`nursery`

Section titled “nursery”| Rule name | Description | Properties |
|---|---|---|
| noDeprecatedMediaType | Disallow deprecated media types. | |
| noDuplicateSelectors | Disallow duplicate selectors. | |
| noExcessiveLinesPerFile | Restrict the number of lines in a file. | |
| noExcessiveSelectorClasses | Limit the number of classes in a selector. | |
| noHexColors | Disallow hex colors. | |
| useBaseline | Disallow CSS properties, values, at-rules, functions, and selectors that are not part of the configured Baseline. |

| Rule name | Description | Properties |
|---|---|---|
| noDescendingSpecificity | Disallow a lower specificity selector from coming after a higher specificity selector. | |
| noValueAtRule | Disallow use of `@value` rule in CSS modules. |

`suspicious`

Section titled “suspicious”| Rule name | Description | Properties |
|---|---|---|
| noDuplicateAtImportRules | Disallow duplicate `@import` rules. | |
| noDuplicateCustomProperties | Disallow duplicate custom properties within declaration blocks. | |
| noDuplicateFontNames | Disallow duplicate names within font families. | |
| noDuplicateProperties | Disallow duplicate properties within declaration blocks. | |
| noDuplicateSelectorsKeyframeBlock | Disallow duplicate selectors within keyframe blocks. | |
| noEmptyBlock | Disallow CSS empty blocks. | |
| noEmptySource | Disallow empty sources. | |
| noImportantInKeyframe | Disallow invalid `!important` within keyframe declarations | |
| noIrregularWhitespace | Disallows the use of irregular whitespace characters. | |
| noShorthandPropertyOverrides | Disallow shorthand properties that override related longhand properties. | |
| noUnknownAtRules | Disallow unknown at-rules. | |
| noUselessEscapeInString | Disallow unnecessary escapes in string literals. |

## Recommended rules

Section titled “Recommended rules”- useGenericFontNames (Severity: error)
- noImportantStyles (Severity: warning)
- noInvalidDirectionInLinearGradient (Severity: error)
- noInvalidGridAreas (Severity: error)
- noInvalidPositionAtImportRule (Severity: error)
- noMissingVarFunction (Severity: error)
- noUnknownFunction (Severity: error)
- noUnknownMediaFeatureName (Severity: error)
- noUnknownProperty (Severity: error)
- noUnknownPseudoClass (Severity: error)
- noUnknownPseudoElement (Severity: error)
- noUnknownTypeSelector (Severity: error)
- noUnknownUnit (Severity: error)
- noUnmatchableAnbSelector (Severity: error)
- noDescendingSpecificity (Severity: warning)
- noDuplicateAtImportRules (Severity: error)
- noDuplicateCustomProperties (Severity: error)
- noDuplicateFontNames (Severity: error)
- noDuplicateProperties (Severity: error)
- noDuplicateSelectorsKeyframeBlock (Severity: error)
- noEmptyBlock (Severity: warning)
- noImportantInKeyframe (Severity: error)
- noIrregularWhitespace (Severity: warning)
- noShorthandPropertyOverrides (Severity: error)
- noUnknownAtRules (Severity: error)
- noUselessEscapeInString (Severity: warning)

Missing a rule? Help us by contributing to the analyzer or create a rule suggestion here.

Copyright (c) 2023-present Biome Developers and Contributors.
