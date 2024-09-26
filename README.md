
poetry install --no-root

docker compose up --build

alembic upgrade head

poetry run python -m src.main