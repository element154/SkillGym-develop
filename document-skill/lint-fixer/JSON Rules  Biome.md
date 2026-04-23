# JSON Rules

Below the list of rules supported by Biome, divided by group. Here’s a legend of the emojis:

- The icon indicates that the rule is part of the recommended rules.
- The icon indicates that the rule provides a code action (fix) that is
**safe**to apply. - The icon indicates that the rule provides a code action (fix) that is
**unsafe**to apply. - The icon indicates that the rule has been implemented and scheduled for the next release.

`nursery`

Section titled “nursery”| Rule name | Description | Properties |
|---|---|---|
| noEmptyObjectKeys | Disallow empty keys in JSON objects. | |
| noTopLevelLiterals | Require the JSON top-level value to be an array or object. | |
| noUntrustedLicenses | Disallow dependencies with untrusted licenses. | |
| useRequiredScripts | Enforce the presence of required scripts in package.json. |

`suspicious`

Section titled “suspicious”| Rule name | Description | Properties |
|---|---|---|
| noBiomeFirstException | Prevents the misuse of glob patterns inside the `files.includes` field. | |
| noDuplicateDependencies | Prevent the listing of duplicate dependencies. | |
| noDuplicateObjectKeys | Disallow two keys with the same name inside objects. | |
| noQuickfixBiome | Disallow the use if `quickfix.biome` inside editor settings file. | |
| useBiomeIgnoreFolder | Promotes the correct usage for ignoring folders in the configuration file. |

## Recommended rules

Section titled “Recommended rules”- noBiomeFirstException (Severity: error)
- noDuplicateObjectKeys (Severity: error)
- noQuickfixBiome (Severity: information)
- useBiomeIgnoreFolder (Severity: warning)

Missing a rule? Help us by contributing to the analyzer or create a rule suggestion here.

Copyright (c) 2023-present Biome Developers and Contributors.
