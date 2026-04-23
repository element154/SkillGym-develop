# CLI

# Command summary

Section titled “Command summary”`biome`

↴`biome version`

↴`biome rage`

↴`biome start`

↴`biome stop`

↴`biome check`

↴`biome lint`

↴`biome format`

↴`biome ci`

↴`biome init`

↴`biome lsp-proxy`

↴`biome migrate`

↴`biome migrate prettier`

↴`biome migrate eslint`

↴`biome search`

↴`biome explain`

↴`biome clean`

↴

Biome official CLI. Use it to check the health of your project or run it to check single files.

**Usage**: `biome`

`COMMAND ...`

**Available options:**

,`-h`

— Prints help information`--help`

,`-V`

— Prints version information`--version`

**Available commands:**

— Shows the Biome version information and quit.`version`

— Prints information for debugging.`rage`

— Starts the Biome daemon server process.`start`

— Stops the Biome daemon server process.`stop`

— Runs formatter, linter and import sorting to the requested files.`check`

— Run various checks on a set of files.`lint`

— Run the formatter on a set of files.`format`

— Command to use in CI environments. Runs formatter, linter and import sorting to the requested files.`ci`

— Bootstraps a new biome project. Creates a configuration file with some defaults.`init`

— Acts as a server for the Language Server Protocol over stdin/stdout.`lsp-proxy`

— Updates the configuration when there are breaking changes.`migrate`

— EXPERIMENTAL: Searches for Grit patterns across a project.`search`

— Shows documentation of various aspects of the CLI.`explain`

— Cleans the logs emitted by the daemon.`clean`

## biome version

Section titled “biome version”Shows the Biome version information and quit.

**Usage**: `biome`

`version`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Available options:**

,`-h`

— Prints help information`--help`

## biome rage

Section titled “biome rage”Prints information for debugging.

**Usage**: `biome`

** rage** [

**] [**

`--daemon-logs`

**] [**

`--formatter`

**]**

`--linter`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Available options:**

— Prints the Biome daemon server logs`--daemon-logs`

— Prints the formatter options applied`--formatter`

— Prints the linter options applied`--linter`

,`-h`

— Prints help information`--help`

## biome start

Section titled “biome start”Starts the Biome daemon server process.

**Usage**: `biome`

** start** [

**=**

`--log-prefix-name`

*] [*

`STRING`

**=**

`--log-path`

*] [*

`PATH`

**=**

`--log-level`

*] [*

`<none|debug|info|warn|error>`

**=**

`--log-kind`

*] [*

`<pretty|compact|json>`

**=**

`--watcher-kind`

*] [*

`<polling|recommended|none>`

**=**

`--watcher-polling-interval`

*]*

`NUMBER`

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Controls various aspects of the Biome Daemon.**

-
=`--watcher-kind`

— Controls how the Biome file watcher should behave.`<polling|recommended|none>`

Uses environment variable

`BIOME_WATCHER_KIND`

[default: recommended]

-
=`--watcher-polling-interval`

— The polling interval in milliseconds. This is only applicable when using the polling watcher.`NUMBER`

Uses environment variable

`BIOME_WATCHER_POLLING_INTERVAL`

[default: 2000]

**Available options:**

,`-h`

— Prints help information`--help`

## biome stop

Section titled “biome stop”Stops the Biome daemon server process.

**Usage**: `biome`

`stop`

**Available options:**

,`-h`

— Prints help information`--help`

## biome check

Section titled “biome check”Runs formatter, linter and import sorting to the requested files.

**Usage**: `biome`

** check** [

**] [**

`--write`

**] [**

`--unsafe`

**=**

`--assist-enabled`

*] [*

`<true|false>`

**=**

`--enforce-assist`

*] [*

`<true|false>`

**=**

`--format-with-errors`

*] [*

`<true|false>`

**] [**

`--profile-rules`

**] [**

`--staged`

**] [**

`--changed`

**=**

`--since`

*] [*

`REF`

**=**

`--only`

*]… [*

`<GROUP|RULE|DOMAIN|ACTION>`

**=**

`--skip`

*]… [*

`<GROUP|RULE|DOMAIN|ACTION>`

*]…*

`PATH`

**Options that changes how the JSON parser behaves**

=`--json-parse-allow-comments`

— Allow parsing comments in`<true|false>`

`.json`

files=`--json-parse-allow-trailing-commas`

— Allow parsing trailing commas in`<true|false>`

`.json`

files

**The configuration that is contained inside the file biome.json**

-
=`--vcs-enabled`

— Whether Biome should integrate itself with the VCS client`<true|false>`

-
=`--vcs-client-kind`

— The kind of client.`<git>`

-
=`--vcs-use-ignore-file`

— Whether Biome should use the VCS ignore file. When [true], Biome will ignore the files specified in the ignore file.`<true|false>`

-
=`--vcs-root`

— The folder where Biome should check for VCS files. By default, Biome will use the same folder where`PATH`

`biome.json`

was found.If Biome can’t find the configuration, it will attempt to use the current working directory. If no current working directory can’t be found, Biome won’t use the VCS integration, and a diagnostic will be emitted

-
=`--vcs-default-branch`

— The main branch of the project`BRANCH`

-
=`--files-max-size`

— The maximum allowed size for source code files in bytes. Files above this limit will be ignored for performance reasons. Defaults to 1 MiB`NUMBER`

-
=`--files-ignore-unknown`

— Tells Biome to not emit diagnostics when handling files that it doesn’t know`<true|false>`

-
=`--format-with-errors`

— Whether formatting should be allowed to proceed if a given file has syntax errors`<true|false>`

-
=`--indent-style`

— The indent style.`<tab|space>`

-
=`--indent-width`

— The size of the indentation, 2 by default`NUMBER`

-
=`--line-ending`

— The type of line ending.`<lf|crlf|cr|auto>`

-
=`--line-width`

— What’s the max width of a line. Defaults to 80.`NUMBER`

-
=`--attribute-position`

— The attribute position style in HTML-ish languages. Defaults to auto.`<multiline|auto>`

-
=`--bracket-same-line`

— Put the`<true|false>`

`>`

of a multi-line HTML or JSX element at the end of the last line instead of being alone on the next line (does not apply to self closing elements). -
=`--bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

Setting this option to

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--use-editorconfig`

— Use any`<true|false>`

`.editorconfig`

files to configure the formatter. Configuration in`biome.json`

will override`.editorconfig`

configuration.Default:

`false`

. -
=`--jsx-everywhere`

— When enabled, files like`<true|false>`

`.js`

/`.mjs`

