FROM python:latest

RUN pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock pyproject.toml ./
RUN poetry install

# Doing this in a second step so that we get layer caching for dependencies
# and the project doesn't invalidate it
COPY update_poetry_dependencies ./update_poetry_dependencies/
RUN poetry install
RUN poetry build
RUN pip install --use-feature=in-tree-build .

ENTRYPOINT ["upd"]
