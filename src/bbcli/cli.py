import click
from bbcli.commands.auth import auth
from bbcli.commands.pr import pr


@click.group()
def cli():
    """bb — Bitbucket CLI."""


cli.add_command(auth)
cli.add_command(pr)
