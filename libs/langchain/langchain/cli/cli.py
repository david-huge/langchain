"""A CLI for creating a new project with LangChain."""
import typer
from typing_extensions import Annotated

from langchain.cli.create_repo import (
    create,
    get_git_user_email,
    get_git_user_name,
    is_poetry_installed,
)

app = typer.Typer(no_args_is_help=False, add_completion=False)


AUTHOR_NAME_OPTION = typer.Option(
    default_factory=get_git_user_name,
    prompt=True,
    help="If not specified, will be inferred from git config if possible. ",
)
AUTHOR_EMAIL_OPTION = typer.Option(
    default_factory=get_git_user_email,
    prompt=True,
    help="If not specified, will be inferred from git config if possible. ",
)
USE_POETRY_OPTION = typer.Option(
    default_factory=is_poetry_installed,
    prompt=True,
    help=(
        "Whether to use Poetry to manage the project. "
        "If not specified, Poetry will be used if poetry is installed."
    ),
)


@app.command()
def new(
    project_directory: Annotated[str, "The directory to create the project in."],
    author_name: Annotated[str, AUTHOR_NAME_OPTION],
    author_email: Annotated[str, AUTHOR_EMAIL_OPTION],
    use_poetry: Annotated[bool, USE_POETRY_OPTION],
) -> None:
    """Create a new project with LangChain."""
    return create(project_directory, author_name, author_email, use_poetry)


if __name__ == "__main__":
    app()
