# File for development process

COMPOSE = docker compose
FILE = docker-compose.dev.yaml
CONTAINERS = $$(docker ps -q)

run:
	$(COMPOSE) -f $(FILE) up -d

restart:
	docker restart $(CONTAINERS)

migrate:
	make $(restart)
	docker exec telegram_bot alembic upgrade head