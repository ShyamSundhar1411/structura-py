import os
import subprocess
import time

import yaml
from rich.console import Console

from structura_py.models.dependency_model import DependencyModel, EnvDependencyModel
from structura_py.models.project_model import ProjectModel

console = Console()


def log_message(
    message: str,
    level: str = "INFO",
    show_loader: bool = False,
    task_name: str = "",
    action_func=None,
) -> None:
    """Log a message to the console using rich with different styles based on level.
    Optionally display a loader while performing a task."""

    styles = {
        "INFO": "white",
        "DEBUG": "italic green",
        "WARNING": "bold yellow",
        "ERROR": "bold red",
        "SUCCESS": "bold green",
    }

    style = styles.get(level.upper(), "bold cyan")

    console.print(message, style=style)

    if show_loader and action_func:
        loader(task_name, action_func)


def loader(task_name: str, action_func) -> None:
    """Show a loading spinner while executing a task"""
    with console.status(f"[bold green]Running {task_name}...[/bold green]"):
        action_func()


def long_running_task() -> None:
    """Simulate a long-running task"""
    time.sleep(5)


def run_subprocess(command: str, cwd: str) -> None:
    """Wrapper function to run a subprocess command"""
    subprocess.run(command, shell=True, cwd=cwd, check=True)


def run_git_operations(path: str) -> None:
    try:
        run_subprocess("git init", path)
        log_message("✅ An empty repository initialized.")
    except subprocess.CalledProcessError as e:
        log_message(f"⚠️ Error running Git command: {e}", level="ERROR")


def run_dependency_installations(
    project: ProjectModel, server: DependencyModel
) -> None:
    try:
        env_manager = project.env_manager.lower()
        path = project.path
        if env_manager == "poetry":
            server_command = f"poetry add {server.source}"
            log_message(
                f"Installing {server.name} Server dependencies",
                show_loader=True,
                task_name="Poetry",
                action_func=lambda: run_subprocess(server_command, path),
            )
        elif env_manager == "pipenv":
            server_command = f"pipenv install {server.source}"
            log_message(
                f"Installing {server.name} Server dependencies",
                show_loader=True,
                task_name="Pipenv",
                action_func=lambda: run_subprocess(server_command, path),
            )
        elif env_manager == "venv":
            server_command = f"python -m venv .venv && .venv\\Scripts\\activate && pip install {server.source}"
            log_message(
                f"Installing {server.name} Server dependencies",
                show_loader=True,
                task_name="Venv",
                action_func=lambda: run_subprocess(server_command, path),
            )
        else:
            server_command = f"pip install {server.source}"
            log_message(
                f"Installing {server.name} Server dependencies",
                show_loader=True,
                task_name="Pip",
                action_func=lambda: run_subprocess(server_command, path),
            )
    except subprocess.CalledProcessError as e:
        log_message(f"⚠️ Error running pip command: {e}", level="ERROR")


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
            log_message(
                "Running pre_install command...",
                show_loader=True,
                task_name="Pre-install",
                action_func=lambda: run_subprocess(env_model.pre_install, path),
            )
            if env_model.setup_environment:
                processed_setup_command = env_model.setup_environment.replace(
                    "{{PROJECT_NAME}}", project.name
                )
                log_message(
                    "Running initial setup command ...",
                    show_loader=True,
                    task_name="Setup",
                    action_func=lambda: run_subprocess(processed_setup_command, path),
                )
            if env_model.post_install:
                log_message(
                    "Running post_install command...",
                    show_loader=True,
                    task_name="Post-install",
                    action_func=lambda: run_subprocess(env_model.post_install, path),
                )

            log_message(f"✅ {env_model.name} initialized.", level="SUCCESS")
        except subprocess.CalledProcessError as e:
            log_message(
                f"⚠️ Error running {env_data['name']} command: {e}", level="ERROR"
            )
    else:
        log_message("No environment manager selected. Skipping initialization.")
