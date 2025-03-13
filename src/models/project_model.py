import os
from typing import Literal

from pydantic import BaseModel, Field, field_validator

SERVER_CHOICES = {
    "🧪 Flask": "Flask",
    "⚡ FastAPI": "FastAPI",
    "⭕ None": "None",
}


class ProjectModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Project Name")
    path: str = Field(..., min_length=1, max_length=50, description="Project Path")
    description: str = Field(
        ..., min_length=3, max_length=50, description="Project Description"
    )
    architecture: Literal["MVC", "MVC-API", "MVCS", "Hexagonal"] = Field(
        ..., description="Project Architecture"
    )
    server: Literal["Flask", "FastAPI", "None"] = Field(
        ..., description="Server Framework"
    )

    @field_validator("path")
    def validate_path(cls, value):
        """Ensure the path is valid (absolute or relative) and create if needed."""
        abs_path = os.path.abspath(value)
        return abs_path

    @classmethod
    def map_server_choice(cls, user_input: str) -> str:
        """Convert emoji-based user input into valid server values."""
        return SERVER_CHOICES.get(user_input, "None")
