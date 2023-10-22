# File for development process

COMPOSE = docker compose
FILE = docker-compose.dev.yaml
CONTAINERS = $$(docker ps -q)

run:
	$(COMPOSE) -f $(FILE) up -d

restart:
	docker restart $(CONTAINERS)

migration:
	make $(restart)
	docker exec telegram_bot alembic revision --autogenerate

migrate:
	docker exec telegram_bot alembic upgrade head

stop:
	docker stop $(CONTAINERS)