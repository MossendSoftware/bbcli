# bbcli

A fast, git-context-aware Bitbucket CLI for day-to-day developer workflows.

## Installation

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv tool install git+https://github.com/your-org/bbcli
```

Or for local development:

```bash
git clone https://github.com/your-org/bbcli
cd bbcli
uv pip install -e .
```

## Authentication

bbcli uses [Bitbucket API tokens](https://bitbucket.org/account/settings/api-tokens) with scopes.

Create a token with **Pull requests: read & write**, then run:

```bash
bb auth login
```

Credentials are stored at `~/.config/bbcli/credentials.yaml` (mode `600`).

## Usage

### Create a pull request

Run from inside any Bitbucket repository:

```bash
bb pr create
```

bbcli infers the workspace, repo, and source branch from the git remote. You will be prompted for:
- **Title** — pre-filled from the branch name
- **Destination branch** — defaults to `main` or `master`
- **Description** — opens `$EDITOR` with a markdown template

## Commands

| Command | Description |
|---|---|
| `bb auth login` | Save Bitbucket API token to disk |
| `bb pr create` | Create a PR from the current branch |

More commands coming soon: `bb pr list`, `bb pr approve`, `bb pr merge`.

## Contributing

1. Fork the repo and create a branch
2. `uv pip install -e ".[dev]"`
3. Open a PR — the project uses itself for PR workflows

## License

MIT
