from fastapi import FastAPI

from app.main import app as api_app

app = FastAPI(title="Trading Assistant API")
app.mount("/api", api_app)
