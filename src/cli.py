import typer

from src.commands import command_app

structura = typer.Typer()
structura.add_typer(command_app, name="structura")

if __name__ == "__main__":
    structura()
