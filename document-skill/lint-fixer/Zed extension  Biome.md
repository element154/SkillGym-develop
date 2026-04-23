# Zed extension

## Installation

Section titled “Installation”Requires Zed >= **v0.131.0**.

This extension is available in the extensions view inside the Zed editor. Open `zed: extensions`

and search for *Biome*. It runs the Biome binary under the hood and checks for Biome installations in the following order:

- Path specified in Zed’s configuration, for example like this:

- Locally installed Biome via
`package.json`

- System-wide installed Biome in
`PATH`

If neither exists, it will ask Zed to install Biome using `npm`

and use that.

## Configuration

Section titled “Configuration”`config_path`

Section titled “config_path”By default, the configuration file is required to be in the **root of the workspace**.

Otherwise, it can be configured through the lsp settings:

`require_config_file`

Section titled “require_config_file”It enables Biome only if the project contains a configuration file:

Default:

`false`

`inline_config`

Section titled “inline_config”An inline version of the Biome configuration. The options of this configuration will override the options coming from any `biome.json`

file read from disk (or the defaults).

For example, let’s say your project enables the rule `noConsole`

with `error`

severity:

However, during local development, you want to disable this rule because it’s useful and you don’t want to see red squiggles. In your `inline_config`

, you would write something like the following:

## Formatting

Section titled “Formatting”To use the language server as a formatter, specify biome as your formatter in the settings:

See Language Support for more information.

### Enable biome only when biome.json is present

Section titled “Enable biome only when biome.json is present”### Run code actions on format:

Section titled “Run code actions on format:”If you want to apply unsafe fixes on save, you must make the code fix of the rule safe.

### Project-based configuration

Section titled “Project-based configuration”You can include these settings in Zed Project Settings (`.zed/settings.json`

) at the root of your project folder or as Zed User Settings (`~/.config/zed/settings.json`

) which will apply to all projects by default.

#### Disable biome for a particular project

Section titled “Disable biome for a particular project”You can exclude biome for a given language (e.g. GraphQL) on project with:

### Global Settings

Section titled “Global Settings”It is not recommended to add `biome`

to top-level `language_servers`

, `formatter`

or `code_actions_on_format`

keys in your Zed setting.json. Specifying biome as `language_server`

or `formatter`

globally may break functionality for languages that biome does not support (Rust, Python, etc). See language support for a complete list of supported languages.

This documentation previously recommended global settings; please switch your Zed settings to explicitly configure biome on a per language basis.

Copyright (c) 2023-present Biome Developers and Contributors.
