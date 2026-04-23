# Continuous Integration

Running Biome in a CI environment is easy. Check out the following examples for some inspiration.

`biome check`

VS `biome ci`

Section titled “biome check VS biome ci”Biome offers two CLI commands to run all checks: `biome check`

and `biome ci`

, however the latter should be used in CI (Continuous Integration) environments.

Compared to the `check`

command, the `ci`

command:

- Doesn’t provide any
`--write`

/`--fix`

option. - Integrates better with specific runners. For example, when run on GitHub, the diagnostics are printed using the GitHub annotations.
- Allows controlling the number of threads.
- When VCS integration is enabled, it uses the
`--changed`

flag instead of`--staged`

, because a remote repository doesn’t have the concept of “staged files”.

With time, the `ci`

command will receive more and more features.

## GitHub Actions

Section titled “GitHub Actions”We provide a first-party GitHub Action to setup Biome in your runner. Here’s what a simple workflow might look like:

If your Biome configuration has external dependencies (e.g., extends a config from a package), you’ll need to setup Node.js and install dependencies using your preferred package manager before running Biome:

### Third-party actions

Section titled “Third-party actions”These are actions maintained by other communities, that you use in your runner:

- reviewdog-action-biome: run Biome with reviewdog and make comments and commit suggestions on the pull request.

## GitLab CI

Section titled “GitLab CI”Below is an example configuration:

Copyright (c) 2023-present Biome Developers and Contributors.
