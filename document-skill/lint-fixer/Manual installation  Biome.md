# Manual installation

Using Biome’s standalone CLI binary can be a great choice if you aren’t already using Node.js or `npm`

(or any other package manager).
Or in other words, Biome shouldn’t be the only reason for you to have a `package.json`

.

## Supported platforms

Section titled “Supported platforms”You have to pick the correct binary for your platform for Biome work. The following table should help you do so.

| CPU Architecture | Windows | macOS | Linux | Linux (musl) |
|---|---|---|---|---|
`arm64` | `win32-arm64` | `darwin-arm64` (M1 or newer) | `linux-arm64` | `linux-arm64-musl` |
`x64` | `win32-x64` | `darwin-x64` | `linux-x64` | `linux-x64-musl` |

## Homebrew

Section titled “Homebrew”Biome is available as a Homebrew formula for macOS and Linux users.

## Arch Linux (x86_64)

Section titled “Arch Linux (x86_64)”Biome is available as a community maintained binary from the Arch Linux Extra repository.

To install Biome run:

## Docker

Section titled “Docker”Biome publishes official Docker images that support
the **amd64** and **arm64** architectures for all Biome versions starting from `v1.7.0`

.

Here are a couple examples on how to use the Docker image:

## Using a published binary

Section titled “Using a published binary”To install Biome, grab the executable for your platform from the latest CLI release on GitHub and give it execution permission.

Now you can use Biome by simply running `./biome`

.

## Next Steps

Section titled “Next Steps”Follow our Getting Started guide.

Copyright (c) 2023-present Biome Developers and Contributors.
