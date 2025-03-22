import os

import typer

from structura_py.utils.cmd_utils import log_message, run_git_operations
from structura_py.utils.init_utils import (
    load_structure_from_architecture,
    project_prompt_builder,
)

init_app = typer.Typer()


@init_app.command()
def init():
    project, error = project_prompt_builder()
    if error:
        log_message("❌ Error: Invalid project data")
        log_message(error)
        os._exit(1)
    load_structure_from_architecture(project)
    log_message("✅ Project initialized Successfully")
    run_git_operations(project.path)
