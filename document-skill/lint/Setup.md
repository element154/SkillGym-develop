# Setup

We have specific setup instructions depending on your editor of choice. If you don't see your editor on this list and would like a setup guide, please open an issue.

If you're transferring your configuration from `ruff-lsp`

,
regardless of editor, there are several settings which have changed or are no longer available. See
the migration guide for more.

Note

The setup instructions provided below are on a best-effort basis. If you encounter any issues while setting up the Ruff in an editor, please open an issue for assistance and help in improving this documentation.

Tip

Regardless of the editor, it is recommended to disable the older language server
(`ruff-lsp`

) to prevent any conflicts.

## VS Code

Install the Ruff extension from the VS Code
Marketplace. It is
recommended to have the Ruff extension version `2024.32.0`

or later to get the best experience with
the Ruff Language Server.

For more documentation on the Ruff extension, refer to the README of the extension repository.

## Neovim

The `nvim-lspconfig`

plugin can be used to configure the
Ruff Language Server in Neovim. To set it up, install
`nvim-lspconfig`

plugin, set it up as per the
configuration documentation, and add the
following to your `init.lua`

:

Note

If the installed version of `nvim-lspconfig`

includes the changes from
neovim/nvim-lspconfig@`70d1c2c`

,
you will need to use Ruff version `0.5.3`

or later.

If you're using Ruff alongside another language server (like Pyright), you may want to defer to that
language server for certain capabilities, like `textDocument/hover`

:

```
vim.api.nvim_create_autocmd("LspAttach", {
group = vim.api.nvim_create_augroup('lsp_attach_disable_ruff_hover', { clear = true }),
callback = function(args)
local client = vim.lsp.get_client_by_id(args.data.client_id)
if client == nil then
return
end
if client.name == 'ruff' then
-- Disable hover in favor of Pyright
client.server_capabilities.hoverProvider = false
end
end,
desc = 'LSP: Disable hover capability from Ruff',
})
```

If you'd like to use Ruff exclusively for linting, formatting, and organizing imports, you can disable those capabilities for Pyright:

```
require('lspconfig').pyright.setup {
settings = {
pyright = {
-- Using Ruff's import organizer
disableOrganizeImports = true,
},
python = {
analysis = {
-- Ignore all files for analysis to exclusively use Ruff for linting
ignore = { '*' },
},
},
},
}
```

By default, the log level for Ruff is set to `info`

. To change the log level, you can set the
`logLevel`

setting:

By default, Ruff will write logs to stderr which will be available in Neovim's LSP client log file
(`:lua vim.print(vim.lsp.get_log_path())`

). It's also possible to divert these logs to a separate
file with the `logFile`

setting.

To view the trace logs between Neovim and Ruff, set the log level for Neovim's LSP client to `debug`

:

## With the `conform.nvim`

plugin for Neovim.

## With the `nvim-lint`

plugin for Neovim.

## With the ALE plugin for Neovim or Vim.

*Neovim (using Lua):*

```
-- Linters
vim.g.ale_linters = { python = { "ruff" } }
-- Fixers
vim.g.ale_fixers = { python = { "ruff", "ruff_format" } }
```

*Vim (using Vimscript):*

```
" Linters
let g:ale_linters = { "python": ["ruff"] }
" Fixers
let g:ale_fixers = { "python": ["ruff", "ruff_format"] }
```

`ruff`

will run `ruff check --fix`

(to fix all auto-fixable
problems) whereas `ruff_format`

will run `ruff format`

.
## Vim

The `vim-lsp`

plugin can be used to configure the Ruff Language Server in Vim.
To set it up, install `vim-lsp`

plugin and register the server using the following
in your `.vimrc`

:

```
if executable('ruff')
au User lsp_setup call lsp#register_server({
\ 'name': 'ruff',
\ 'cmd': {server_info->['ruff', 'server']},
\ 'allowlist': ['python'],
\ 'workspace_config': {},
\ })
endif
```

See the `vim-lsp`

documentation for more
details on how to configure the language server.

If you're using Ruff alongside another LSP (like Pyright), you may want to defer to that LSP for certain capabilities,
like `textDocument/hover`

by adding the following to the function `s:on_lsp_buffer_enabled()`

:

```
function! s:on_lsp_buffer_enabled() abort
" add your keybindings here (see https://github.com/prabirshrestha/vim-lsp?tab=readme-ov-file#registering-servers)
let l:capabilities = lsp#get_server_capabilities('ruff')
if !empty(l:capabilities)
let l:capabilities.hoverProvider = v:false
endif
endfunction
```

Ruff is also available as part of the coc-pyright extension for coc.nvim.

## Ruff can also be integrated via efm language server in just a few lines.

Following is an example config for efm to use Ruff for linting and formatting Python files:## Helix

Open the language configuration file for Helix and add the language server as follows:

