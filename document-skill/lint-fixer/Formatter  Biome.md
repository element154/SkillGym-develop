# Formatter

Biome is an opinionated formatter that supports multiple languages. It follows a similar philosophy to Prettier, only supporting a few options to avoid debates over styles, turning into debates over Biome options. It deliberately resists the urge to add new options to prevent bike-shed discussions in teams so they can focus on what really matters instead.

The following command checks the formatting of the files in the `src`

directory.
It emits text differences if it finds code that is not formatted.

If you want to **apply** the new formatting, pass the `--write`

option:

The command accepts a list of files and directories.

For more information about all the available options, check the CLI reference.

## Options

Section titled “Options”Biome provides some options to tune the behavior of its formatter. Differently from other tools, Biome separates language-agnostic options from language-specific options.

The formatter options can be set on the CLI or via a Biome configuration file.
As of v1.9, Biome supports loading `.editorconfig`

files.

It’s recommended to use a Biome configuration file to ensure that both the Biome CLI and the Biome LSP apply the same options. The following defaults are applied:

The main language-agnostic options supported by the Biome formatter are:

- indent style (default:
`tab`

): Use spaces or tabs for indentation; - indent width (default:
`2`

): The number of spaces per indentation level. - line width (default:
`80`

): The column width at which Biome wraps code;

See the configuration reference for more details.

## Ignore Code

Section titled “Ignore Code”There are times when the formatted code isn’t ideal.

### Ignore an entire file

Section titled “Ignore an entire file”You can suppress (ignore) the formatter for an entire file by using the `biome-ignore-all format: reason`

comment **at the top of the file**:

For example, in JavaScript:

### Ignore nodes

Section titled “Ignore nodes”In case you want to suppress only a portion (node) of the code, use the suppression comment `biome-ignore format: reason`

Example:

Copyright (c) 2023-present Biome Developers and Contributors.
