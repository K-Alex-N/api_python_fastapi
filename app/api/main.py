import random

from fastapi import FastAPI, Request, Response, status
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge
import string

from .database import async_db
from .transactions import routes as transactions_routes
from .categories import routes as categories_routes
from .database import lifespan
from .logger_config import setup_logger

logger = setup_logger()
app = FastAPI(lifespan=lifespan)

app.include_router(transactions_routes.router)
app.include_router(categories_routes.router)

# --- Healthcheck ---

@app.get("/health")
async def healthcheck():
    await async_db.command("ping")
    return {"status": "ok"}

# ---------------for elastic------------------------------------------

@app.middleware("http")
async def log_requests(request: Request, call_next):
    ip = request.client.host
    endpoint = request.url.path
    method = request.method

    response: Response = await call_next(request)
    status_code = response.status_code

    logger.info(
        f"{method} {endpoint} - {status_code}",
        extra={
            "extra": {
                "ip": ip,
                "endpoint": endpoint,
                "method": method,
                "status": status_code,
            }
        }
    )

    return response


@app.get("/generate-random-logs")
def generate_random_logs():
    levels = ["info", "debug", "warning", "error", "supper_error"]
    actions = ["login", "logout", "purchase", "view", "click"]
    countries = ["US", "DE", "FR", "IN", "RU", "CN", "BR"]
    devices = ["mobile", "desktop", "tablet", "smart_tv"]

    for _ in range(10):
        level = random.choice(levels)
        log_data = {
            "user_id": random.randint(1000, 9999),
            "action": random.choice(actions),
            "duration": round(random.uniform(0.1, 5.0), 2),
            "success": random.choice([True, False]),
            "country": random.choice(countries),
            "device": random.choice(devices),
            "session_id": ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        }

        msg = f"User {log_data['user_id']} performed {log_data['action']}"

        # Логируем на нужном уровне
        getattr(logger, level)(
            msg,
            extra={"extra": log_data}
        )

    return {"message": "Random logs generated"}


# ---------------for prometheus------------------------------------------

Instrumentator().instrument(app).expose(app)

ERROR_COUNTER = Counter("fastapi_errors_total", "Total number of simulated errors")
ACTIVE_USERS = Gauge("fastapi_active_users", "Number of active users")


@app.get("/")
def read_root():
    ACTIVE_USERS.set(random.randint(5, 50))  # Пример бизнес-метрики
    return {"message": "Hello from FastAPI"}


@app.get("/error")
def generate_error():
    ERROR_COUNTER.inc()
    raise ValueError("Simulated error")


# ---------------------------------------------------------
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    print(f"An internal server error occurred: {exc}")

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal Server Error"}
    )

# ---------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
