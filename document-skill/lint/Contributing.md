# Run once on your "baseline" code
cargo bench -p ruff_benchmark -- --save-baseline=main
# Then iterate with
cargo bench -p ruff_benchmark -- --baseline=main
```

#### PR Summary

You can use `--save-baseline`

and `critcmp`

to get a pretty comparison between two recordings.
This is useful to illustrate the improvements of a PR.

```
# On main
cargo bench -p ruff_benchmark -- --save-baseline=main
# After applying your changes
cargo bench -p ruff_benchmark -- --save-baseline=pr
critcmp main pr
```

You must install `critcmp`

for the comparison.

#### Tips

- Use
`cargo bench -p ruff_benchmark <filter>`

to only run specific benchmarks. For example:`cargo bench -p ruff_benchmark lexer`

to only run the lexer benchmarks. - Use
`cargo bench -p ruff_benchmark -- --quiet`

for a more cleaned up output (without statistical relevance) - Use
`cargo bench -p ruff_benchmark -- --quick`

to get faster results (more prone to noise)

### Profiling Projects

You can either use the microbenchmarks from above or a project directory for benchmarking. There are a lot of profiling tools out there, The Rust Performance Book lists some examples.

#### Linux

Install `perf`

and build `ruff_benchmark`

with the `profiling`

profile and then run it with perf

```
cargo bench -p ruff_benchmark --no-run --profile=profiling && perf record --call-graph dwarf -F 9999 cargo bench -p ruff_benchmark --profile=profiling -- --profile-time=1
```

You can also use the `ruff_dev`

launcher to run `ruff check`

multiple times on a repository to
gather enough samples for a good flamegraph (change the 999, the sample rate, and the 30, the number
of checks, to your liking)

```
cargo build --bin ruff_dev --profile=profiling
perf record -g -F 999 target/profiling/ruff_dev repeat --repeat 30 --exit-zero --no-cache path/to/cpython > /dev/null
```

Then convert the recorded profile

You can now view the converted file with firefox profiler. To learn more about Firefox profiler, read the Firefox profiler profiling-guide.

An alternative is to convert the perf data to `flamegraph.svg`

using
flamegraph (`cargo install flamegraph`

):

#### Mac

Install `cargo-instruments`

:

Then run the profiler with

`-t`

: Specifies what to profile. Useful options are`time`

to profile the wall time and`alloc`

for profiling the allocations.- You may want to pass an additional filter to run a single test file

Otherwise, follow the instructions from the linux section.

`cargo dev`

`cargo dev`

is a shortcut for `cargo run --package ruff_dev --bin ruff_dev`

. You can run some useful
utils with it:

`cargo dev print-ast <file>`

: Print the AST of a python file using Ruff's Python parser. For`if True: pass # comment`

, you can see the syntax tree, the byte offsets for start and stop of each node and also how the`:`

token, the comment and whitespace are not represented anymore:

```
[
If(
StmtIf {
range: 0..13,
test: Constant(
ExprConstant {
range: 3..7,
value: Bool(
true,
),
kind: None,
},
),
body: [
Pass(
StmtPass {
range: 9..13,
},
),
],
orelse: [],
},
),
]
```

`cargo dev print-tokens <file>`

: Print the tokens that the AST is built upon. Again for`if True: pass # comment`

:

`cargo dev print-cst <file>`

: Print the CST of a Python file using LibCST, which is used in addition to the RustPython parser in Ruff. For example, for`if True: pass # comment`

, everything, including the whitespace, is represented:

```
Module {
body: [
Compound(
If(
If {
test: Name(
Name {
value: "True",
lpar: [],
rpar: [],
},
),
body: SimpleStatementSuite(
SimpleStatementSuite {
body: [
Pass(
Pass {
semicolon: None,
},
),
],
leading_whitespace: SimpleWhitespace(
" ",
),
trailing_whitespace: TrailingWhitespace {
whitespace: SimpleWhitespace(
" ",
),
comment: Some(
Comment(
"# comment",
),
),
newline: Newline(
None,
Real,
),
},
},
),
orelse: None,
leading_lines: [],
whitespace_before_test: SimpleWhitespace(
" ",
),
whitespace_after_test: SimpleWhitespace(
"",
),
is_elif: false,
},
),
),
],
header: [],
footer: [],
default_indent: " ",
default_newline: "\n",
has_trailing_newline: true,
encoding: "utf-8",
}
```

