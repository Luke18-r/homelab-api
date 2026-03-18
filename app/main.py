from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import socket

app = FastAPI(title="homelab-api")
requests_total = Counter("http_requests_total", "Total HTTP requests")

@app.get("/")
def root():
    requests_total.inc()
    return {"app": "homelab-api", "host": socket.gethostname()}

@app.get("/healthz")
def healthz():
    requests_total.inc()
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    requests_total.inc()
    return {"ready": True}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
