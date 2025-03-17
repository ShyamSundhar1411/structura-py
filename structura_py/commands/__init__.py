import typer

from .init import init_app

command_app = typer.Typer()
command_app.add_typer(init_app)
