# Backend Template

# Installing
- Install all the requirements in `requirements.txt`
- Run `pre-commit install` and `pre-commit run --all-files`
- Add a .env file with each config in a line like `URL=http://localhost:8000`

# Debugging
- Config file: `.vscode/launch.json`
- Run using: VSCode debugger
- Features: add breakpoints, analyze variables, call stack

# Features
- Fastapi async `server` configured with `router` divided into `api` and `model` folders
- `Routers` are designed as per `Resource` (eg: Author, Book)
- Logging module setup with file logging with daily rotation enabled
- Strictly typed GraphQL objects with `Query` and `Mutation` separated
- GraphQL endpoint `/graphql` with UI to run queries
- Swagger docs on `/docs`
- async SQLAlchemy connection with session manager
- .env file for environment management
- `api/author.py` Example of ease of writing apis between Sqlalchemy - Strawberry - Fastapi
- Pre-commit automations for isort, black and flake8
- Pytest tests `./test.sh`
- Run script `./run.sh`
- Docker Build and push script `./build.sh`

# ToDo
- Alembic integration for table structure management
