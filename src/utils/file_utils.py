import os
from typing import Optional, Union

import yaml

from src.models.dependency_model import DependencyModel, FileContentModel
from src.models.project_model import ProjectModel

from .cmd_utils import log_message


def create_init_files(base_path: str) -> None:
    """
    Traverse all folders inside `base_path` and create an `__init__.py` file in each folder.

    Args:
        base_path (str): The base path where the folders are located.
    """

    for root, dirs, _ in os.walk(base_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            init_file_path = os.path.join(dir_path, "__init__.py")
            if not os.path.exists(init_file_path):
                with open(init_file_path, "w") as init_file:
                    init_file.write(
                        "# This is an empty __init__.py file for the folder: "
                        + dir_name
                    )


def create_folders(base_path: str, folder_structure: Union[str, list]):
    if isinstance(folder_structure, list):
        for folder in folder_structure:
            try:
                os.makedirs(os.path.join(base_path, folder), exist_ok=True)
                log_message(f"Created folder: {folder}")
            except Exception as e:
                log_message(f"⚠️ Error creating folder {folder}: {e}", level="ERROR")
    elif isinstance(folder_structure, dict):
        for folder, subfolders in folder_structure.items():
            try:
                os.makedirs(os.path.join(base_path, folder), exist_ok=True)
                log_message(f"Created folder: {folder}")
                create_folders(os.path.join(base_path, folder), subfolders)
            except Exception as e:
                log_message(f"⚠️ Error creating folder {folder}: {e}", level="ERROR")
    else:
        log_message(
            f"⚠️ Invalid folder structure format: {folder_structure}", level="ERROR"
        )


def create_files_from_dependencies(
    project: ProjectModel, dependencies: DependencyModel
):
    app_path = project.get_app_path()
    for folder, file_content in dependencies.content.items():
        if folder == "root":
            folder_path = project.path
        elif folder == "app":
            folder_path = os.path.join(app_path)
        else:
            folder_path = os.path.join(app_path, folder)
        for file_name, content in file_content.files.items():
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, "w") as file:
                    file.write(content)
                log_message(f"Created file: {file_path}")
            except Exception as e:
                log_message(f"⚠️ Error creating file {file_path}: {e}", level="ERROR")


def create_initial_broiler_plate(project: ProjectModel):
    log_message("Creating initial boilerplate...")
    file_name = "initial_structure.yaml"
    file_path = os.path.join(os.path.dirname(__file__), "..", "templates", file_name)
    with open(file_path) as file:
        yaml_data = yaml.safe_load(file)
    yaml_data["content"] = {
        key: FileContentModel(files=value)
        for key, value in yaml_data["content"].items()
    }
    initial_dependency_data = DependencyModel(**yaml_data)
    create_files_from_dependencies(project, initial_dependency_data)


def create_files_for_server(project: ProjectModel) -> Optional[DependencyModel]:
    if project.server == "None":
        return None
    log_message("Creating server files...")
    file_name = f"{project.server}_server.yaml"
    file_path = os.path.join(os.path.dirname(__file__), "..", "templates", file_name)
    with open(file_path) as file:
        yaml_content = file.read()
    yaml_content = yaml_content.replace("{{APP_NAME}}", project.name)
    yaml_data = yaml.safe_load(yaml_content)
    yaml_data["content"] = {
        key: FileContentModel(files=value)
        for key, value in yaml_data["content"].items()
    }
    server_dependency_data = DependencyModel(**yaml_data)
    create_files_from_dependencies(project, server_dependency_data)
    return server_dependency_data