Then, you'll register the language server as the one to use with Python. If you don't already have a
language server registered to use with Python, add this to `languages.toml`

:

Otherwise, if you already have `language-servers`

defined, you can simply add `"ruff"`

to the list. For example,
if you already have `pylsp`

as a language server, you can modify the language entry as follows:

Note

Support for multiple language servers for a language is only available in Helix version
`23.10`

and later.

If you want to, as an example, turn on auto-formatting, add `auto-format = true`

:

See the Helix documentation for more settings you can use here.

You can pass settings into `ruff server`

using `[language-server.ruff.config.settings]`

. For example:

```
[language-server.ruff.config.settings]
lineLength = 80
[language-server.ruff.config.settings.lint]
select = ["E4", "E7"]
preview = false
[language-server.ruff.config.settings.format]
preview = true
```

By default, the log level for Ruff is set to `info`

. To change the log level, you can set the
`logLevel`

setting:

```
[language-server.ruff]
command = "ruff"
args = ["server"]
[language-server.ruff.config.settings]
logLevel = "debug"
```

You can also divert Ruff's logs to a separate file with the `logFile`

setting.

To view the trace logs between Helix and Ruff, pass in the `-v`

(verbose) flag when starting Helix:

## Kate

- Activate the LSP Client plugin.
- Setup LSP Client as desired.
- Finally, add this to
`Settings`

->`Configure Kate`

->`LSP Client`

->`User Server Settings`

:

```
{
"servers": {
"python": {
"command": ["ruff", "server"],
"url": "https://github.com/astral-sh/ruff",
"highlightingModeRegex": "^Python$",
"settings": {}
}
}
}
```

See LSP Client documentation for more details on how to configure the server from there.

Important

Kate's LSP Client plugin does not support multiple servers for the same language. As a
workaround, you can use the `python-lsp-server`

along with the `python-lsp-ruff`

plugin to
use Ruff alongside another language server. Note that this setup won't use the server settings
because the `python-lsp-ruff`

plugin uses the
`ruff`

executable and not the language server.

## Sublime Text

To use Ruff with Sublime Text, install Sublime Text's LSP and LSP-ruff package.

## PyCharm

Starting with version 2025.3, PyCharm supports Ruff out of the box:

-
Go to

**Python | Tools | Ruff**in the Settings dialog. -
Select the

**Enable**checkbox. -
In the Execution mode setting, select how PyCharm should search for the executable:

**Interpreter**mode: PyCharm searches for an executable installed in your interpreter. To install the Ruff package for the selected interpreter, click*Install Ruff*.**Path**mode: PyCharm searches for an executable in`$PATH`

. If the executable is not found, you can specify the path by clicking the Browse... icon. -
Select which options should be enabled.

For more information, refer to PyCharm documentation.

### Via External Tool

Ruff can be installed as an External Tool in PyCharm. Open the Preferences pane, then navigate to "Tools", then "External Tools". From there, add a new tool with the following configuration:

Ruff should then appear as a runnable action:

### Via third-party plugin

Ruff is also available as the Ruff plugin on the IntelliJ Marketplace (maintained by @koxudaxi).

## Emacs

Ruff can be utilized as a language server via `Eglot`

, which is in Emacs's core.
To enable Ruff with automatic formatting on save, use the following configuration:

```
(with-eval-after-load 'eglot
(add-to-list 'eglot-server-programs
'(python-base-mode . ("ruff" "server"))))
(add-hook 'python-base-mode-hook
(lambda ()
(eglot-ensure)
(add-hook 'after-save-hook 'eglot-format nil t)))
```

Ruff is available as `flymake-ruff`

on MELPA:

Ruff is also available as `emacs-ruff-format`

:

Alternatively, it can be used via the Apheleia formatter library, by setting this configuration:

```
;; Replace default (black) to use ruff for sorting import and formatting.
(setf (alist-get 'python-mode apheleia-mode-alist)
'(ruff-isort ruff))
(setf (alist-get 'python-ts-mode apheleia-mode-alist)
'(ruff-isort ruff))
```

## TextMate

Ruff is also available via the `textmate2-ruff-linter`

bundle for TextMate.

## Zed

Ruff support is now built into Zed (no separate extension required).

By default, Zed uses Ruff for formatting and linting.

To set up editor-wide Ruff options, provide the server settings
under the `lsp.ruff.initialization_options.settings`

key of your `settings.json`

file:

```
{
"lsp": {
"ruff": {
"initialization_options": {
"settings": {
// Ruff server settings go here
"lineLength": 80,
"lint": {
"extendSelect": ["I"],
}
}
}
}
}
}
```

`format_on_save`

is enabled by default.
You can disable it for Python by changing `format_on_save`

in your `settings.json`

file:

You can configure Ruff to fix lint violations and/or organize imports on-save by enabling the
`source.fixAll.ruff`

and `source.organizeImports.ruff`

code actions respectively:
