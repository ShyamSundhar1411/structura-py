import typer

from src.utils.init_utils import project_prompt_builder

init_app = typer.Typer()


@init_app.command()
def init():
    project, error = project_prompt_builder()
    if error:
        typer.echo("❌ Error: Invalid project data")
        typer.echo(error)
    else:
        typer.echo("✅ Project initialized:")
        typer.echo("✅ Project data:")
        typer.echo(project)
