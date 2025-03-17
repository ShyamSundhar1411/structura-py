import os
import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator

SERVER_CHOICES = {
    "🧪 Flask": "Flask",
    "⚡ FastAPI": "FastAPI",
    "⭕ None": "None",
}


INVALID_NAMES = {"__pycache__", "venv", "env", "site-packages", "dist", "build"}

VALID_NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


class ProjectModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Project Name")
    path: str = Field(..., min_length=1, max_length=50, description="Project Path")
    description: str = Field(
        ..., min_length=3, max_length=50, description="Project Description"
    )
    architecture: Literal["MVC", "MVC-API", "MVCS", "Hexagonal"] = Field(
        ..., description="Project Architecture"
    )
    env_manager: Literal["Poetry", "Pipenv", "venv", "None"] = Field(
        ..., description="Environment Manager"
    )
    server: Literal["Flask", "FastAPI", "None"] = Field(
        ..., description="Server Framework"
    )

    @field_validator("path")
    def validate_path(cls, value):
        """Ensure the path is valid (absolute or relative) and return the absolute path."""
        return os.path.abspath(value)

    @field_validator("name")
    def validate_name(cls, value):
        """Ensure the project name is valid and does not use reserved folder names."""
        if value in INVALID_NAMES:
            raise ValueError(
                f"❌ Invalid project name: '{value}' is a reserved folder name in Python."
            )

        if not VALID_NAME_PATTERN.match(value):
            raise ValueError(
                "❌ Invalid project name: Must start with a letter and contain only letters & numbers (no underscores, spaces, or special characters)."
            )

        return value

    @classmethod
    def map_server_choice(cls, user_input: str) -> str:
        """Convert emoji-based user input into valid server values."""
        return SERVER_CHOICES.get(user_input, "None")

    def get_app_path(self) -> str:
        """Get the absolute application path inside the project directory."""
        return os.path.join(self.path, self.name)
