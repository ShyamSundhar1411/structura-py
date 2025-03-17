from typing import Dict, List, Union

from pydantic import BaseModel, Field


class ArchitectureModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Architecture Name")
    description: str = Field(
        ..., min_length=3, max_length=10000, description="Architecture Description"
    )
    folders: Union[Dict[str, Dict[str, List[str]]], List[str]] = Field(
        ..., description="Architecture Folders"
    )
