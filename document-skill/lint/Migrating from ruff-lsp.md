# Migrating from `ruff-lsp`

`ruff-lsp`

is the Language Server Protocol implementation for Ruff to power the editor
integrations. It is written in Python and is a separate package from Ruff itself. The **native
server**, however, is the Language Server Protocol implementation which is **written in Rust** and
is available under the `ruff server`

command. This guide is intended to help users migrate from
`ruff-lsp`

to the native server.

Note

The native server was first introduced in Ruff version `0.3.5`

. It was marked as beta in
version `0.4.5`

and officially stabilized in version
`0.5.3`

. It is recommended to use the
latest version of Ruff to ensure the best experience.

The migration process involves any or all of the following:

- Migrate deprecated settings to the new settings
- Remove settings that are no longer supported
- Update the
`ruff`

version

Read on to learn more about the unsupported or new settings, or jump to the examples that enumerate some of the common settings and how to migrate them.

## Unsupported Settings

The following `ruff-lsp`

settings are not supported by the native server:

`lint.run`

: This setting is no longer relevant for the native language server, which runs on every keystroke by default.`lint.args`

,`format.args`

: These settings have been replaced by more granular settings in the native server like`lint.select`

,`format.preview`

, etc. along with the ability to override any configuration using the`configuration`

setting.

The following settings are not accepted by the language server but are still used by the VS Code extension. Refer to their respective documentation for more information on how each is used by the extension:

## Removed Settings

Additionally, the following settings are not supported by the native server and should be removed:

## New Settings

The native server introduces several new settings that `ruff-lsp`

does not have:

`configuration`

`configurationPreference`

`exclude`

`format.preview`

`lineLength`

`lint.select`

`lint.extendSelect`

`lint.ignore`

`lint.preview`

## Examples

All of the examples mentioned below are only valid for the VS Code extension. For other editors, please refer to their respective documentation sections in the settings page.

### Configuration file

If you've been providing a configuration file as shown below:

```
{
"ruff.lint.args": "--config ~/.config/custom_ruff_config.toml",
"ruff.format.args": "--config ~/.config/custom_ruff_config.toml"
}
```

You can migrate to the new server by using the `configuration`

setting
like below which will apply the configuration to both the linter and the formatter:

`lint.args`

If you're providing the linter flags by using `ruff.lint.args`

like so:

You can migrate to the new server by using the `lint.select`

and
`configuration`

setting like so:

```
{
"ruff.lint.select": ["E", "F"],
"ruff.configuration": {
"unsafe-fixes": true,
"lint": {
"unfixable": ["F401"]
}
}
}
```

The following options can be set directly in the editor settings:

The remaining options can be set using the `configuration`

setting.

`format.args`

If you're also providing formatter flags by using `ruff.format.args`

like so:

You can migrate to the new server by using the `lineLength`

and
`configuration`

setting like so:

The following options can be set directly in the editor settings:

The remaining options can be set using the `configuration`

setting.
