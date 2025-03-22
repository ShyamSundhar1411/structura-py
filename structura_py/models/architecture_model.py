from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field


class ArchitectureModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Architecture Name")
    description: str = Field(
        ..., min_length=3, max_length=10000, description="Architecture Description"
    )
    readme: str = Field(..., description="Architecture Readme")
    folders: Union[Dict[str, Any], List[Union[str, Dict[str, Any]]]] = Field(
        ..., description="Architecture Folders"
    )
