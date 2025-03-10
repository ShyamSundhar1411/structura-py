from inquirer import prompt
from pydantic import ValidationError

from src.models.project_model import ProjectModel
from src.utils.prompt_utils import input_prompt, select_prompt


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
