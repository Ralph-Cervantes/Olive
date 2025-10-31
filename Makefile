.PHONY: up build down logs test-server rebuild info

start:
	@$(MAKE) build
	@$(MAKE) up
	@$(MAKE) remove-tables
	@$(MAKE) create-tables
	@$(MAKE) info

up:
	docker compose up -d --build
	@$(MAKE) info

build:
	docker compose build

down:
	docker compose down

logs:
	docker compose logs -f

test-server:
	docker compose exec server pytest

create-tables:
	docker compose exec server python data/scripts/create_tables.py

remove-tables:
	docker compose exec server python data/scripts/remove_tables.py

rebuild:
	docker compose build --no-cache client

info:
	@echo "---------------------------------"
	@echo "[36mClient (Next.js):[0m http://localhost:3000"
	@echo "[35mServer (FastAPI):[0m http://localhost:8001"
	@echo "---------------------------------"