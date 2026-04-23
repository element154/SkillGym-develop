# Ruff

An extremely fast Python linter and code formatter, written in Rust.

*Linting the CPython codebase from scratch.*

- ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
- 🐍 Installable via
`pip`

- 🛠️
`pyproject.toml`

support - 🤝 Python 3.14 compatibility
- ⚖️ Drop-in parity with Flake8, isort, and Black
- 📦 Built-in caching, to avoid re-analyzing unchanged files
- 🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
- 📏 Over 800 built-in rules, with native re-implementations of popular Flake8 plugins, like flake8-bugbear
- ⌨️ First-party editor integrations for VS Code and more
- 🌎 Monorepo-friendly, with hierarchical and cascading configuration

Ruff aims to be orders of magnitude faster than alternative tools while integrating more functionality behind a single, common interface.

Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort, pydocstyle, pyupgrade, autoflake, and more, all while executing tens or hundreds of times faster than any individual tool.

Ruff is extremely actively developed and used in major open-source projects like:

...and many more.

Ruff is backed by Astral, the creators of uv and ty.

Read the launch post, or the original project announcement.

## Testimonials

**Sebastián Ramírez**, creator
of FastAPI:

Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually running and checking the code.

**Nick Schrock**, founder of Elementl,
co-creator of GraphQL:

Why is Ruff a gamechanger? Primarily because it is nearly 1000x faster. Literally. Not a typo. On our largest module (dagster itself, 250k LOC) pylint takes about 2.5 minutes, parallelized across 4 cores on my M1. Running ruff against our

entirecodebase takes .4 seconds.

**Bryan Van de Ven**, co-creator
of Bokeh, original author
of Conda:

Ruff is ~150-200x faster than flake8 on my machine, scanning the whole repo takes ~0.2s instead of ~20s. This is an enormous quality of life improvement for local dev. It's fast enough that I added it as an actual commit hook, which is terrific.

**Timothy Crosley**,
creator of isort:

Just switched my first project to Ruff. Only one downside so far: it's so fast I couldn't believe it was working till I intentionally introduced some errors.

**Tim Abbott**, lead developer of Zulip (also here):

This is just ridiculously fast...

`ruff`

is amazing.
