from enum import Enum


class ProjectType(Enum):
    MVC = "MVC"
    MVC_API = "MVC-API"
    MVCS = "MVCS"
    HEXAGONAL = "Hexagonal"
    NONE = "None"

    @classmethod
    def choices(cls):
        return [project_type.value for project_type in cls]


class EnvManager(Enum):
    UV = "uv"
    POETRY = "Poetry"
    PIPENV = "Pipenv"
    VENV = "venv"
    NONE = "None"

    @classmethod
    def choices(cls):
        return [env_manager.value for env_manager in cls]


class ServerType(Enum):
    FLASK = "flask"
    FASTAPI = "fastapi"
    NONE = "None"

    @classmethod
    def choices(cls):
        return [server_type.value for server_type in cls]
