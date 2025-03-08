import typer

init_app = typer.Typer()


@init_app.command()
def init(project: str):
    typer.echo(f"Initializing project {project}")
