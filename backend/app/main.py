from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(title="Trading Assistant", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "mode": settings.broker_mode}


@app.get("/api/setup")
async def get_setup() -> dict:
    return {
        "symbol": "EURUSD",
        "direction": "BUY",
        "entry": 1.0872,
        "stop_loss": 1.0838,
        "take_profit": 1.0938,
        "risk_pct": 1.0,
        "confluence_score": 88,
        "ai_bias": "bullish",
        "ai_confidence": 82,
        "requires_user_confirmation": True,
        "status": "pending_approval",
        "warning": "Trading carries substantial risk. This is not financial advice and no profits are guaranteed.",
    }


@app.get("/api/summary")
async def get_summary() -> dict:
    return {
        "balance": 25000.0,
        "equity": 25480.0,
        "daily_pl": 420.0,
        "risk_used_today": 0.8,
        "open_trades": 1,
    }
