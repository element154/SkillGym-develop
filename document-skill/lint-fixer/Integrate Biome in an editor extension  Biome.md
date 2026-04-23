# Integrate Biome in an editor extension

Biome has LSP first-class support. If your editor does implement LSP, then the integration of Biome should be seamless.

### Use the LSP proxy

Section titled “Use the LSP proxy”Biome has a command called `lsp-proxy`

. When executed, Biome will spawn two processes:

- a daemon that does execute the requested operations;
- a server that functions as a proxy between the requests of the client - the editor - and the server - the daemon;

If your editor is able to interact with a server and send JSON-RPC request, you only need to configure the editor run that command.

You can check how the `neo-vim biome extension`

does it.

### Use `stdin`

Section titled “Use stdin”If your editor doesn’t support LSP, you use directly the binary `biome`

and call it using standard input.

The following commands can be called via standard input:

Biome will return the new output (or the original output if changes haven’t occurred) to standard output and the diagnostics to standard error.

When you use `stdin`

, you must pass the `--stdin-file-path`

option. The file `path`

**doesn’t need to exist** in your file system, it can be any name. **What’s important** is to provide the correct file extension, so Biome knows **how to treat** your file.

It’s the editor’s responsibility to locate the resolve the path of the binary and then call it when it’s needed. The binaries are shipped to npm based on the architectures and OS that we support:

`@biomejs/cli-darwin-arm64`

`@biomejs/cli-darwin-x64`

`@biomejs/cli-linux-arm64`

`@biomejs/cli-linux-x64`

`@biomejs/cli-win32-arm64`

`@biomejs/cli-win32-x64`

The binary name is `biome`

or `biome.exe`

, and it can be found in the root directory of the library, e.g.: `@biomejs/cli-darwin-arm64/biome`

, `@biomejs/cli-win32-x64/biome.exe`

.

### Extension settings

Section titled “Extension settings”The Biome Language Server exposes the following settings, which the extension can expose to users.

`require_configuration`

Section titled “require_configuration”Type:

`boolean`

Default:`false`

Whether the Biome Language Server requires a configuration file. When set to `true`

, it won’t analyze any file (except for parsing) until there’s a `biome.json`

file in the root of the project.

`configuration_path`

Section titled “configuration_path”Type:

`string`

Default:`null`

A path to a custom configuration file. The path can be the folder where the `biome.json`

/`biome.jsonc`

is, or a path to a file.

The path can be relative or absolute. The Biome Language Server reads this option only when provided. Use this option when the configuration is *in a subfolder of your project*.

`inline_config`

Section titled “inline_config”Type:

`object`

Default:`null`

An inline version of the Biome configuration. The options of this configuration will override the options coming from any `biome.json`

file read from disk (or the defaults).

For example, let’s say your project enables the rule `noConsole`

with `error`

severity:

However, during local development, you want to disable this rule because it’s useful and you don’t want to see red squiggles. In your `inline_config`

, you would write something like the following:

### Use the daemon with the binary

Section titled “Use the daemon with the binary”Using the binary via CLI is very efficient, although you won’t be able to provide logs to your users. The CLI allows you to bootstrap a daemon and then use the CLI commands through the daemon itself.

In order to do so, you first need to start a daemon process with the `start`

command:

Then, every command needs to add the `--use-server`

options, e.g.:

### Daemon logs

Section titled “Daemon logs”The Biome daemon saves logs in your file system. Logs are stored in a folder called `biome-logs`

. The path of this folder changes based on your operative system:

- Linux:
`~/.cache/biome`

; - Windows:
`C:\Users\<UserName>\AppData\Local\biomejs\biome\cache`

- macOS:
`/Users/<UserName>/Library/Caches/dev.biomejs.biome`

For other operative systems, you can find the folder in the system’s temporary directory.

To obtain the precise path, execute the following command:

The log files are rotated on an hourly basis.

Copyright (c) 2023-present Biome Developers and Contributors.
