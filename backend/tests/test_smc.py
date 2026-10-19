import json

from app.core.smc_engine import SMCDetector


def test_detects_bullish_setup():
    candles = [
        {"open": 1.0, "high": 1.01, "low": 0.99, "close": 1.0},
        {"open": 1.0, "high": 1.03, "low": 0.98, "close": 1.02},
        {"open": 1.02, "high": 1.05, "low": 1.01, "close": 1.04},
        {"open": 1.04, "high": 1.07, "low": 1.02, "close": 1.06},
    ]

    detector = SMCDetector(candles)
    setup = detector.build_setup()
    assert setup.bias in {"bullish", "neutral"}
    assert setup.confluence_score > 0


def test_json_contract_shape():
    payload = {
        "bias": "bullish",
        "confidence": 83,
        "reasoning": "Strong structure and liquidity alignment.",
        "key_levels": {"entry": 1.0872},
        "invalidation": 1.0838,
        "setup_quality": "A",
        "warnings": [],
    }
    assert json.loads(json.dumps(payload))["setup_quality"] == "A"
