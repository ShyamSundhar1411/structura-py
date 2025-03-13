import os
from typing import Dict, List, Union

import yaml
from inquirer import prompt
from pydantic import ValidationError

from src.models.architecture_model import ArchitectureModel
from src.models.project_model import ProjectModel
from src.utils.prompt_utils import input_prompt, select_prompt

from .cmd_utils import log_message
from .file_utils import create_folders, create_initial_broiler_plate


def project_prompt_builder():
    prompt_data = []
    prompt_data.append(
        input_prompt(field="project_name", message="Project Name", default="my-project")
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
    prompt_data = prompt(prompt_data)
    try:
        project = ProjectModel(
            name=prompt_data["project_name"],
            path=prompt_data["project_path"],
            description=prompt_data["project_description"],
            architecture=prompt_data["project_architecture"],
        )
        return project, None
    except ValidationError as e:
        return None, str(e)


def print_folder_structure(folder_structure: Union[Dict, List], indent: int = 0):
    """Recursively prints the folder structure from an ArchitectureModel."""
    if isinstance(folder_structure, list):
        for folder in folder_structure:
            log_message("  " * indent + f"📂 {folder}")
    elif isinstance(folder_structure, dict):
        for folder, subfolders in folder_structure.items():
            log_message("  " * indent + f"📂 {folder}")
            print_folder_structure(subfolders, indent + 1)


def load_structure_from_architecture(project: ProjectModel):
    file_name = f"{project.architecture.lower()}.yaml"
    file_path = os.path.join(os.path.dirname(__file__), "..", "templates", file_name)
    with open(file_path) as file:
        yaml_data = yaml.safe_load(file)

    architecture_structure = ArchitectureModel(**yaml_data)
    print_folder_structure(architecture_structure.folders)
    create_folders(project.path, architecture_structure.folders)
    create_initial_broiler_plate(project)
