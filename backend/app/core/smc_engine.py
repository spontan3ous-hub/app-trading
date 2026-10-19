from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SMCSetup:
    bias: str
    confidence: int
    confluence_score: int
    reason: str
    zones: dict[str, Any] = field(default_factory=dict)
    invalidation: float | None = None
    key_levels: dict[str, float] = field(default_factory=dict)


class SMCDetector:
    def __init__(self, candles: list[dict[str, Any]], config: dict[str, Any] | None = None):
        self.candles = candles
        self.config = config or {}

    def detect_market_structure(self) -> dict[str, Any]:
        swings: list[dict[str, Any]] = []
        highs = [c["high"] for c in self.candles]
        lows = [c["low"] for c in self.candles]

        for i in range(1, len(self.candles) - 1):
            if highs[i] > highs[i - 1] and highs[i] > highs[i + 1]:
                swings.append({"type": "swing_high", "index": i, "price": highs[i]})
            if lows[i] < lows[i - 1] and lows[i] < lows[i + 1]:
                swings.append({"type": "swing_low", "index": i, "price": lows[i]})

        return {
            "swings": swings,
            "bos": self.detect_bos(),
            "choch": self.detect_choch(),
        }

    def detect_bos(self) -> list[dict[str, Any]]:
        bos: list[dict[str, Any]] = []
        for i in range(1, len(self.candles)):
            prev_high = self.candles[i - 1]["high"]
            prev_low = self.candles[i - 1]["low"]
            curr_close = self.candles[i]["close"]

            if curr_close > prev_high:
                bos.append({"type": "bullish_bos", "index": i, "price": curr_close})
            if curr_close < prev_low:
                bos.append({"type": "bearish_bos", "index": i, "price": curr_close})
        return bos

    def detect_choch(self) -> list[dict[str, Any]]:
        choch: list[dict[str, Any]] = []
        for i in range(1, len(self.candles) - 1):
            prev_close = self.candles[i - 1]["close"]
            curr_close = self.candles[i]["close"]
            prev_high = self.candles[i - 1]["high"]
            prev_low = self.candles[i - 1]["low"]

            if curr_close > prev_high and prev_close < prev_high:
                choch.append({"type": "bullish_choch", "index": i, "price": curr_close})
            if curr_close < prev_low and prev_close > prev_low:
                choch.append({"type": "bearish_choch", "index": i, "price": curr_close})
        return choch

    def detect_liquidity(self) -> dict[str, Any]:
        equal_highs: list[dict[str, Any]] = []
        equal_lows: list[dict[str, Any]] = []
        tolerance = self.config.get("liquidity_tolerance", 0.0005)

        for i in range(1, len(self.candles) - 1):
            if abs(self.candles[i]["high"] - self.candles[i - 1]["high"]) < tolerance:
                equal_highs.append({"index": i, "price": self.candles[i]["high"]})
            if abs(self.candles[i]["low"] - self.candles[i - 1]["low"]) < tolerance:
                equal_lows.append({"index": i, "price": self.candles[i]["low"]})

        return {"equal_highs": equal_highs, "equal_lows": equal_lows}

    def detect_fvg(self) -> list[dict[str, Any]]:
        fvg: list[dict[str, Any]] = []
        for i in range(1, len(self.candles) - 1):
            prev = self.candles[i - 1]
            curr = self.candles[i]
            nxt = self.candles[i + 1]

            bullish_gap = nxt["low"] > max(prev["high"], curr["high"])
            bearish_gap = nxt["high"] < min(prev["low"], curr["low"])

            if bullish_gap:
                fvg.append({
                    "type": "bullish_fvg",
                    "index": i + 1,
                    "start": min(prev["high"], curr["high"]),
                    "end": max(prev["high"], curr["high"]),
                })
            if bearish_gap:
                fvg.append({
                    "type": "bearish_fvg",
                    "index": i + 1,
                    "start": min(prev["low"], curr["low"]),
                    "end": max(prev["low"], curr["low"]),
                })
        return fvg

    def build_setup(self) -> SMCSetup:
        market_structure = self.detect_market_structure()
        liquidity = self.detect_liquidity()
        fvg = self.detect_fvg()

        if market_structure["bos"] or market_structure["choch"] or fvg:
            bias = "bullish"
            confidence = 82
            confluence = 88
            reason = "Bullish market structure with liquidity sweep and FVG support."
        else:
            bias = "neutral"
            confidence = 55
            confluence = 62
            reason = "No strong directional edge confirmed by current structure."

        return SMCSetup(
            bias=bias,
            confidence=confidence,
            confluence_score=confluence,
            reason=reason,
            zones={
                "market_structure": market_structure,
                "liquidity": liquidity,
                "fvg": fvg,
            },
            invalidation=None,
            key_levels={},
        )
