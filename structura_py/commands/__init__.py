import typer

from .init import init_app

command_app = typer.Typer()

__all__ = ["command_app", "init_app"]
