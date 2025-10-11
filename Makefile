run:
	docker compose up --build

test:
	docker compose exec api pytest -q

lint:
	docker compose exec api ruff check .

fmt:
	docker compose exec api ruff check . --fix && docker compose exec api black .

typecheck:
	docker compose exec api mypy app
