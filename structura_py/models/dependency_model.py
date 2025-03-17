from typing import Dict, Optional

from pydantic import BaseModel, Field


class FileContentModel(BaseModel):
    files: Dict[str, str] = Field(
        ..., description="Mapping of file names to their contents."
    )


class DependencyModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Dependency Name")
    version: str = Field(
        ..., min_length=3, max_length=50, description="Dependency Version"
    )
    description: str = Field(
        ..., min_length=3, max_length=255, description="Dependency Description"
    )
    source: str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="Dependency Source (e.g., URL or repository)",
    )
    content: Dict[str, FileContentModel] = Field(
        ..., description="Dependency content mapping directories to file contents."
    )


class EnvDependencyModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Dependency Name")
    version: str = Field(
        ..., min_length=3, max_length=50, description="Dependency Version"
    )
    description: str = Field(
        ..., min_length=3, max_length=255, description="Dependency Description"
    )
    pre_install: str = Field(
        ..., min_length=3, max_length=255, description="Dependency Pre Install Command"
    )
    post_install: Optional[str] = Field(
        None, description="Dependency Post Install Command"
    )
    setup_environment: Optional[str] = Field(
        None, description="Dependency Setup Environment Command"
    )
