# Settings

The Ruff Language Server provides a set of configuration options to customize its behavior
along with the ability to use an existing `pyproject.toml`

or `ruff.toml`

file to configure the
linter and formatter. This is done by providing these settings while initializing the server.
VS Code provides a UI to configure these settings, while other editors may require manual
configuration. The setup section provides instructions on where to place these settings
as per the editor.

## Top-level

`configuration`

The `configuration`

setting allows you to configure editor-specific Ruff behavior. This can be done
in one of the following ways:

**Configuration file path:**Specify the path to a`ruff.toml`

or`pyproject.toml`

file that contains the configuration. User home directory and environment variables will be expanded.**Inline JSON configuration:**Directly provide the configuration as a JSON object.

Added in Ruff `0.9.8`

The **Inline JSON configuration** option was introduced in Ruff `0.9.8`

.

The default behavior, if `configuration`

is unset, is to load the settings from the project's
configuration (a `ruff.toml`

or `pyproject.toml`

in the project's directory), consistent with when
running Ruff on the command-line.

The `configurationPreference`

setting controls the precedence if both an
editor-provided configuration (`configuration`

) and a project level configuration file are present.

#### Resolution order

In an editor, Ruff supports three sources of configuration, prioritized as follows (from highest to lowest):

**Specific settings:**Individual settings like`lineLength`

or`lint.select`

defined in the editor: Settings provided via the`ruff.configuration`

`configuration`

field (either a path to a configuration file or an inline configuration object)**Configuration file:**Settings defined in a`ruff.toml`

or`pyproject.toml`

file in the project's directory (if present)

For example, if the line length is specified in all three sources, Ruff will use the value from the
`lineLength`

setting.

**Default value**: `null`

**Type**: `string`

**Example usage**:

*Using configuration file path:*

*Using inline configuration:*

```
require('lspconfig').ruff.setup {
init_options = {
settings = {
configuration = {
lint = {
unfixable = {"F401"},
["extend-select"] = {"TID251"},
["flake8-tidy-imports"] = {
["banned-api"] = {
["typing.TypedDict"] = {
msg = "Use `typing_extensions.TypedDict` instead"
}
}
}
},
format = {
["quote-style"] = "single"
}
}
}
}
}
```

```
{
"lsp": {
"ruff": {
"initialization_options": {
"settings": {
"configuration": {
"lint": {
"unfixable": ["F401"],
"extend-select": ["TID251"],
"flake8-tidy-imports": {
"banned-api": {
"typing.TypedDict": {
"msg": "Use `typing_extensions.TypedDict` instead"
}
}
}
},
"format": {
"quote-style": "single"
}
}
}
}
}
}
}
```

`configurationPreference`

The strategy to use when resolving settings across VS Code and the filesystem. By default, editor
configuration is prioritized over `ruff.toml`

and `pyproject.toml`

files.

`"editorFirst"`

: Editor settings take priority over configuration files present in the workspace.`"filesystemFirst"`

: Configuration files present in the workspace takes priority over editor settings.`"editorOnly"`

: Ignore configuration files entirely i.e., only use editor settings.

**Default value**: `"editorFirst"`

**Type**: `"editorFirst" | "filesystemFirst" | "editorOnly"`

**Example usage**:

`exclude`

A list of file patterns to exclude from linting and formatting. See the documentation for more details.

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

`lineLength`

The line length to use for the linter and formatter.

**Default value**: `null`

**Type**: `int`

**Example usage**:

`fixAll`

Whether to register the server as capable of handling `source.fixAll`

code actions.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`organizeImports`

Whether to register the server as capable of handling `source.organizeImports`

code actions.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`showSyntaxErrors`

*New in Ruff v0.5.0*

Whether to show syntax error diagnostics.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`logLevel`

The log level to use for the server.

**Default value**: `"info"`

**Type**: `"trace" | "debug" | "info" | "warn" | "error"`

**Example usage**:

`logFile`

Path to the log file to use for the server.

If not set, logs will be written to stderr.

**Default value**: `null`

**Type**: `string`

**Example usage**:

`codeAction`

Enable or disable code actions provided by the server.

`disableRuleComment.enable`

Whether to display Quick Fix actions to disable rules via `noqa`

suppression comments.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`fixViolation.enable`

Whether to display Quick Fix actions to autofix violations.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`lint`

Settings specific to the Ruff linter.

`enable`

Whether to enable linting. Set to `false`

to use Ruff exclusively as a formatter.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`preview`

Whether to enable Ruff's preview mode when linting.

**Default value**: `null`

**Type**: `bool`

**Example usage**:

`select`

Rules to enable by default. See the documentation.

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

`extendSelect`

Rules to enable in addition to those in `lint.select`

.

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

`ignore`

Rules to disable by default. See the documentation.

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

`format`

Settings specific to the Ruff formatter.

`preview`

Whether to enable Ruff's preview mode when formatting.

**Default value**: `null`

**Type**: `bool`

**Example usage**:

`backend`

The backend to use for formatting files. Following options are available:

`"internal"`

: Use the built-in Ruff formatter`"uv"`

: Use uv for formatting (requires uv >= 0.8.13)

For `internal`

, the formatter version will match the selected Ruff version while for `uv`

, the
formatter version may differ.

**Default value**: `"internal"`

**Type**: `"internal" | "uv"`

**Example usage**:

## VS Code specific

Additionally, the Ruff extension provides the following settings specific to VS Code. These settings are not used by the language server and are only relevant to the extension.

`enable`

Whether to enable the Ruff extension. Modifying this setting requires restarting VS Code to take effect.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`format.args`

Deprecated

This setting is only used by `ruff-lsp`

which is
deprecated in favor of the native language server. Refer to the migration
guide for more information.

**This setting is not used by the native language server.**

Additional arguments to pass to the Ruff formatter.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

`ignoreStandardLibrary`

Deprecated

This setting is only used by `ruff-lsp`

which is
deprecated in favor of the native language server. Refer to the migration
guide for more information.

**This setting is not used by the native language server.**

Whether to ignore files that are inferred to be part of the Python standard library.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

`importStrategy`

Strategy for loading the `ruff`

executable.

`fromEnvironment`

finds Ruff in the environment, falling back to the bundled version`useBundled`

uses the version bundled with the extension

**Default value**: `"fromEnvironment"`

**Type**: `"fromEnvironment" | "useBundled"`

**Example usage**:

`interpreter`

A list of paths to Python interpreters. Even though this is a list, only the first interpreter is used.

This setting depends on the `ruff.nativeServer`

setting:

- If using the native server, the interpreter is used to find the
`ruff`

executable when`ruff.importStrategy`

is set to`fromEnvironment`

. - Otherwise, the interpreter is used to run the
`ruff-lsp`

server.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

`lint.args`

Deprecated

This setting is only used by `ruff-lsp`

which is
deprecated in favor of the native language server. Refer to the migration
guide for more information.

**This setting is not used by the native language server.**

Additional arguments to pass to the Ruff linter.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

`lint.run`

Deprecated

`ruff-lsp`

which is
deprecated in favor of the native language server. Refer to the migration
guide for more information.

**This setting is not used by the native language server.**

Run Ruff on every keystroke (`onType`

) or on save (`onSave`

).

**Default value**: `"onType"`

**Type**: `"onType" | "onSave"`

**Example usage**:

`nativeServer`

Whether to use the native language server, `ruff-lsp`

or
automatically decide between the two based on the Ruff version and extension settings.

`"on"`

: Use the native language server. A warning will be displayed if deprecated settings are detected.`"off"`

: Use`ruff-lsp`

. A warning will be displayed if settings specific to the native server are detected.`"auto"`

: Automatically select between the native language server and`ruff-lsp`

based on the following conditions:`true`

: Same as`on`

`false`

: Same as`off`

**Default value**: `"auto"`

**Type**: `"on" | "off" | "auto" | true | false`

**Example usage**:

`path`

A list of path to `ruff`

executables.

The first executable in the list which is exists is used. This setting takes precedence over the
`ruff.importStrategy`

setting.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

`showNotifications`

Deprecated

`ruff-lsp`

which is
deprecated in favor of the native language server. Refer to the migration
guide for more information.

Setting to control when a notification is shown.

**Default value**: `"off"`

**Type**: `"off" | "onError" | "onWarning" | "always"`

**Example usage**:

`trace.server`

The trace level for the language server. Refer to the LSP specification for more information.

**Default value**: `"off"`

**Type**: `"off" | "messages" | "verbose"`

**Example usage**:
