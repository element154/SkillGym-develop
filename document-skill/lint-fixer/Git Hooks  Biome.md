# Git Hooks

Git allows executing scripts during the run of a git command using Git Hooks. For example, you can format and lint the staged files before committing or pushing. Several tools exist to simplify the management of Git Hooks. In the following sections we introduce some of them and how they can be used with Biome.

## Lefthook

Section titled “Lefthook”Lefthook provides a fast, cross-platform, and dependency-free hook manager. It can be installed via NPM.

Add a file named `lefthook.yml`

at the root of your Git repository.
Some examples of *Lefthook* configurations:

-
Check formatting and lint before committing

-
Format, lint, and apply safe code fixes before committing

`stage_fixed: true`

adds again the staged files. -
Check formatting and lint before pushing

Note that you don’t need to use both `glob`

and `--files-ignore-unknown=true`

.
Using only `--files-ignore-unknown=true`

allows handling files supported in the present and in the future by Biome.
If you wish more control over which files are handled, you should use `glob`

.

`--no-errors-on-unmatched`

silents possible errors in case *no files are processed*.

Once configured, run `lefthook install`

to set up the hooks.

Husky is a widely-used hook manager in the JavaScript ecosystem.
Husky doesn’t hide unstaged changes and is not able to provide the list of staged files.
This is why it is often used in tandem with another tool such as *lint-staged* or *git-format-staged*.

If your project contains a `package.json`

,
you can automatically set up *husky* hooks upon package installation using `scripts.prepare`

:

### lint-staged

Section titled “lint-staged”lint-staged is one of the most used tools in the JavaScript ecosystem.

Add the following husky configuration:

The configuration of lint-staged is directly embedded in `package.json`

.
Here’s some example of commands that you could find useful when running the Git hooks:

Remember to use the CLI option `--no-errors-on-unmatched`

in your command, to silent possible errors in case *no files are processed*.

### git-format-staged

Section titled “git-format-staged”In contrast to other tools such as *lefthook*, *pre-commit*, and *lint-staged*,
git-format-staged doesn’t use `git stash`

internally.
This avoids manual intervention when conflicts arise between unstaged changes and updated staged changes.
See the comparison of *git-format-staged* with other tools.

Some examples of configuration:

-
Check formatting and lint before committing

-
Format, lint, and apply safe code fixes before committing

## pre-commit

Section titled “pre-commit”pre-commit provides a multi-language hook manager. Biome provides four pre-commit hooks via the biomejs/pre-commit repository.

hook `id` | description |
|---|---|
`biome-ci` | Check formatting, check if imports are organized, and lints |
`biome-check` | Format, organize imports, lint, and apply safe fixes to the committed files |
`biome-format` | Format the committed files |
`biome-lint` | Lint and apply safe fixes to the committed files |

In the following example, we assume that you installed pre-commit and run `pre-commit install`

in your repository.
if you want to use the `biome-check`

hook, add the following pre-commit configuration to the root of your project in a file named `.pre-commit-config.yaml`

:

This will run `biome check --write`

when you run `git commit`

.

Note that you must specify which version of Biome to use thanks to the `additional_dependencies`

option.
pre-commit separately installs tools and need to know which one to install.

If Biome is already installed as a `npm`

package in your local repository,
then it can be a burden to update both `package.json`

and `.pre-commit-config.yaml`

when you update Biome.
Instead of using the provided Biome hooks, you can specify your own local hook.

For example, if you use `npm`

, you can write the following hook in `.pre-commit-config.yaml`

:

The pre-commit option `files`

is optional,
because Biome is able to ignore unknown files (using the option `--files-ignore-unknown=true`

).

## Shell script

Section titled “Shell script”You can also use a custom shell script. Note that you can encounter cross-platform incompatibilities. We recommend the use of a dedicated tool as the one presented in the previous sections.

Some examples of shells scripts:

-
Check formatting and lint before committing

-
Format, lint, and apply safe code fixes before committing

Note that we make the hook fail if staged files have unstaged changes.

Copyright (c) 2023-present Biome Developers and Contributors.
