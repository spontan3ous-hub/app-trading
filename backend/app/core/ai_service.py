from __future__ import annotations

import json
import os
from typing import Any

import httpx


class ClaudeAIService:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("CLAUDE_API_KEY")
        self.base_url = "https://api.anthropic.com/v1/messages"

    async def analyze_chart(self, chart_image_b64: str, smc_json: dict[str, Any]) -> dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("CLAUDE_API_KEY is not set")

        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 512,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": chart_image_b64}},
                        {"type": "text", "text": "Analyze this chart with the supplied SMC/ICT JSON. Return strict JSON only: {'bias':'bullish|bearish|neutral','confidence':0-100,'reasoning':'...','key_levels':{},'invalidation':price,'setup_quality':'A+|A|B|C','warnings':[]}."},
                        {"type": "text", "text": json.dumps(smc_json)},
                    ],
                }
            ],
        }

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            text = data["content"][0]["text"]
            return json.loads(text)
