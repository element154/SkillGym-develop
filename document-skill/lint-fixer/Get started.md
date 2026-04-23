Biome is best installed as a development dependency of your projects, but it is
also available as a standalone executable that doesn’t require Node.js.

npm i -D -E @biomejs/biome

pnpm add -D -E @biomejs/biome

bun add -D -E @biomejs/biome

deno add -D npm:@biomejs/biome

yarn add -D -E @biomejs/biome

Although Biome can run with zero configuration, you’ll likely want to tweak some
settings to suit your project’s needs, in which case you can run the following
command to generate a `biome.json`

configuration file.

bunx --bun @biomejs/biome init

deno run -A npm:@biomejs/biome init

Lets get a quick overview of how to use Biome in your project.

Biome provides a command-line interface to format, lint, and check your code.

npx @biomejs/biome format --write

npx @biomejs/biome format --write <files>

# Lint files and apply safe fixes to all files

npx @biomejs/biome lint --write

# Lint files and apply safe fixes to specific files

npx @biomejs/biome lint --write <files>

# Format, lint, and organize imports of all files

npx @biomejs/biome check --write

# Format, lint, and organize imports of specific files

npx @biomejs/biome check --write <files>

pnpx @biomejs/biome format --write

pnpx @biomejs/biome format --write <files>

# Lint and apply safe fixes to all files

pnpx @biomejs/biome lint --write

# Lint files and apply safe fixes to specific files

pnpx @biomejs/biome lint --write <files>

# Format, lint, and organize imports of all files

pnpx @biomejs/biome check --write

# Format, lint, and organize imports of specific files

pnpx @biomejs/biome check --write <files>

bunx --bun @biomejs/biome format --write

bunx --bun @biomejs/biome format --write <files>

# Lint and apply safe fixes to all files

bunx --bun @biomejs/biome lint --write

# Lint files and apply safe fixes to specific files

bunx --bun @biomejs/biome lint --write <files>

# Format, lint, and organize imports of all files

bunx --bun @biomejs/biome check --write

# Format, lint, and organize imports of specific files

bunx --bun @biomejs/biome check --write <files>

deno run -A npm:@biomejs/biome format --write <files>

deno run -A npm:@biomejs/biome format --write

# Lint files and apply safe fixes to all files

deno run -A npm:@biomejs/biome lint --write

# Lint files and apply safe fixes to specific files

deno run -A npm:@biomejs/biome lint --write <files>

# Format, lint, and organize imports of all files

deno run -A npm:@biomejs/biome check --write

# Format, lint, and organize imports of specific files

deno run -A npm:@biomejs/biome check --write <files>

yarn exec biome format --write

yarn exec biome format --write <files>

# Lint files and apply safe fixes to all files

yarn exec biome lint --write

# Lint files and apply safe fixes to specific files

yarn exec biome lint --write <files>

# Format, lint, and organize imports of all files

yarn exec biome check --write

# Format, lint, and organize imports of specific files

yarn exec biome check --write <files>

Biome is available as a first-party extension in your favorite editors.

There are also community extensions
for other editors, such as Vim , Neovim , and Sublime Text , to name
a few.

Run `biome ci`

as part of your CI pipeline to enforce code quality and consistency
across your team. It works just like the `biome check`

command, but is optimized for
CI environments.

See the Continuous Integration recipes for more examples.

Success! You’re now ready to use Biome. 🥳
