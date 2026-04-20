import click
from rich.console import Console

from bbcli import api, config

console = Console()


@click.group()
def auth():
    """Manage Bitbucket credentials."""


@auth.command()
def login():
    """Save Bitbucket credentials to ~/.config/bbcli/credentials.yaml."""
    console.print("\n[bold]Bitbucket login[/bold]")
    console.print(
        "Create an API token at: "
        "[link]https://bitbucket.org/account/settings/personal-access-tokens[/link]\n"
    )

    email = click.prompt("Email")
    api_token = click.prompt("API token", hide_input=True)

    console.print("\n[dim]Verifying token...[/dim]")
    try:
        user = api.verify_credentials(email, api_token)
    except RuntimeError as e:
        console.print(f"\n[red]Login failed:[/red] {e}")
        raise SystemExit(1)

    config.save_credentials(email, api_token)
    console.print(
        f"\n[green]✓[/green] Logged in as [bold]{user.get('display_name', email)}[/bold]"
    )
    console.print(f"[dim]Credentials saved to {config.CREDENTIALS_FILE}[/dim]\n")