`cargo dev generate-all`

: Update`ruff.schema.json`

,`docs/configuration.md`

and`docs/rules`

. You can also set`RUFF_UPDATE_SCHEMA=1`

to update`ruff.schema.json`

during`cargo test`

.`cargo dev generate-cli-help`

,`cargo dev generate-docs`

and`cargo dev generate-json-schema`

: Update just`docs/configuration.md`

,`docs/rules`

and`ruff.schema.json`

respectively.`cargo dev generate-options`

: Generate a markdown-compatible table of all`pyproject.toml`

options. Used for https://docs.astral.sh/ruff/settings/.`cargo dev generate-rules-table`

: Generate a markdown-compatible table of all rules. Used for https://docs.astral.sh/ruff/rules/.`cargo dev round-trip <python file or jupyter notebook>`

: Read a Python file or Jupyter Notebook, parse it, serialize the parsed representation and write it back. Used to check how good our representation is so that fixes don't rewrite irrelevant parts of a file.`cargo dev format_dev`

: See ruff_python_formatter README.md

## Subsystems

### Compilation Pipeline

If we view Ruff as a compiler, in which the inputs are paths to Python files and the outputs are diagnostics, then our current compilation pipeline proceeds as follows:

-
**File discovery**: Given paths like`foo/`

, locate all Python files in any specified subdirectories, taking into account our hierarchical settings system and any`exclude`

options. -
**Package resolution**: Determine the "package root" for every file by traversing over its parent directories and looking for`__init__.py`

