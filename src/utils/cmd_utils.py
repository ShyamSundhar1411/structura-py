import os
import subprocess

import typer
import yaml

from src.models.dependency_model import EnvDependencyModel
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


def initialize_env_manager(project: ProjectModel) -> None:
    file_path = os.path.join(
        os.path.dirname(__file__), "..", "templates", "default_dependencies.yaml"
    )
    with open(file_path) as file:
        yaml_data = yaml.safe_load(file)

    env_data = next(
        (item for item in yaml_data if item["name"] == project.env_manager), None
    )

    path = project.path
    if env_data:
        env_model = EnvDependencyModel(**env_data)
        try:
            log_message("Running pre_install command...")
            subprocess.run(env_model.pre_install, shell=True, cwd=path, check=True)
            log_message("Running initial setup command ...")
            subprocess.run(
                env_model.setup_environment, shell=True, cwd=path, check=True
            )
            subprocess.run(env_model.post_install, shell=True, cwd=path, check=True)
            log_message(f"✅ {env_model.name} initialized.")
        except subprocess.CalledProcessError as e:
            log_message(f"⚠️ Error running {env_data['name']} command: {e}")
    else:
        log_message("No environment manager selected. Skipping initialization.")
