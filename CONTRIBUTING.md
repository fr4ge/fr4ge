# Contributing

Contributions are welcome!

## Table of Contents

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=1 -->

- [Contributing](#contributing)
  - [Table of Contents](#table-of-contents)
  - [Development Environment Setup](#development-environment-setup)
    - [uv](#uv)
    - [npm](#npm)
    - [pre-commit](#pre-commit)
  - [Running Tests](#running-tests)
  - [Development Tools](#development-tools)
    - [pre-commit-hooks](#pre-commit-hooks)
    - [REUSE](#reuse)
    - [yamllint](#yamllint)
    - [markdownlint-cli2](#markdownlint-cli2)
    - [mdformat](#mdformat)
    - [tombi](#tombi)
  - [Editor Support](#editor-support)
    - [EditorConfig](#editorconfig)
    - [Visual Studio Code](#visual-studio-code)
  - [Licensing](#licensing)
    - [Copyright and License Notices](#copyright-and-license-notices)

<!-- mdformat-toc end -->

## Development Environment Setup

### uv

This project uses [uv](https://docs.astral.sh/uv/) for Python package and project management. Follow the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) to install the `uv` command.

Use `uv` to install the version of python pinned in this project's [`.python-version`](.python-version):

```sh
uv python install
```

Automatically create a Python virtual environment and install project dependencies:

```sh
uv sync
```

Commands exposed by the project and its dependencies (like `fr4ge` or `pytest`) can be run via `uv` without having to activate the python virtual environment in the shell, for example:

```sh
uv run fr4ge
```

Alternatively, to run commands directly (without the `uv run` prefix), activate the python virtual environment in the current shell:

```sh
source .venv/bin/activate
```

Commands can now be run directly:

```sh
fr4ge
```

### npm

A few development dependencies defined in the project's [`package.json`](package.json) file need to be installed via [npm](https://www.npmjs.com/). Follow the [npm installation guide](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) to install the `npm` command.

Use `npm` to install the dependencies:

```sh
npm install
```

### pre-commit

This project uses [pre-commit](https://pre-commit.com/) to identify simple issues before submission to code review. Although these checks are also run automatically in CI, it is strongly recommended that you install `pre-commit` locally to catch these issues *before* a commit is created in the repository.

The `uv` setup instructions above automatically install the `pre-commit` command into the Python virtual environment. Run the following commands to complete the pre-commit setup (i.e. install the git pre-commit hooks defined by this project's [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file):

```sh
uv run pre-commit install

# (Optional) run all pre-commit hooks on all files in the repository
uv run pre-commit run --all
```

You can configure `git` to automatically install `pre-commit` hooks when a new repository is cloned (rather than having to run `pre-commit install` manually). Follow the recommended setup instructions:

<https://pre-commit.com/#pre-commit-init-templatedir>

## Running Tests

Tests can be run via the [pytest](https://docs.pytest.org/en/stable/) framework:

```sh
uv run pytest
```

## Development Tools

After setting up the development environment, the following tools are available.

### pre-commit-hooks

The [pre-commit](https://pre-commit.com/) developers provide an [official set of pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks). These hooks are installed and run automatically via `pre-commit`, but they are also installed in the virtual environment so that each hook can be run as a command outside of the pre-commit framework.

For example, to run the `check-json` CLI tool:

```sh
# Check a json file
uv run check-json .vscode/extensions.json
```

### REUSE

This project uses the [`reuse`](https://reuse.software/) tool to ensure that all files have copyright and license information. REUSE compliance is checked automatically via a pre-commit hook, but it's also possible to run the `reuse` CLI tool manually:

```sh
# Lint all files in the project
uv run reuse lint
```

### yamllint

[`yamllint`](https://yamllint.readthedocs.io/en/stable/index.html) is a linter for YAML files. It is run automatically as a pre-commit hook, but it's also possible to run the `yamllint` CLI tool manually:

```sh
# Lint YAML files in the current directory tree
uv run yamllint .
```

### markdownlint-cli2

[`markdownlint-cli2`](https://github.com/DavidAnson/markdownlint-cli2) is a command-line interface for linting Markdown files. It is run automatically as a pre-commit hook, but it's also possible to run the `markdownlint-cli2` CLI tool manually:

```sh
# Lint markdown files in the current directory tree
npx markdownlint-cli2 .
```

### mdformat

[`mdformat`](https://mdformat.readthedocs.io/en/stable/index.html) is an opinionated Markdown formatter that can be used to enforce a consistent style in Markdown files. It is run automatically as a pre-commit hook, but it's also possible to run the `mdformat` CLI tool manually:

```sh
# Format markdown files in the current directory tree
uv run mdformat .
```

### tombi

[`tombi`](http://tombi-toml.github.io/tombi/) is a toolkit for TOML files that supports linting and formatting. It is run automatically as a pre-commit hook, but it's also possible to run the `tombi` CLI tool manually.

```sh
# Lint TOML files in the current directory tree
tombi lint

# Format TOML files in the current directory tree
tombi format
```

## Editor Support

### EditorConfig

An [EditorConfig](https://editorconfig.org/) config file ([`.editorconfig`](.editorconfig)) is provided to allow supported editors to automatically configure coding style settings for this project.

### Visual Studio Code

Opening this project in VS Code will open a prompt to install the set of [workspace recommended extensions](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_workspace-recommended-extensions) defined in [`.vscode/extensions.json`](.vscode/extensions.json).

## Licensing

See [LICENSE.md](LICENSE.md) for details on this project's licensing information.

### Copyright and License Notices

This project uses [SPDX](https://spdx.dev/)/[REUSE](https://reuse.software/)-style file headers:

<!-- REUSE-IgnoreStart -->

```plaintext
SPDX-FileCopyrightText: Your Name <https://your.website>
SPDX-License-Identifier: <SPDX License ID>
```

<!-- REUSE-IgnoreEnd -->

Place both lines at the very top of the file using the file’s native comment syntax (make sure to replace `<SPDX License ID>` with the actual [SPDX License ID](https://spdx.org/licenses/)). If the file type does not support adding comments, the copyright & license notices may be added to the project's [REUSE.toml](REUSE.toml) file.

If you authored substantial, original content, you may add an additional copyright line for yourself or your organization.
