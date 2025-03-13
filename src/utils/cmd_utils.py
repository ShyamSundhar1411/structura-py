import subprocess

import typer

from src.models.project_model import ProjectModel


def log_message(message: str) -> None:
    typer.echo(message)


def run_git_operations(path: str) -> None:
    try:
        subprocess.run(["git", "init"], cwd=path, check=True)
        log_message("✅ An empty repository initialized.")
    except subprocess.CalledProcessError as e:
        log_message(f"⚠️ Error running Git command: {e}")


def run_dependency_installations(project: ProjectModel) -> None:
    try:
        pass
    except subprocess.CalledProcessError as e:
        log_message(f"⚠️ Error running pip command: {e}")
