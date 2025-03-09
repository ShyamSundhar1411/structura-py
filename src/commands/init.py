from pathlib import Path

import typer
from pydantic import ValidationError

from src.models.project_model import ProjectModel
from src.utils.prompt_utils import input_prompt, select_prompt

init_app = typer.Typer()


@init_app.command()
def init():
    project_name = input_prompt(
        field="project_name", message="Project Name", default="my-project"
    )
    project_path = input_prompt(
        field="project_path", message="Project Path", default=str(Path.cwd())
    )
    project_description = input_prompt(
        field="project_description", message="A new python project", default=""
    )
    project_architecture = select_prompt(
        field="project_architecture",
        message="Project Architecture",
        choices=["MVC", "MVC-API", "MVCS", "Hexagonal"],
    )
    try:
        project_data = ProjectModel(
            name=project_name,
            path=project_path,
            description=project_description,
            architecture=project_architecture,
        )
        typer.echo(f"✅ Project initialized:\n{project_data.model_dump_json(indent=2)}")
    except ValidationError as e:
        typer.echo("❌ Error: Invalid project data")
        typer.echo(e)
