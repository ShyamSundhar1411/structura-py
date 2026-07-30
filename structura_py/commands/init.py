import os

import click
import typer

from structura_py.utils.cmd_utils import log_message, run_git_operations
from structura_py.utils.constants import EnvManager, ProjectType, ServerType
from structura_py.utils.init_utils import (
    load_structure_from_architecture,
    project_prompt_builder,
)

from . import command_app


@command_app.command("init")
def init(
    name: str = typer.Option(None, "--name", "-n", help="Name of the project"),
    path: str = typer.Option(None, "--path", "-p", help="Path to the project"),
    framework: str = typer.Option(
        None,
        "--framework",
        "-f",
        click_type=click.Choice(ServerType.choices()),
        help="Web Framework to be used",
    ),
    env_manager: str = typer.Option(
        None,
        "--env-manager",
        "-e",
        click_type=click.Choice(EnvManager.choices()),
        help="Environment Manager to be used",
    ),
    project_type: str = typer.Option(
        None,
        "--project-type",
        "-t",
        click_type=click.Choice(ProjectType.choices()),
        help="Project Architecture type",
    ),
):
    project, error = project_prompt_builder(
        name=name,
        path=path,
        framework=framework,
        env_manager=env_manager,
        project_type=project_type,
    )
    if error:
        log_message("❌ Error: Invalid project data")
        log_message(error)
        os._exit(1)
    load_structure_from_architecture(project)
    log_message("✅ Project initialized Successfully")
    run_git_operations(project.path)
