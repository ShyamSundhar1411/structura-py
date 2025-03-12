import os
from typing import Union

from .cmd_utils import log_message


def create_folders(base_path: str, folder_structure: Union[str, list]):
    if isinstance(folder_structure, list):
        for folder in folder_structure:
            try:
                os.makedirs(os.path.join(base_path, folder), exist_ok=True)
                log_message(f"Created folder: {folder}")
            except Exception as e:
                log_message(f"⚠️ Error creating folder {folder}: {e}")
    elif isinstance(folder_structure, dict):
        for folder, subfolders in folder_structure.items():
            try:
                os.makedirs(os.path.join(base_path, folder), exist_ok=True)
                log_message(f"Created folder: {folder}")
                create_folders(os.path.join(base_path, folder), subfolders)
            except Exception as e:
                log_message(f"⚠️ Error creating folder {folder}: {e}")
    else:
        log_message(f"⚠️ Invalid folder structure format: {folder_structure}")
