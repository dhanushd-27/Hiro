docker-up:
	cd infra && docker-compose up -d

docker-down:
	cd infra && docker-compose down -v

server-up:
	cd apps/server && uv run uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload --no-access-log

web-up:
	cd apps/web && yarn dev