files. -
**Cache initialization**: For every "package root", initialize an empty cache. -
**Analysis**: For every file, in parallel:-
**Cache read**: If the file is cached (i.e., its modification timestamp hasn't changed since it was last analyzed), short-circuit, and return the cached diagnostics. -
**Tokenization**: Run the lexer over the file to generate a token stream. -
**Indexing**: Extract metadata from the token stream, such as: comment ranges,`# noqa`

locations,`# isort: off`

locations, "doc lines", etc. -
**Token-based rule evaluation**: Run any lint rules that are based on the contents of the token stream (e.g., commented-out code). -
**Filesystem-based rule evaluation**: Run any lint rules that are based on the contents of the filesystem (e.g., lack of`__init__.py`

file in a package). -
**Logical line-based rule evaluation**: Run any lint rules that are based on logical lines (e.g., stylistic rules). -
**Parsing**: Run the parser over the token stream to produce an AST. (This consumes the token stream, so anything that relies on the token stream needs to happen before parsing.) -
**AST-based rule evaluation**: Run any lint rules that are based on the AST. This includes the vast majority of lint rules. As part of this step, we also build the semantic model for the current file as we traverse over the AST. Some lint rules are evaluated eagerly, as we iterate over the AST, while others are evaluated in a deferred manner (e.g., unused imports, since we can't determine whether an import is unused until we've finished analyzing the entire file), after we've finished the initial traversal. -
**Import-based rule evaluation**: Run any lint rules that are based on the module's imports (e.g., import sorting). These could, in theory, be included in the AST-based rule evaluation phase — they're just separated for simplicity. -
**Physical line-based rule evaluation**: Run any lint rules that are based on physical lines (e.g., line-length). -
**Suppression enforcement**: Remove any violations that are suppressed via`# noqa`

directives or`per-file-ignores`

. -
**Cache write**: Write the generated diagnostics to the package cache using the file as a key.

-
-
**Reporting**: Print diagnostics in the specified format (text, JSON, etc.), to the specified output channel (stdout, a file, etc.).

### Import Categorization

To understand Ruff's import categorization system, we first need to define two concepts:

- "Project root": The directory containing the
`pyproject.toml`

,`ruff.toml`

, or`.ruff.toml`

file, discovered by identifying the "closest" such directory for each Python file. (If you're running via`ruff --config /path/to/pyproject.toml`

, then the current working directory is used as the "project root".) - "Package root": The top-most directory defining the Python package that includes a given Python
file. To find the package root for a given Python file, traverse up its parent directories until
you reach a parent directory that doesn't contain an
`__init__.py`

file (and isn't in a subtree marked as a namespace package); take the directory just before that, i.e., the first directory in the package.

For example, given:

Then when analyzing `baz.py`

, the project root would be the top-level directory (`./my_project`

),
and the package root would be `./my_project/src/foo`

.

#### Project root

The project root does not have a significant impact beyond that all relative paths within the loaded configuration file are resolved relative to the project root.

For example, to indicate that `bar`

above is a namespace package (it isn't, but let's run with it),
the `pyproject.toml`

would list `namespace-packages = ["./src/bar"]`

, which would resolve
to `my_project/src/bar`

.

The same logic applies when providing a configuration file via `--config`

. In that case, the
*current working directory* is used as the project root, and so all paths in that configuration file
are resolved relative to the current working directory. (As a general rule, we want to avoid relying
on the current working directory as much as possible, to ensure that Ruff exhibits the same behavior
regardless of where and how you invoke it — but that's hard to avoid in this case.)

Additionally, if a `pyproject.toml`

file *extends* another configuration file, Ruff will still use
the directory containing that `pyproject.toml`

file as the project root. For example, if
`./my_project/pyproject.toml`

contains:

Then Ruff will use `./my_project`

as the project root, even though the configuration file extends
`/path/to/pyproject.toml`

. As such, if the configuration file at `/path/to/pyproject.toml`

contains
any relative paths, they will be resolved relative to `./my_project`

.

If a project uses nested configuration files, then Ruff would detect multiple project roots, one for each configuration file.

#### Package root

The package root is used to determine a file's "module path". Consider, again, `baz.py`

. In that
case, `./my_project/src/foo`

was identified as the package root, so the module path for `baz.py`

would resolve to `foo.bar.baz`

— as computed by taking the relative path from the package root
(inclusive of the root itself). The module path can be thought of as "the path you would use to
import the module" (e.g., `import foo.bar.baz`

).

The package root and module path are used to, e.g., convert relative to absolute imports, and for import categorization, as described below.

#### Import categorization

When sorting and formatting import blocks, Ruff categorizes every import into one of five categories:

**"Future"**: the import is a`__future__`

import. That's easy: just look at the name of the imported module!**"Standard library"**: the import comes from the Python standard library (e.g.,`import os`

). This is easy too: we include a list of all known standard library modules in Ruff itself, so it's a simple lookup.**"Local folder"**: the import is a relative import (e.g.,`from .foo import bar`

). This is easy too: just check if the import includes a`level`

(i.e., a dot-prefix).**"First party"**: the import is part of the current project. (More on this below.)**"Third party"**: everything else.

The real challenge lies in determining whether an import is first-party — everything else is either trivial, or (as in the case of third-party) merely defined as "not first-party".

There are three ways in which an import can be categorized as "first-party":

**Explicit settings**: the import is marked as such via the`known-first-party`

setting. (This should generally be seen as an escape hatch.)**Same-package**: the imported module is in the same package as the current file. This gets back to the importance of the "package root" and the file's "module path". Imagine that we're analyzing`baz.py`

above. If`baz.py`

contains any imports that appear to come from the`foo`

package (e.g.,`from foo import bar`

or`import foo.bar`

), they'll be classified as first-party automatically. This check is as simple as comparing the first segment of the current file's module path to the first segment of the import.**Source roots**: Ruff supports a`src`

setting, which sets the directories to scan when identifying first-party imports. The algorithm is straightforward: given an import, like`import foo`

, iterate over the directories enumerated in the`src`

setting and, for each directory, check for the existence of a subdirectory`foo`

or a file`foo.py`

.

By default, `src`

is set to the project root, along with `"src"`

subdirectory in the project root.
This ensures that Ruff supports both flat and "src" layouts out of the box.
