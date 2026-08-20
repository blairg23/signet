"""signet CLI entrypoint."""

from __future__ import annotations

import typer

from signet import __version__
from signet.clients import new_client
from signet.config import load_config

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(False, "--version", help="Show the version and exit."),
) -> None:
    if version:
        typer.echo(f"signet {__version__}")
        raise typer.Exit()


@app.command()
def doctor() -> None:
    """Check the environment: config presence and data_dir reachability."""
    problems: list[str] = []

    config = load_config()
    if not config.data_dir.exists():
        problems.append(f"data_dir does not exist: {config.data_dir}")

    if problems:
        for problem in problems:
            typer.echo(f"FAIL  {problem}")
        raise typer.Exit(code=1)

    typer.echo("OK  environment looks good")


@app.command()
def new(client: str) -> None:
    """Create a new client folder for CLIENT and print its path."""
    config = load_config()
    path = new_client(client, config=config)
    typer.echo(str(path))


if __name__ == "__main__":
    app()
