import os
from typing import Dict, List, Union

import yaml
from inquirer import prompt
from pydantic import ValidationError

from structura_py.models.architecture_model import ArchitectureModel
from structura_py.models.project_model import ProjectModel
from structura_py.utils.prompt_utils import input_prompt, select_prompt

from .cmd_utils import initialize_env_manager, log_message, run_dependency_installations
from .file_utils import (
    create_file,
    create_files_for_server,
    create_folders,
    create_initial_broiler_plate,
)


def project_prompt_builder():
    prompt_data = []
    prompt_data.append(
        input_prompt(field="project_name", message="Project Name", default="my_project")
    )
    prompt_data.append(
        input_prompt(field="project_path", message="Project Path", default="./")
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
    prompt_data.append(
        select_prompt(
            field="project_server",
            message="Server Framework",
            choices=["🧪 Flask", "⚡ FastAPI", "⭕ None"],
        )
    )
    prompt_data.append(
        select_prompt(
            field="project_env_manager",
            message="Environment Manager",
            choices=["Poetry", "Pipenv", "venv", "None"],
        )
    )
    prompt_data = prompt(prompt_data)
    try:
        project = ProjectModel(
            name=prompt_data["project_name"],
            path=prompt_data["project_path"],
            description=prompt_data["project_description"],
            architecture=prompt_data["project_architecture"],
            server=ProjectModel.map_server_choice(prompt_data["project_server"]),
            env_manager=prompt_data["project_env_manager"],
        )
        return project, None
    except ValidationError as e:
        return None, str(e)


def print_folder_structure(folder_structure: Union[Dict, List], indent: int = 0):
    if isinstance(folder_structure, list):
        for item in folder_structure:
            if isinstance(item, str):
                continue
            elif isinstance(item, dict):
                print_folder_structure(item, indent)

    elif isinstance(folder_structure, dict):
        for folder, subfolders in folder_structure.items():
            log_message("  " * indent + f"📂 {folder}")

            if isinstance(subfolders, list):
                for entry in subfolders:
                    if isinstance(entry, str):
                        continue
                    elif isinstance(entry, dict):
                        print_folder_structure(entry, indent + 1)

            elif isinstance(subfolders, dict):
                print_folder_structure(subfolders, indent + 1)


def load_structure_from_architecture(project: ProjectModel):
    file_name = f"{project.architecture.lower()}.yaml"
    file_path = os.path.join(os.path.dirname(__file__), "..", "templates", file_name)
    with open(file_path) as file:
        yaml_data = yaml.safe_load(file)
    architecture_structure = ArchitectureModel(**yaml_data)
    create_folders(project.get_app_path(), architecture_structure.folders)
    create_initial_broiler_plate(project)
    create_file(project.path, "README.md", architecture_structure.readme)
    server_dependencies = create_files_for_server(project)
    initialize_env_manager(project)
    if not server_dependencies:
        log_message(
            "No server dependencies found. Skipping server initializations",
            level="INFO",
        )
        return
    run_dependency_installations(project, server_dependencies)
