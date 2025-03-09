from pathlib import Path

import typer
from inquirer import prompt
from pydantic import ValidationError

from src.utils.prompt_utils import input_prompt, select_prompt

init_app = typer.Typer()


@init_app.command()
def init():
    prompt_data = []
    prompt_data.append(
        input_prompt(field="project_name", message="Project Name", default="my-project")
    )
    prompt_data.append(
        input_prompt(
            field="project_path", message="Project Path", default=str(Path.cwd())
        )
    )
    prompt_data.append(
        input_prompt(
            field="project_description",
            message="Project Description",
            default="A new python project",
        )
    )
    prompt_data.append(
        select_prompt(
            field="project_architecture",
            message="Project Architecture",
            choices=["MVC", "MVC-API", "MVCS", "Hexagonal"],
        )
    )
    _ = prompt(prompt_data)
    try:
        typer.echo("🚀 Initializing project...")
        typer.echo("✅ Project initialized:")
    except ValidationError as e:
        typer.echo("❌ Error: Invalid project data")
        typer.echo(e)