/`.cjs`

may contain JSX syntax.Defaults to

`true`

. -
=`--javascript-formatter-enabled`

— Control the formatter for JavaScript (and its super languages) files.`<true|false>`

-
=`--jsx-quote-style`

— The type of quotes used in JSX. Defaults to double.`<double|single>`

-
=`--quote-properties`

— When properties in objects are quoted. Defaults to asNeeded.`<preserve|as-needed>`

-
=`--trailing-commas`

— Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Defaults to “all”.`<all|es5|none>`

-
=`--semicolons`

— Whether the formatter prints semicolons for all statements or only in for statements where it is necessary because of ASI.`<always|as-needed>`

-
=`--arrow-parentheses`

— Whether to add non-necessary parentheses to arrow functions. Defaults to “always”.`<always|as-needed>`

-
=`--bracket-same-line`

— Whether to hug the closing bracket of multiline HTML/JSX tags to the end of the last line, rather than being alone on the following line. Defaults to false.`<true|false>`

-
=`--javascript-formatter-indent-style`

— The indent style applied to JavaScript (and its super languages) files.`<tab|space>`

-
=`--javascript-formatter-indent-width`

— The size of the indentation applied to JavaScript (and its super languages) files. Default to 2.`NUMBER`

-
=`--javascript-formatter-line-ending`

