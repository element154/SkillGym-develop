# GraphQL Rules

Below the list of rules supported by Biome, divided by group. Here’s a legend of the emojis:

- The icon indicates that the rule is part of the recommended rules.
- The icon indicates that the rule provides a code action (fix) that is
**safe**to apply. - The icon indicates that the rule provides a code action (fix) that is
**unsafe**to apply. - The icon indicates that the rule has been implemented and scheduled for the next release.

`correctness`

Section titled “correctness”| Rule name | Description | Properties |
|---|---|---|
| useGraphqlNamedOperations | Enforce specifying the name of GraphQL operations. |

`nursery`

Section titled “nursery”| Rule name | Description | Properties |
|---|---|---|
| noDuplicateArgumentNames | Require all argument names for fields & directives to be unique. | |
| noDuplicateEnumValueNames | Require all enum value names to be unique. | |
| noDuplicateFieldDefinitionNames | Require all fields of a type to be unique. | |
| noDuplicateGraphqlOperationName | Enforce unique operation names across a GraphQL document. | |
| noDuplicateInputFieldNames | Require fields within an input object to be unique. | |
| noDuplicateVariableNames | Require all variable definitions to be unique. | |
| noExcessiveLinesPerFile | Restrict the number of lines in a file. | |
| noRootType | Disallow the usage of specified root types | |
| useConsistentGraphqlDescriptions | Require all descriptions to follow the same style (either block or inline) to maintain consistency and improve readability across the schema. | |
| useInputName | Require mutation argument to be always called “input” | |
| useLoneAnonymousOperation | Disallow anonymous operations when more than one operation specified in document. | |
| useLoneExecutableDefinition | Require queries, mutations, subscriptions or fragments each to be located in separate files. |

| Rule name | Description | Properties |
|---|---|---|
| useDeprecatedReason | Require specifying the reason argument when using `@deprecated` directive | |
| useGraphqlNamingConvention | Validates that all enum values are capitalized. |

`suspicious`

Section titled “suspicious”| Rule name | Description | Properties |
|---|---|---|
| noDuplicateFields | No duplicated fields in GraphQL operations. | |
| noEmptySource | Disallow empty sources. | |
| useDeprecatedDate | Require the `@deprecated` directive to specify a deletion date. |

## Recommended rules

Section titled “Recommended rules”- useGraphqlNamedOperations (Severity: error)
- useDeprecatedReason (Severity: warning)
- noDuplicateFields (Severity: information)

Missing a rule? Help us by contributing to the analyzer or create a rule suggestion here.

Copyright (c) 2023-present Biome Developers and Contributors.
