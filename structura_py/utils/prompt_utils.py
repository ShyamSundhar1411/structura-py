from inquirer import List, Text


def input_prompt(field: str, message: str, default: str = None) -> str:
    prompt = Text(field, message=message, default=default)
    return prompt


def select_prompt(field: str, message: str, choices: list[str]) -> str:
    prompt = List(field, message=message, choices=choices)
    return prompt
