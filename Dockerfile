FROM python:latest

RUN pip install poetry

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY update_poetry_dependencies ./update_poetry_dependencies/

ENTRYPOINT ["poetry", "run", "python", "update_poetry_dependencies/main.py"]
