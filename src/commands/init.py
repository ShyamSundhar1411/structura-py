import os

import typer

from src.utils.init_utils import (
    load_structure_from_architecture,
    project_prompt_builder,
)

init_app = typer.Typer()


@init_app.command()
def init():
    project, error = project_prompt_builder()
    if error:
        typer.echo("❌ Error: Invalid project data")
        typer.echo(error)
        os._exit(1)
    load_structure_from_architecture(project)
    typer.echo("✅ Project initialized:")
    typer.echo("✅ Project data:")
    typer.echo(project)
