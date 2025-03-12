import subprocess

import typer


def log_message(message: str) -> None:
    typer.echo(message)


def run_git_operations(path) -> None:
    try:
        subprocess.run(["git", "init"], cwd=path, check=True)
        log_message("✅ An empty repository initialized.")
    except subprocess.CalledProcessError as e:
        log_message(f"⚠️ Error running Git command: {e}")
