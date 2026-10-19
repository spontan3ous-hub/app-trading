# Trading Assistant

A production-ready starter monorepo for a Smart Money Concepts (SMC) / ICT trading assistant that:
- scans market structure and liquidity zones
- evaluates confluence and risk
- asks for explicit user approval before any trade is executed
- supports paper trading by default
- includes AI analysis via Claude Vision contract

## Safety notice
Trading carries substantial risk. This is not financial advice and no profits are guaranteed. The application is designed to require explicit user approval before any trade execution.

## Stack
- Backend: FastAPI + Python
- Frontend: React + TypeScript + Vite + Tailwind
- Database: PostgreSQL or SQLite for local development
- Charting: TradingView Lightweight Charts
- AI: Claude API with chart image + structured JSON

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Repository layout

```text
backend/          Python API and trading logic
frontend/         React dashboard and approval flow
README.md         Project overview
.env.example      Example environment variables
```

## Strategy logic
The app combines:
- market structure and BOS/CHoCH detection
- liquidity sweeps and equal high/low analysis
- order block and FVG detection
- premium/discount evaluation
- HTF bias and LTF entry logic
- confluence scoring from 0-100
- AI bias validation against the rule-based engine

Trade setups are only shown when they pass minimum confluence and risk limits. A trade is never executed without the user's confirmation.

## Confluence scoring
A setup scores higher when multiple conditions align:
- HTF bias
- CHoCH or BOS
- liquidity sweep or stop hunt
- order block or FVG entry zone
- killzone timing
- premium/discount alignment
- minimum risk-reward ratio

The default threshold is 70.

## License
This project is for learning and experimentation. Use responsibly.
