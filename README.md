# weather-data-api

A FastAPI service that collects weather data from the public [Open-Meteo](https://open-meteo.com/) APIs, validates it, stores it in PostgreSQL, and serves it through a clean REST API.

**Stack:** Python 3.14 · FastAPI · PostgreSQL · SQLAlchemy · Pydantic · Docker · uv · pytest

> **Status: in progress.** The [Roadmap](#roadmap) shows exactly what works today.

---

## Goal

Build a small but complete backend service, the kind a real team would run in production:

- **Collect** data from an external API reliably (timeouts, errors, retries).
- **Validate** it before it is stored, so bad data never reaches the database.
- **Store** it in PostgreSQL with a schema designed for the queries the API serves.
- **Serve** it through a typed, documented REST API with tests.

Weather data is the subject because it is free, updates constantly and comes in many shapes (forecast, history, air quality, marine). That makes it a good stand-in for any external data a backend has to depend on.

## How it works

```
 Open-Meteo APIs ──► Fetch ──► Transform ──► Validate ──► PostgreSQL
                    (per source)                              │
                                                              ▼
                                                  FastAPI  (REST + OpenAPI docs)
```

1. **Fetch:** one small class per Open-Meteo API, all sharing a base class and a registry.
2. **Transform:** turns the API's parallel arrays (`time[]`, `temperature_2m[]`, …) into rows.
3. **Validate:** rejects null timestamps, duplicates and impossible values before saving.
4. **Store:** idempotent upserts, so fetching the same day twice updates instead of duplicating.
5. **Serve:** endpoints read from PostgreSQL, never from Open-Meteo directly, so the API stays fast and works even when the upstream API is down.

## API

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/health` | Service and database status |
| `GET` | `/sources` | Available data sources from the registry |
| `GET` | `/cities` | Cities that have stored data |
| `GET` | `/weather/{city}/hourly?from=&to=` | Hourly readings for a date range |
| `GET` | `/weather/{city}/daily?from=&to=` | Daily min, max and average |
| `POST` | `/ingest/{source}?city=` | Fetch fresh data for a city and store it |

Interactive docs are generated automatically at `/docs` once the service runs.

## Data model

| Table | Purpose | Unique key |
| --- | --- | --- |
| `cities` | Name, country, latitude, longitude | `name, country` |
| `weather_hourly` | One reading per city per hour | `city_id, ts` |
| `ingestion_runs` | Log of each fetch: source, city, row count, status, time | `id` |

`weather_hourly` has a unique key on `(city_id, ts)`, which is what makes re-running an ingest safe.

## Design decisions

- **The API reads from the database, not from Open-Meteo.** Responses are fast and predictable, and the service keeps working if the upstream API is slow or down.
- **Idempotent upserts** (`INSERT … ON CONFLICT DO UPDATE`). Retries and repeated requests never create duplicate rows.
- **Validation before storage.** Bad rows are rejected with a clear error instead of being saved and discovered later.
- **One registry for all sources.** Adding a new Open-Meteo API means adding one small class; the `/ingest/{source}` endpoint picks it up automatically.
- **Pydantic schemas at the edges.** Request parameters and responses are typed and validated, and that same typing produces the OpenAPI docs.

## Project structure

```
weather-data-api/
  src/weather_data_api/
    api/            # FastAPI app, routers, Pydantic schemas
    ingestion/      # one class per Open-Meteo API + registry
    transform/      # API response → rows
    quality/        # validation rules
    db/             # SQLAlchemy models, session, upserts
  tests/
  docker-compose.yaml
  pyproject.toml
```

## Quickstart

> Fill this in only once `docker compose up` works from a fresh clone.

```bash
git clone https://github.com/amiralicv/weather-data-api.git
cd weather-data-api
cp .env.example .env
docker compose up -d
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs

**Local development:**

```bash
uv sync
uv run pytest
uv run ruff check .
```

## Roadmap

- [x] Fetch from Open-Meteo through a shared base class and registry
- [ ] Transform responses into rows
- [ ] Validation rules with clear errors
- [ ] PostgreSQL schema and idempotent upserts
- [ ] Tests for transform, validation and upserts
- [ ] FastAPI app with `/health` and `/cities`
- [ ] Weather endpoints with date-range queries
- [ ] `POST /ingest/{source}` endpoint
- [ ] `docker compose up` works from a clean clone
- [ ] CI: lint and tests on every push
- [ ] Scheduled ingestion (APScheduler)

Tick a box only when it is true in the repo.

## What I learned

_Filled in as the project grows._

## Author

**Amirali Abbasi** · Backend Developer, Python & FastAPI
[GitHub](https://github.com/amiralicv) · [LinkedIn](https://linkedin.com/in/amirali-abbasi) · [Portfolio](https://amiraliabbasi.ir)
