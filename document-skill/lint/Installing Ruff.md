# Installing Ruff

Ruff is available as `ruff`

on PyPI.

Ruff can be invoked directly with `uvx`

:

```
uvx ruff check # Lint all files in the current directory.
uvx ruff format # Format all files in the current directory.
```

Or installed with `uv`

(recommended), `pip`

, or `pipx`

:

```
$ # Install Ruff globally.
$ uv tool install ruff@latest
$ # Or add Ruff to your project.
$ uv add --dev ruff
$ # With pip.
$ # With pipx.
$ pipx install ruff
```

Once installed, you can run Ruff from the command line:

```
$ ruff check # Lint all files in the current directory.
$ ruff format # Format all files in the current directory.
```

Starting with version `0.5.0`

, Ruff can also be installed with our standalone installers:

```
$ # On macOS and Linux.
$ curl -LsSf https://astral.sh/ruff/install.sh | sh
$ # On Windows.
$ powershell -c "irm https://astral.sh/ruff/install.ps1 | iex"
$ # For a specific version.
$ curl -LsSf https://astral.sh/ruff/0.5.0/install.sh | sh
$ powershell -c "irm https://astral.sh/ruff/0.5.0/install.ps1 | iex"
```

For **macOS Homebrew** and **Linuxbrew** users, Ruff is also available
as `ruff`

on Homebrew:

For **Conda** users, Ruff is also available as `ruff`

on
`conda-forge`

:

For **pkgx** users, Ruff is also available as `ruff`

on the `pkgx`

registry:

For **Arch Linux** users, Ruff is also available as `ruff`

on the official repositories:

For **Alpine** users, Ruff is also available as `ruff`

on the testing repositories:

For **openSUSE Tumbleweed** users, Ruff is also available in the distribution repository:

On **Docker**, it is published as `ghcr.io/astral-sh/ruff`

, tagged for each release and `latest`

for
the latest release.