— The type of line ending applied to JavaScript (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--javascript-formatter-line-width`

— What’s the max width of a line applied to JavaScript (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--javascript-formatter-quote-style`

— The type of quotes used in JavaScript code. Defaults to double.`<double|single>`

-
=`--javascript-formatter-attribute-position`

— The attribute position style in JSX elements. Defaults to auto.`<multiline|auto>`

-
=`--javascript-formatter-bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--javascript-formatter-expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--javascript-formatter-operator-linebreak`

— When breaking binary expressions into multiple lines, whether to break them before or after the binary operator. Defaults to “after”.`<before|after>`

-
=`--javascript-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

Setting this option to

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--javascript-linter-enabled`

— Control the linter for JavaScript (and its super languages) files.`<true|false>`

-
=`--javascript-assist-enabled`

— Control the assist for JavaScript (and its super languages) files.`<true|false>`

-
=`--json-parse-allow-comments`

— Allow parsing comments in`<true|false>`

`.json`

files -
=`--json-parse-allow-trailing-commas`

— Allow parsing trailing commas in`<true|false>`

`.json`

files -
=`--json-formatter-enabled`

— Control the formatter for JSON (and its super languages) files.`<true|false>`

-
=`--json-formatter-indent-style`

— The indent style applied to JSON (and its super languages) files.`<tab|space>`

-
=`--json-formatter-indent-width`

— The size of the indentation applied to JSON (and its super languages) files. Default to 2.`NUMBER`

-
=`--json-formatter-line-ending`

— The type of line ending applied to JSON (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--json-formatter-line-width`

— What’s the max width of a line applied to JSON (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--json-formatter-trailing-commas`

— Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Defaults to “none”.`<none|all>`

-
=`--json-formatter-expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--json-formatter-bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--json-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

Setting this option to

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--json-linter-enabled`

— Control the linter for JSON (and its super languages) files.`<true|false>`

-
=`--json-assist-enabled`

— Control the assist for JSON (and its super languages) files.`<true|false>`

-
=`--css-parse-css-modules`

— Enables parsing of CSS Modules specific features. Enable this feature only when your files don’t end in`<true|false>`

`.module.css`

. -
=`--css-parse-tailwind-directives`

— Enables parsing of Tailwind CSS 4.0 directives and functions.`<true|false>`

-
=`--css-formatter-enabled`

— Control the formatter for CSS (and its super languages) files.`<true|false>`

-
=`--css-formatter-indent-style`

— The indent style applied to CSS (and its super languages) files.`<tab|space>`

-
=`--css-formatter-indent-width`

— The size of the indentation applied to CSS (and its super languages) files. Default to 2.`NUMBER`

-
=`--css-formatter-line-ending`

— The type of line ending applied to CSS (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--css-formatter-line-width`

— What’s the max width of a line applied to CSS (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--css-formatter-quote-style`

— The type of quotes used in CSS code. Defaults to double.`<double|single>`

-
=`--css-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--css-linter-enabled`

— Control the linter for CSS files.`<true|false>`

-
=`--css-assist-enabled`

— Control the assist for CSS files.`<true|false>`

-
=`--graphql-formatter-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--graphql-formatter-indent-style`

— The indent style applied to GraphQL files.`<tab|space>`

-
=`--graphql-formatter-indent-width`

— The size of the indentation applied to GraphQL files. Default to 2.`NUMBER`

-
=`--graphql-formatter-line-ending`

— The type of line ending applied to GraphQL files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--graphql-formatter-line-width`

— What’s the max width of a line applied to GraphQL files. Defaults to 80.`NUMBER`

-
=`--graphql-formatter-quote-style`

— The type of quotes used in GraphQL code. Defaults to double.`<double|single>`

-
=`--graphql-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--graphql-linter-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--graphql-assist-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--grit-formatter-enabled`

— Control the formatter for Grit files.`<true|false>`

-
=`--grit-formatter-indent-style`

— The indent style applied to Grit files.`<tab|space>`

-
=`--grit-formatter-indent-width`

— The size of the indentation applied to Grit files. Default to 2.`NUMBER`

-
=`--grit-formatter-line-ending`

— The type of line ending applied to Grit files.`<lf|crlf|cr>`

-
=`--grit-formatter-line-width`

— What’s the max width of a line applied to Grit files. Defaults to 80.`NUMBER`

-
=`--grit-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--grit-linter-enabled`

— Control the linter for Grit files.`<true|false>`

-
=`--grit-assist-enabled`

— Control the assist functionality for Grit files.`<true|false>`

-
=`--html-formatter-enabled`

— Control the formatter for HTML (and its super languages) files.`<true|false>`

-
=`--html-formatter-indent-style`

— The indent style applied to HTML (and its super languages) files.`<tab|space>`

-
=`--html-formatter-indent-width`

— The size of the indentation applied to HTML (and its super languages) files. Default to 2.`NUMBER`

-
=`--html-formatter-line-ending`

— The type of line ending applied to HTML (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--html-formatter-line-width`

— What’s the max width of a line applied to HTML (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--html-formatter-attribute-position`

— The attribute position style in HTML elements. Defaults to auto.`<multiline|auto>`

-
=`--html-formatter-bracket-same-line`

— Whether to hug the closing bracket of multiline HTML tags to the end of the last line, rather than being alone on the following line. Defaults to false.`<true|false>`

-
=`--html-formatter-whitespace-sensitivity`

— Whether to account for whitespace sensitivity when formatting HTML (and its super languages). Defaults to “css”.`<css|strict|ignore>`

-
=`--html-formatter-indent-script-and-style`

— Whether to indent the`<true|false>`

`<script>`

and`<style>`

tags for HTML (and its super languages). Defaults to false. -
=`--html-formatter-self-close-void-elements`

— Whether void elements should be self-closed. Defaults to never.`<always|never>`

-
=`--html-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--html-linter-enabled`

— Control the linter for HTML (and its super languages) files.`<true|false>`

-
=`--html-assist-enabled`

— Control the assist for HTML (and its super languages) files.`<true|false>`

-
=`--assist-enabled`

— Whether Biome should enable assist via LSP and CLI.`<true|false>`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Available positional items:**

— Single file, single path or list of paths`PATH`

**Available options:**

-
— Apply safe fixes, formatting and import sorting`--write`

-
— Apply unsafe fixes. Should be used with`--unsafe`

`--write`

or`--fix`

-
— Alias for`--fix`

`--write`

, writes safe fixes, formatting and import sorting -
=`--formatter-enabled`

— Allow enabling or disabling the formatter check.`<true|false>`

-
=`--linter-enabled`

— Allow enabling or disabling the linter check.`<true|false>`

-
=`--assist-enabled`

— Allow enabling or disabling the assist.`<true|false>`

-
=`--enforce-assist`

— Allows enforcing assist, and make the CLI fail if some actions aren’t applied. Defaults to`<true|false>`

`true`

. -
=`--format-with-errors`

— Whether formatting should be allowed to proceed if a given file has syntax errors`<true|false>`

-
— Enable rule profiling output. Captures timing only for rule execution, not preprocessing such as querying or building the semantic model.`--profile-rules`

-
=`--stdin-file-path`

— Use this option when you want to format code piped from`PATH`

`stdin`

, and print the output to`stdout`

.The file doesn’t need to exist on disk, what matters is the extension of the file. Based on the extension, Biome knows how to check the code.

Also, if you have overrides configured and/or nested configurations, the path may determine the settings being applied.

The provided path may also affect whether the input is treated as ignored. If the path doesn’t exist on disk (virtual path), Biome won’t require it to be part of the project file set, and ignore checks (

`files.includes`

and VCS ignore rules) are skipped.Example:

`shell echo 'let a;' | biome check --stdin-file-path=file.js --write`

-
— When set to true, only the files that have been staged (the ones prepared to be committed) will be linted. This option should be used when working locally.`--staged`

-
— When set to true, only the files that have been changed compared to your`--changed`

`defaultBranch`

configuration will be linted. This option should be used in CI environments. -
=`--since`

— Use this to specify the base branch to compare against when you’re using the —changed flag and the`REF`

`defaultBranch`

is not set in your`biome.json`

-
=`--only`

— Run only the given lint rule, assist action, group of rules and actions, or domain. If the severity level of a rule is`<GROUP|RULE|DOMAIN|ACTION>`

`off`

, then the severity level of the rule is set to`error`

if it is a recommended rule or`warn`

otherwise.Example:

-
=`--skip`

— Skip the given lint rule, assist action, group of rules and actions, or domain by setting the severity level of the rules to`<GROUP|RULE|DOMAIN|ACTION>`

`off`

. This option takes precedence over`--only`

.Example:

-
,`-h`

— Prints help information`--help`

## biome lint

Section titled “biome lint”Run various checks on a set of files.

**Usage**: `biome`

** lint** [

**] [**

`--write`

**] [**

`--unsafe`

**] [**

`--suppress`

**=**

`--reason`

*] [*

`STRING`

**=**

`--only`

*]… [*

`<GROUP|RULE|DOMAIN|ACTION>`

**=**

`--skip`

*]… [*

`<GROUP|RULE|DOMAIN|ACTION>`

**] [**

`--staged`

**] [**

`--changed`

**=**

`--since`

*] [*

`REF`

**] [**

`--profile-rules`

*]…*

`PATH`

**Options that changes how the JSON parser behaves**

=`--json-parse-allow-comments`

— Allow parsing comments in`<true|false>`

`.json`

files=`--json-parse-allow-trailing-commas`

— Allow parsing trailing commas in`<true|false>`

`.json`

files

**Set of properties to integrate Biome with a VCS software.**

-
=`--vcs-enabled`

— Whether Biome should integrate itself with the VCS client`<true|false>`

-
=`--vcs-client-kind`

— The kind of client.`<git>`

-
=`--vcs-use-ignore-file`

— Whether Biome should use the VCS ignore file. When [true], Biome will ignore the files specified in the ignore file.`<true|false>`

-
=`--vcs-root`

— The folder where Biome should check for VCS files. By default, Biome will use the same folder where`PATH`

`biome.json`

was found.If Biome can’t find the configuration, it will attempt to use the current working directory. If no current working directory can’t be found, Biome won’t use the VCS integration, and a diagnostic will be emitted

-
=`--vcs-default-branch`

— The main branch of the project`BRANCH`

**The configuration of the filesystem**

=`--files-max-size`

— The maximum allowed size for source code files in bytes. Files above this limit will be ignored for performance reasons. Defaults to 1 MiB`NUMBER`

=`--files-ignore-unknown`

— Tells Biome to not emit diagnostics when handling files that it doesn’t know`<true|false>`

**Linter options specific to the JavaScript linter**

=`--javascript-linter-enabled`

— Control the linter for JavaScript (and its super languages) files.`<true|false>`

**Linter options specific to the JSON linter**

=`--json-linter-enabled`

— Control the linter for JSON (and its super languages) files.`<true|false>`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Available positional items:**

— Single file, single path or list of paths`PATH`

**Available options:**

-
— Writes safe fixes`--write`

-
— Apply unsafe fixes. Should be used with`--unsafe`

`--write`

or`--fix`

-
— Alias for`--fix`

`--write`

, writes safe fixes -
— Fixes lint rule violations with comment suppressions instead of using a rule code action (fix)`--suppress`

-
=`--reason`

— Explanation for suppressing diagnostics with`STRING`

`--suppress`

-
=`--only`

— Run only the given lint rule, assist action, group of rules and actions, or domain. If the severity level of a rule is`<GROUP|RULE|DOMAIN|ACTION>`

`off`

, then the severity level of the rule is set to`error`

if it is a recommended rule or`warn`

otherwise.Example:

-
=`--skip`

— Skip the given lint rule, assist action, group of rules and actions, or domain by setting the severity level of the rules to`<GROUP|RULE|DOMAIN|ACTION>`

`off`

. This option takes precedence over`--only`

.Example:

-
=`--stdin-file-path`

— Use this option when you want to format code piped from`PATH`

`stdin`

, and print the output to`stdout`

.The file doesn’t need to exist on disk, what matters is the extension of the file. Based on the extension, Biome knows how to lint the code.

The provided path may also affect whether the input is treated as ignored. If the path doesn’t exist on disk (virtual path), Biome won’t require it to be part of the project file set, and ignore checks (

`files.includes`

and VCS ignore rules) are skipped.Example:

`shell echo 'let a;' | biome lint --stdin-file-path=file.js --write`

-
— When set to true, only the files that have been staged (the ones prepared to be committed) will be linted.`--staged`

-
— When set to true, only the files that have been changed compared to your`--changed`

`defaultBranch`

configuration will be linted. -
=`--since`

— Use this to specify the base branch to compare against when you’re using the —changed flag and the`REF`

`defaultBranch`

is not set in your biome.json -
— Enable rule profiling output. Captures timing only for rule execution, not preprocessing such as querying or building the semantic model.`--profile-rules`

-
,`-h`

— Prints help information`--help`

## biome format

Section titled “biome format”Run the formatter on a set of files.

**Usage**: `biome`

** format** [

**] [**

`--write`

**] [**

`--staged`

**] [**

`--changed`

**=**

`--since`

*] [*

`REF`

*]…*

`PATH`

**Generic options applied to all files**

-
=`--format-with-errors`

— Whether formatting should be allowed to proceed if a given file has syntax errors`<true|false>`

-
=`--indent-style`

— The indent style.`<tab|space>`

-
=`--indent-width`

— The size of the indentation, 2 by default`NUMBER`

-
=`--line-ending`

— The type of line ending.`<lf|crlf|cr|auto>`

-
=`--line-width`

— What’s the max width of a line. Defaults to 80.`NUMBER`

-
=`--attribute-position`

— The attribute position style in HTML-ish languages. Defaults to auto.`<multiline|auto>`

-
=`--bracket-same-line`

— Put the`<true|false>`

`>`

of a multi-line HTML or JSX element at the end of the last line instead of being alone on the next line (does not apply to self closing elements). -
=`--bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--use-editorconfig`

— Use any`<true|false>`

`.editorconfig`

files to configure the formatter. Configuration in`biome.json`

will override`.editorconfig`

configuration.Default:

`false`

.

**Formatting options specific to the JavaScript files**

-
=`--javascript-formatter-enabled`

— Control the formatter for JavaScript (and its super languages) files.`<true|false>`

-
=`--jsx-quote-style`

— The type of quotes used in JSX. Defaults to double.`<double|single>`

-
=`--quote-properties`

— When properties in objects are quoted. Defaults to asNeeded.`<preserve|as-needed>`

-
=`--trailing-commas`

— Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Defaults to “all”.`<all|es5|none>`

-
=`--semicolons`

— Whether the formatter prints semicolons for all statements or only in for statements where it is necessary because of ASI.`<always|as-needed>`

-
=`--arrow-parentheses`

— Whether to add non-necessary parentheses to arrow functions. Defaults to “always”.`<always|as-needed>`

-
=`--bracket-same-line`

— Whether to hug the closing bracket of multiline HTML/JSX tags to the end of the last line, rather than being alone on the following line. Defaults to false.`<true|false>`

-
=`--javascript-formatter-indent-style`

— The indent style applied to JavaScript (and its super languages) files.`<tab|space>`

-
=`--javascript-formatter-indent-width`

— The size of the indentation applied to JavaScript (and its super languages) files. Default to 2.`NUMBER`

-
=`--javascript-formatter-line-ending`

— The type of line ending applied to JavaScript (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--javascript-formatter-line-width`

— What’s the max width of a line applied to JavaScript (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--javascript-formatter-quote-style`

— The type of quotes used in JavaScript code. Defaults to double.`<double|single>`

-
=`--javascript-formatter-attribute-position`

— The attribute position style in JSX elements. Defaults to auto.`<multiline|auto>`

-
=`--javascript-formatter-bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--javascript-formatter-expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--javascript-formatter-operator-linebreak`

— When breaking binary expressions into multiple lines, whether to break them before or after the binary operator. Defaults to “after”.`<before|after>`

-
=`--javascript-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

**Options that changes how the JSON parser behaves**

=`--json-parse-allow-comments`

— Allow parsing comments in`<true|false>`

`.json`

files=`--json-parse-allow-trailing-commas`

— Allow parsing trailing commas in`<true|false>`

`.json`

files

**Options that changes how the CSS parser behaves**

=`--css-parse-css-modules`

— Enables parsing of CSS Modules specific features. Enable this feature only when your files don’t end in`<true|false>`

`.module.css`

.=`--css-parse-tailwind-directives`

— Enables parsing of Tailwind CSS 4.0 directives and functions.`<true|false>`

**Options that changes how the GraphQL formatter behaves**

-
=`--graphql-formatter-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--graphql-formatter-indent-style`

— The indent style applied to GraphQL files.`<tab|space>`

-
=`--graphql-formatter-indent-width`

— The size of the indentation applied to GraphQL files. Default to 2.`NUMBER`

-
=`--graphql-formatter-line-ending`

— The type of line ending applied to GraphQL files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--graphql-formatter-line-width`

— What’s the max width of a line applied to GraphQL files. Defaults to 80.`NUMBER`

-
=`--graphql-formatter-quote-style`

— The type of quotes used in GraphQL code. Defaults to double.`<double|single>`

-
=`--bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--graphql-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

**Options that changes how the CSS formatter behaves**

-
=`--css-formatter-enabled`

— Control the formatter for CSS (and its super languages) files.`<true|false>`

-
=`--css-formatter-indent-style`

— The indent style applied to CSS (and its super languages) files.`<tab|space>`

-
=`--css-formatter-indent-width`

— The size of the indentation applied to CSS (and its super languages) files. Default to 2.`NUMBER`

-
=`--css-formatter-line-ending`

— The type of line ending applied to CSS (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--css-formatter-line-width`

— What’s the max width of a line applied to CSS (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--css-formatter-quote-style`

— The type of quotes used in CSS code. Defaults to double.`<double|single>`

-
=`--css-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

**Options that changes how the HTML formatter behaves**

-
=`--html-formatter-enabled`

— Control the formatter for HTML (and its super languages) files.`<true|false>`

-
=`--html-formatter-indent-style`

— The indent style applied to HTML (and its super languages) files.`<tab|space>`

-
=`--html-formatter-indent-width`

— The size of the indentation applied to HTML (and its super languages) files. Default to 2.`NUMBER`

-
=`--html-formatter-line-ending`

— The type of line ending applied to HTML (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--html-formatter-line-width`

— What’s the max width of a line applied to HTML (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--html-formatter-attribute-position`

— The attribute position style in HTML elements. Defaults to auto.`<multiline|auto>`

-
=`--html-formatter-bracket-same-line`

— Whether to hug the closing bracket of multiline HTML tags to the end of the last line, rather than being alone on the following line. Defaults to false.`<true|false>`

-
=`--html-formatter-whitespace-sensitivity`

— Whether to account for whitespace sensitivity when formatting HTML (and its super languages). Defaults to “css”.`<css|strict|ignore>`

-
=`--html-formatter-indent-script-and-style`

— Whether to indent the`<true|false>`

`<script>`

and`<style>`

tags for HTML (and its super languages). Defaults to false. -
=`--html-formatter-self-close-void-elements`

— Whether void elements should be self-closed. Defaults to never.`<always|never>`

-
=`--html-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

**Set of properties to integrate Biome with a VCS software.**

-
=`--vcs-enabled`

— Whether Biome should integrate itself with the VCS client`<true|false>`

-
=`--vcs-client-kind`

— The kind of client.`<git>`

-
=`--vcs-use-ignore-file`

— Whether Biome should use the VCS ignore file. When [true], Biome will ignore the files specified in the ignore file.`<true|false>`

-
=`--vcs-root`

— The folder where Biome should check for VCS files. By default, Biome will use the same folder where`PATH`

`biome.json`

was found.If Biome can’t find the configuration, it will attempt to use the current working directory. If no current working directory can’t be found, Biome won’t use the VCS integration, and a diagnostic will be emitted

-
=`--vcs-default-branch`

— The main branch of the project`BRANCH`

**The configuration of the filesystem**

=`--files-max-size`

— The maximum allowed size for source code files in bytes. Files above this limit will be ignored for performance reasons. Defaults to 1 MiB`NUMBER`

=`--files-ignore-unknown`

— Tells Biome to not emit diagnostics when handling files that it doesn’t know`<true|false>`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Available positional items:**

— Single file, single path or list of paths.`PATH`

**Available options:**

-
=`--json-formatter-enabled`

— Control the formatter for JSON (and its super languages) files.`<true|false>`

-
=`--json-formatter-indent-style`

— The indent style applied to JSON (and its super languages) files.`<tab|space>`

-
=`--json-formatter-indent-width`

— The size of the indentation applied to JSON (and its super languages) files. Default to 2.`NUMBER`

-
=`--json-formatter-line-ending`

— The type of line ending applied to JSON (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--json-formatter-line-width`

— What’s the max width of a line applied to JSON (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--json-formatter-trailing-commas`

— Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Defaults to “none”.`<none|all>`

-
=`--json-formatter-expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--json-formatter-bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--json-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--stdin-file-path`

— Use this option when you want to format code piped from`PATH`

`stdin`

, and print the output to`stdout`

.The file doesn’t need to exist on disk, what matters is the extension of the file. Based on the extension, Biome knows how to format the code.

The provided path may also affect whether the input is treated as ignored. If the path doesn’t exist on disk (virtual path), Biome won’t require it to be part of the project file set, and ignore checks (

`files.includes`

and VCS ignore rules) are skipped.Example:

`shell echo 'let a;' | biome format --stdin-file-path=file.js --write`

-
— Writes formatted files to a file system.`--write`

-
— Alias of`--fix`

`--write`

, writes formatted files to a file system. -
— When set to true, only the files that have been staged (the ones prepared to be committed) will be linted.`--staged`

-
— When set to true, only the files that have been changed compared to your`--changed`

`defaultBranch`

configuration will be linted. -
=`--since`

— Use this to specify the base branch to compare against when you’re using the —changed flag, and the`REF`

`defaultBranch`

is not set in your biome.json -
,`-h`

— Prints help information`--help`

## biome ci

Section titled “biome ci”Command to use in CI environments. Runs formatter, linter and import sorting to the requested files.

Files won’t be modified, the command is a read-only operation.

**Usage**: `biome`

** ci** [

**=**

`--formatter-enabled`

*] [*

`<true|false>`

**=**

`--linter-enabled`

*] [*

`<true|false>`

**=**

`--assist-enabled`

*] [*

`<true|false>`

**=**

`--format-with-errors`

*] [*

`<true|false>`

**=**

`--enforce-assist`

*] [*

`<true|false>`

**] [**

`--changed`

**=**

`--since`

*] [*

`REF`

**=**

`--only`

*]… [*

`<GROUP|RULE|DOMAIN|ACTION>`

**=**

`--skip`

*]… [*

`<GROUP|RULE|DOMAIN|ACTION>`

*]…*

`PATH`

**Options that changes how the JSON parser behaves**

=`--json-parse-allow-comments`

— Allow parsing comments in`<true|false>`

`.json`

files=`--json-parse-allow-trailing-commas`

— Allow parsing trailing commas in`<true|false>`

`.json`

files

**The configuration that is contained inside the file biome.json**

-
=`--vcs-enabled`

— Whether Biome should integrate itself with the VCS client`<true|false>`

-
=`--vcs-client-kind`

— The kind of client.`<git>`

-
=`--vcs-use-ignore-file`

— Whether Biome should use the VCS ignore file. When [true], Biome will ignore the files specified in the ignore file.`<true|false>`

-
=`--vcs-root`

— The folder where Biome should check for VCS files. By default, Biome will use the same folder where`PATH`

`biome.json`

was found. -
=`--vcs-default-branch`

— The main branch of the project`BRANCH`

-
=`--files-max-size`

— The maximum allowed size for source code files in bytes. Files above this limit will be ignored for performance reasons. Defaults to 1 MiB`NUMBER`

-
=`--files-ignore-unknown`

— Tells Biome to not emit diagnostics when handling files that it doesn’t know`<true|false>`

-
=`--format-with-errors`

— Whether formatting should be allowed to proceed if a given file has syntax errors`<true|false>`

-
=`--indent-style`

— The indent style.`<tab|space>`

-
=`--indent-width`

— The size of the indentation, 2 by default`NUMBER`

-
=`--line-ending`

— The type of line ending.`<lf|crlf|cr|auto>`

-
=`--line-width`

— What’s the max width of a line. Defaults to 80.`NUMBER`

-
=`--attribute-position`

— The attribute position style in HTML-ish languages. Defaults to auto.`<multiline|auto>`

-
=`--bracket-same-line`

— Put the`<true|false>`

`>`

of a multi-line HTML or JSX element at the end of the last line instead of being alone on the next line (does not apply to self closing elements). -
=`--bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--use-editorconfig`

— Use any`<true|false>`

`.editorconfig`

files to configure the formatter. Configuration in`biome.json`

will override`.editorconfig`

configuration.Default:

`false`

. -
=`--jsx-everywhere`

— When enabled, files like`<true|false>`

`.js`

/`.mjs`

/`.cjs`

may contain JSX syntax.Defaults to

`true`

. -
=`--javascript-formatter-enabled`

— Control the formatter for JavaScript (and its super languages) files.`<true|false>`

-
=`--jsx-quote-style`

— The type of quotes used in JSX. Defaults to double.`<double|single>`

-
=`--quote-properties`

— When properties in objects are quoted. Defaults to asNeeded.`<preserve|as-needed>`

-
=`--trailing-commas`

— Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Defaults to “all”.`<all|es5|none>`

-
=`--semicolons`

— Whether the formatter prints semicolons for all statements or only in for statements where it is necessary because of ASI.`<always|as-needed>`

-
=`--arrow-parentheses`

— Whether to add non-necessary parentheses to arrow functions. Defaults to “always”.`<always|as-needed>`

-
=`--bracket-same-line`

— Whether to hug the closing bracket of multiline HTML/JSX tags to the end of the last line, rather than being alone on the following line. Defaults to false.`<true|false>`

-
=`--javascript-formatter-indent-style`

— The indent style applied to JavaScript (and its super languages) files.`<tab|space>`

-
=`--javascript-formatter-indent-width`

— The size of the indentation applied to JavaScript (and its super languages) files. Default to 2.`NUMBER`

-
=`--javascript-formatter-line-ending`

— The type of line ending applied to JavaScript (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--javascript-formatter-line-width`

— What’s the max width of a line applied to JavaScript (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--javascript-formatter-quote-style`

— The type of quotes used in JavaScript code. Defaults to double.`<double|single>`

-
=`--javascript-formatter-attribute-position`

— The attribute position style in JSX elements. Defaults to auto.`<multiline|auto>`

-
=`--javascript-formatter-bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--javascript-formatter-expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--javascript-formatter-operator-linebreak`

— When breaking binary expressions into multiple lines, whether to break them before or after the binary operator. Defaults to “after”.`<before|after>`

-
=`--javascript-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--javascript-linter-enabled`

— Control the linter for JavaScript (and its super languages) files.`<true|false>`

-
=`--javascript-assist-enabled`

— Control the assist for JavaScript (and its super languages) files.`<true|false>`

-
=`--json-parse-allow-comments`

— Allow parsing comments in`<true|false>`

`.json`

files -
=`--json-parse-allow-trailing-commas`

— Allow parsing trailing commas in`<true|false>`

`.json`

files -
=`--json-formatter-enabled`

— Control the formatter for JSON (and its super languages) files.`<true|false>`

-
=`--json-formatter-indent-style`

— The indent style applied to JSON (and its super languages) files.`<tab|space>`

-
=`--json-formatter-indent-width`

— The size of the indentation applied to JSON (and its super languages) files. Default to 2.`NUMBER`

-
=`--json-formatter-line-ending`

— The type of line ending applied to JSON (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--json-formatter-line-width`

— What’s the max width of a line applied to JSON (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--json-formatter-trailing-commas`

— Print trailing commas wherever possible in multi-line comma-separated syntactic structures. Defaults to “none”.`<none|all>`

-
=`--json-formatter-expand`

— Whether to expand arrays and objects on multiple lines. When set to`<auto|always|never>`

`auto`

, object literals are formatted on multiple lines if the first property has a newline, and array literals are formatted on a single line if it fits in the line. When set to`always`

, these literals are formatted on multiple lines, regardless of length of the list. When set to`never`

, these literals are formatted on a single line if it fits in the line. When formatting`package.json`

, Biome will use`always`

unless configured otherwise. Defaults to “auto”. -
=`--json-formatter-bracket-spacing`

— Whether to insert spaces around brackets in object literals. Defaults to true.`<true|false>`

-
=`--json-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--json-linter-enabled`

— Control the linter for JSON (and its super languages) files.`<true|false>`

-
=`--json-assist-enabled`

— Control the assist for JSON (and its super languages) files.`<true|false>`

-
=`--css-parse-css-modules`

— Enables parsing of CSS Modules specific features. Enable this feature only when your files don’t end in`<true|false>`

`.module.css`

. -
=`--css-parse-tailwind-directives`

— Enables parsing of Tailwind CSS 4.0 directives and functions.`<true|false>`

-
=`--css-formatter-enabled`

— Control the formatter for CSS (and its super languages) files.`<true|false>`

-
=`--css-formatter-indent-style`

— The indent style applied to CSS (and its super languages) files.`<tab|space>`

-
=`--css-formatter-indent-width`

— The size of the indentation applied to CSS (and its super languages) files. Default to 2.`NUMBER`

-
=`--css-formatter-line-ending`

— The type of line ending applied to CSS (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--css-formatter-line-width`

— What’s the max width of a line applied to CSS (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--css-formatter-quote-style`

— The type of quotes used in CSS code. Defaults to double.`<double|single>`

-
=`--css-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--css-linter-enabled`

— Control the linter for CSS files.`<true|false>`

-
=`--css-assist-enabled`

— Control the assist for CSS files.`<true|false>`

-
=`--graphql-formatter-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--graphql-formatter-indent-style`

— The indent style applied to GraphQL files.`<tab|space>`

-
=`--graphql-formatter-indent-width`

— The size of the indentation applied to GraphQL files. Default to 2.`NUMBER`

-
=`--graphql-formatter-line-ending`

— The type of line ending applied to GraphQL files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--graphql-formatter-line-width`

— What’s the max width of a line applied to GraphQL files. Defaults to 80.`NUMBER`

-
=`--graphql-formatter-quote-style`

— The type of quotes used in GraphQL code. Defaults to double.`<double|single>`

-
=`--graphql-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--graphql-linter-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--graphql-assist-enabled`

— Control the formatter for GraphQL files.`<true|false>`

-
=`--grit-formatter-enabled`

— Control the formatter for Grit files.`<true|false>`

-
=`--grit-formatter-indent-style`

— The indent style applied to Grit files.`<tab|space>`

-
=`--grit-formatter-indent-width`

— The size of the indentation applied to Grit files. Default to 2.`NUMBER`

-
=`--grit-formatter-line-ending`

— The type of line ending applied to Grit files.`<lf|crlf|cr>`

-
=`--grit-formatter-line-width`

— What’s the max width of a line applied to Grit files. Defaults to 80.`NUMBER`

-
=`--grit-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--grit-linter-enabled`

— Control the linter for Grit files.`<true|false>`

-
=`--grit-assist-enabled`

— Control the assist functionality for Grit files.`<true|false>`

-
=`--html-formatter-enabled`

— Control the formatter for HTML (and its super languages) files.`<true|false>`

-
=`--html-formatter-indent-style`

— The indent style applied to HTML (and its super languages) files.`<tab|space>`

-
=`--html-formatter-indent-width`

— The size of the indentation applied to HTML (and its super languages) files. Default to 2.`NUMBER`

-
=`--html-formatter-line-ending`

— The type of line ending applied to HTML (and its super languages) files.`<lf|crlf|cr|auto>`

`auto`

uses CRLF on Windows and LF on other platforms. -
=`--html-formatter-line-width`

— What’s the max width of a line applied to HTML (and its super languages) files. Defaults to 80.`NUMBER`

-
=`--html-formatter-attribute-position`

— The attribute position style in HTML elements. Defaults to auto.`<multiline|auto>`

-
=`--html-formatter-bracket-same-line`

— Whether to hug the closing bracket of multiline HTML tags to the end of the last line, rather than being alone on the following line. Defaults to false.`<true|false>`

-
=`--html-formatter-whitespace-sensitivity`

— Whether to account for whitespace sensitivity when formatting HTML (and its super languages). Defaults to “css”.`<css|strict|ignore>`

-
=`--html-formatter-indent-script-and-style`

— Whether to indent the`<true|false>`

`<script>`

and`<style>`

tags for HTML (and its super languages). Defaults to false. -
=`--html-formatter-self-close-void-elements`

— Whether void elements should be self-closed. Defaults to never.`<always|never>`

-
=`--html-formatter-trailing-newline`

— Whether to add a trailing newline at the end of the file.`<true|false>`

`false`

is**highly discouraged**because it could cause many problems with other tools: - https://thoughtbot.com/blog/no-newline-at-end-of-file - https://callmeryan.medium.com/no-newline-at-end-of-file-navigating-gits-warning-for-android-developers-af14e73dd804 - https://unix.stackexchange.com/questions/345548/how-to-cat-files-together-adding-missing-newlines-at-end-of-some-filesDisable the option at your own risk.

Defaults to true.

-
=`--html-linter-enabled`

— Control the linter for HTML (and its super languages) files.`<true|false>`

-
=`--html-assist-enabled`

— Control the assist for HTML (and its super languages) files.`<true|false>`

-
=`--assist-enabled`

— Whether Biome should enable assist via LSP and CLI.`<true|false>`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Available positional items:**

— Single file, single path or list of paths`PATH`

**Available options:**

-
=`--formatter-enabled`

— Allow enabling or disabling the formatter check.`<true|false>`

-
=`--linter-enabled`

— Allow enabling or disable the linter check.`<true|false>`

-
=`--assist-enabled`

— Allow enabling or disabling the assist.`<true|false>`

-
=`--format-with-errors`

— Whether formatting should be allowed to proceed if a given file has syntax errors`<true|false>`

-
=`--enforce-assist`

— Allows enforcing assist, and make the CLI fail if some actions aren’t applied. Defaults to`<true|false>`

`true`

. -
— When set to true, only the files that have been changed compared to your`--changed`

`defaultBranch`

configuration will be linted. -
=`--since`

— Use this to specify the base branch to compare against when you’re using the —changed flag and the`REF`

`defaultBranch`

is not set in your biome.json -
=`--threads`

— The number of threads to use. This is useful when running the CLI in environments with limited resource, for example CI.`NUMBER`

Uses environment variable

`BIOME_THREADS`

-
=`--only`

— Run only the given lint rule, assist action, group of rules and actions, or domain. If the severity level of a rule is`<GROUP|RULE|DOMAIN|ACTION>`

`off`

, then the severity level of the rule is set to`error`

if it is a recommended rule or`warn`

otherwise.Example:

-
=`--skip`

— Skip the given lint rule, assist action, group of rules and actions, or domain by setting the severity level of the rules to`<GROUP|RULE|DOMAIN|ACTION>`

`off`

. This option takes precedence over`--only`

.Example:

-
,`-h`

— Prints help information`--help`

## biome init

Section titled “biome init”Bootstraps a new biome project. Creates a configuration file with some defaults.

**Usage**: `biome`

** init** [

**]**

`--jsonc`

**Available options:**

— Tells Biome to emit a`--jsonc`

`biome.jsonc`

file.,`-h`

— Prints help information`--help`

## biome lsp-proxy

Section titled “biome lsp-proxy”Acts as a server for the Language Server Protocol over stdin/stdout.

**Usage**: `biome`

** lsp-proxy** [

**=**

`--log-prefix-name`

*] [*

`STRING`

**=**

`--log-path`

*] [*

`PATH`

**=**

`--log-level`

*] [*

`<none|debug|info|warn|error>`

**=**

`--log-kind`

*] [*

`<pretty|compact|json>`

**=**

`--watcher-kind`

*] [*

`<polling|recommended|none>`

**=**

`--watcher-polling-interval`

*]*

`NUMBER`

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Controls various aspects of the Biome Daemon.**

-
=`--watcher-kind`

— Controls how the Biome file watcher should behave.`<polling|recommended|none>`

Uses environment variable

`BIOME_WATCHER_KIND`

[default: recommended]

-
=`--watcher-polling-interval`

— The polling interval in milliseconds. This is only applicable when using the polling watcher.`NUMBER`

Uses environment variable

`BIOME_WATCHER_POLLING_INTERVAL`

[default: 2000]

**Available options:**

,`-h`

— Prints help information`--help`

## biome migrate

Section titled “biome migrate”Updates the configuration when there are breaking changes.

**Usage**: `biome`

** migrate** [

**] [**

`--write`

*]*

`COMMAND ...`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**Available options:**

— Writes the new configuration file to disk`--write`

— Alias of`--fix`

`--write`

, writes the new configuration file to disk,`-h`

— Prints help information`--help`

**Available commands:**

— It attempts to find the files`prettier`

`.prettierrc`

/`prettier.json`

and`.prettierignore`

, and map the Prettier’s configuration into Biome’s configuration file.— It attempts to find the ESLint configuration file in the working directory, and update the Biome’s configuration file as a result.`eslint`

## biome migrate prettier

Section titled “biome migrate prettier”It attempts to find the files `.prettierrc`

/`prettier.json`

and `.prettierignore`

, and map the Prettier’s configuration into Biome’s configuration file.

**Usage**: `biome`

`migrate`

`prettier`

**Available options:**

,`-h`

— Prints help information`--help`

## biome migrate eslint

Section titled “biome migrate eslint”It attempts to find the ESLint configuration file in the working directory, and update the Biome’s configuration file as a result.

**Usage**: `biome`

`migrate`

** eslint** [

**] [**

`--include-inspired`

**]**

`--include-nursery`

**Available options:**

— Includes rules inspired from an eslint rule in the migration`--include-inspired`

— Includes nursery rules in the migration`--include-nursery`

,`-h`

— Prints help information`--help`

## biome search

Section titled “biome search”EXPERIMENTAL: Searches for Grit patterns across a project.

Note: GritQL escapes code snippets using backticks, but most shells interpret backticks as command invocations. To avoid this, it’s best to put single quotes around your Grit queries.

### Example

Section titled “Example”**Usage**: `biome`

** search** [

**=**

`-l`

*]*

`ARG`

*[*

`PATTERN`

*]…*

`PATH`

**Global options applied to all commands**

-
=`--colors`

— Set the formatting mode for markup: “off” prints everything as plain text, “force” forces the formatting of markup using ANSI even if the console output is determined to be incompatible`<off|force>`

-
— Connect to a running instance of the Biome daemon server.`--use-server`

-
— Print additional diagnostics, and some diagnostics show more information. Also, print out what files were processed and which ones were modified.`--verbose`

-
=`--config-path`

— Set the file path to the configuration file, or the directory path to find`PATH`

`biome.json`

or`biome.jsonc`

. If used, it disables the default configuration file resolution.Uses environment variable

`BIOME_CONFIG_PATH`

-
=`--max-diagnostics`

— Cap the amount of diagnostics displayed. When`<none|<NUMBER>>`

`none`

is provided, the limit is lifted.[default: 20]

-
— Skip over files containing syntax errors instead of emitting an error diagnostic.`--skip-parse-errors`

-
— Silence errors that would be emitted in case no files were processed during the execution of the command.`--no-errors-on-unmatched`

-
— Tell Biome to exit with an error code if some diagnostics emit warnings.`--error-on-warnings`

### [`--reporter`

=`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

] [`--reporter-file`

=`PATH`

]

Section titled “[--reporter=<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>] [--reporter-file=PATH]”`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

`--reporter-file`

`PATH`

-
=`--reporter`

`<default|json|json-pretty|github|junit|summary|gitlab|checkstyle|rdjson|sarif>`

-
=`--reporter-file`

`PATH`

-
=`--diagnostic-level`

— The level of diagnostics to show. In order, from the lowest to the most important: info, warn, error. Passing`<info|warn|error>`

`--diagnostic-level=error`

will cause Biome to print only diagnostics that contain only errors.[default: info]

**Options to control logging (CLI and Daemon)**

-
=`--log-file`

— Optional path/file to redirect log messages to. This option is applicable only to the CLI.`STRING`

If omitted, logs are printed to stdout.

Uses environment variable

`BIOME_LOG_FILE`

-
=`--log-prefix-name`

— Uses environment variable`STRING`

`BIOME_LOG_PREFIX_NAME`

[default: server.log]

-
=`--log-path`

— Allows changing the folder where logs are stored. This option is applicable only to the daemon.`PATH`

Uses environment variable

`BIOME_LOG_PATH`

[default: /home/runner/.cache/biome/biome-logs]

-
=`--log-level`

— The level of logging. In order, from the most verbose to the least verbose: debug, info, warn, error.`<none|debug|info|warn|error>`

The value

`none`

won’t show any logging.Uses environment variable

`BIOME_LOG_LEVEL`

[default: none]

-
=`--log-kind`

— What the log should look like.`<pretty|compact|json>`

Uses environment variable

`BIOME_LOG_KIND`

[default: pretty]

**The configuration of the filesystem**

=`--files-max-size`

— The maximum allowed size for source code files in bytes. Files above this limit will be ignored for performance reasons. Defaults to 1 MiB`NUMBER`

=`--files-ignore-unknown`

— Tells Biome to not emit diagnostics when handling files that it doesn’t know`<true|false>`

**Set of properties to integrate Biome with a VCS software.**

-
=`--vcs-enabled`

— Whether Biome should integrate itself with the VCS client`<true|false>`

-
=`--vcs-client-kind`

— The kind of client.`<git>`

-
=`--vcs-use-ignore-file`

— Whether Biome should use the VCS ignore file. When [true], Biome will ignore the files specified in the ignore file.`<true|false>`

-
=`--vcs-root`

— The folder where Biome should check for VCS files. By default, Biome will use the same folder where`PATH`

`biome.json`

was found. -
=`--vcs-default-branch`

— The main branch of the project`BRANCH`

**Available positional items:**

-
— The GritQL pattern to search for.`PATTERN`

Note that the search command (currently) does not support rewrites.

-
— Single file, single path or list of paths.`PATH`

**Available options:**

-
=`--stdin-file-path`

— Use this option when you want to search through code piped from`PATH`

`stdin`

, and print the output to`stdout`

.The file doesn’t need to exist on disk, what matters is the extension of the file. Based on the extension, Biome knows how to parse the code.

Example:

`shell echo 'let a;' | biome search '`let $var`' --stdin-file-path=file.js`

-
,`-l`

=`--language`

— The language to which the pattern applies.`ARG`

Grit queries are specific to the grammar of the language they target, so we currently do not support writing queries that apply to multiple languages at once.

When none, the default language is JavaScript.

-
,`-h`

— Prints help information`--help`

## biome explain

Section titled “biome explain”Shows documentation of various aspects of the CLI.

### Examples

Section titled “Examples”**Usage**: `biome`

`explain`

`NAME`

**Available positional items:**

— Single name to display documentation for.`NAME`

**Available options:**

,`-h`

— Prints help information`--help`

## biome clean

Section titled “biome clean”Cleans the logs emitted by the daemon.

**Usage**: `biome`

`clean`

**Available options:**

,`-h`

— Prints help information`--help`

## Useful information

Section titled “Useful information”- When encountering symbolic links, the CLI will expand them until three levels deep. Deeper levels will result into an error diagnostic.

Copyright (c) 2023-present Biome Developers and Contributors.
