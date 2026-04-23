# Linter Plugins

Biome Linter supports GritQL plugins. Currently, these plugins allow you to match specific code patterns and register customized diagnostic messages for them.

Here is an example of a plugin that reports on all usages of `Object.assign()`

:

You can put a GritQL snippet in a file anywhere in your project, but be mindful
you use the `.grit`

extension. Then, you can simply enable it as a plugin with
the following configuration:

The plugin will now be enabled on all supported files the linter runs on. You
can see its results when running `biome lint`

or `biome check`

. For example:

## Target Languages

Section titled “Target Languages”A GritQL snippet always attempts to match against a given *target language*.
If no target language is specified, JavaScript or one of its super languages is
assumed.

If you want to use a different target language, you must specify it explicitly.
For example, here is a CSS plugin to report any selector that sets a color
outside the allowed `.color-*`

classes:

We currently do not support other target languages than JavaScript and CSS.

## Plugin API

Section titled “Plugin API”In addition to Grit’s built-in functions, Biome currently supports one extra function:

`register_diagnostic()`

Section titled “register_diagnostic()”Registers a diagnostic to be reported whenever the pattern matches.

Supports three arguments:

`span`

(required): The syntax node to attach the diagnostic to. This is typically a variable that you matched within a code snippet.`message`

(required): The message to show with the diagnostic.`severity`

: The severity of the diagnostic. Allowed values are:`hint`

,`info`

,`warn`

, and`error`

. By default,`error`

is used.

Copyright (c) 2023-present Biome Developers and Contributors.
