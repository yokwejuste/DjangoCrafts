# Django Brokers: Valkey, Redis, RabbitMQ and alternatives

A Django project that shows how to plug a message broker into Django with [Celery](https://docs.celeryq.dev/), and how to swap brokers by changing a few environment variables in `.env`. It covers:

1. **Valkey**, the open-source (BSD) fork of Redis maintained by the Linux Foundation
2. **Redis**
3. **RabbitMQ** (4.x, with quorum queues)
4. Other options such as Amazon SQS, KeyDB, Dragonfly and Django's own Tasks framework

The same Valkey/Redis server can also be Django's cache backend, which the project demonstrates with a page-view counter.

## What is a broker?

A broker is a queue that sits between your Django app and background workers. Django puts a message on the queue ("send this email", "build this report") and returns a response straight away. A Celery worker picks the message up and runs the work outside the request/response cycle.

```mermaid
flowchart LR
    A[Django view] -- "task.delay()" --> B[Broker<br/>Valkey / Redis / RabbitMQ]
    B --> C[Celery worker]
    C -- stores result --> D[Result backend<br/>Valkey / Redis]
    D -- "AsyncResult(id)" --> A
```

- **Broker**: carries task messages to workers.
- **Result backend**: stores task state and return values so Django can read them later.

## Project Structure

```
django_brokers/
├── brokers/
│   ├── __init__.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── jobs/
│   ├── tasks.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── templates/
│   ├── _base.html
│   └── home.html
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── .env.example
```

## Installation

### Prerequisites

- Python 3.10+
- Docker (or a locally installed Valkey, Redis or RabbitMQ)

### Setup

1. Go to the project folder:
   ```bash
   cd django_brokers
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` (it points at Valkey by default):
   ```bash
   cp .env.example .env
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Using Valkey

Valkey is wire-compatible with Redis, so Celery, `redis-py` and Django's built-in `RedisCache` work with it unchanged. You use the `redis://` URL scheme.

1. Start Valkey (exposed on port `6380` so it can run next to Redis):
   ```bash
   docker compose --profile valkey up -d
   ```
   Or install it locally: `brew install valkey` / `apt install valkey`, then `valkey-server --port 6380`.

2. Point Django and Celery at it in `.env`:
   ```
   CELERY_BROKER_URL='redis://localhost:6380/0'
   CELERY_RESULT_BACKEND='redis://localhost:6380/1'
   CACHE_URL='redis://localhost:6380/2'
   ```
   Each number at the end is a separate logical database, which keeps task messages, results and cache keys apart.

3. Start a worker in one terminal:
   ```bash
   celery -A brokers worker -l info
   ```

4. Start Django in another:
   ```bash
   python manage.py runserver
   ```

5. Visit `http://localhost:8000`, click **add(2, 3)** or **build_report**, and watch the task move from `PENDING` to `SUCCESS`. Visit `http://localhost:8000/health/` to check that Django can reach the broker and the cache.

For a password-protected or TLS Valkey, use `redis://:password@host:6379/0` or `rediss://:password@host:6380/0`.

> Want a Valkey-native client instead of `redis-py`? [`valkey-py`](https://github.com/valkey-io/valkey-py) and [`django-valkey`](https://github.com/django-commons/django-valkey) exist, but they aren't needed: the Redis clients work with Valkey.

## Using Redis

Same steps as Valkey, with Redis on the default port `6379`:

```bash
docker compose --profile redis up -d
```

```
CELERY_BROKER_URL='redis://localhost:6379/0'
CELERY_RESULT_BACKEND='redis://localhost:6379/1'
CACHE_URL='redis://localhost:6379/2'
```

## Using RabbitMQ

RabbitMQ is a dedicated message broker: it has stronger delivery guarantees (acknowledgements, durable quorum queues) and routing features, but it does not store task results or act as a cache. Pair it with Valkey or Redis for those.

1. Start RabbitMQ and Valkey:
   ```bash
   docker compose --profile rabbitmq --profile valkey up -d
   ```
   The management UI is at `http://localhost:15672` (guest / guest).

2. Configure `.env`:
   ```
   CELERY_BROKER_URL='amqp://guest:guest@localhost:5672//'
   CELERY_RESULT_BACKEND='redis://localhost:6380/1'
   CACHE_URL='redis://localhost:6380/2'
   ```

3. Start the worker without mingle and gossip:
   ```bash
   celery -A brokers worker -l info --without-mingle --without-gossip
   ```

RabbitMQ 4 no longer allows the transient, non-exclusive queues that Celery uses by default. When the broker URL starts with `amqp://`, `settings.py` switches Celery to durable **quorum queues** and turns off remote control. The `--without-mingle --without-gossip` flags stop the worker from declaring its transient broadcast reply queues. For the same reason, don't use the `rpc://` result backend with RabbitMQ 4; store results in Valkey or Redis instead.

## Other alternatives

| Option | Broker URL | Notes |
|---|---|---|
| KeyDB / Dragonfly | `redis://host:6379/0` | Redis-compatible servers, same setup as Valkey |
| Amazon SQS | `sqs://` | `pip install "celery[sqs]"`; needs a separate result backend |
| Google Pub/Sub | `gcpubsub://projects/<project-id>` | `pip install "celery[gcpubsub]"` |
| Django Tasks | n/a | Django 6.0+ ships `django.tasks` for simple background work without Celery; production backends come from third-party packages |

## Running the tests

The tests run tasks in-process and use an in-memory cache, so no broker is required:

```bash
python manage.py test
```

## License

This project is licensed under the terms specified in the [LICENSE](../LICENSE) file.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryq.dev/)
- [Valkey](https://valkey.io/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Tailwind CSS](https://tailwindcss.com/)
