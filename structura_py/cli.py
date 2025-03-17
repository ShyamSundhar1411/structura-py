import typer

from structura_py.commands import command_app

structura = typer.Typer()
structura.add_typer(command_app)

if __name__ == "__main__":
    structura()
