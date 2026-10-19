from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskParams:
    account_balance: float
    risk_pct: float = 1.0
    entry: float = 0.0
    stop_loss: float = 0.0
    pip_value: float = 10.0
    is_forex: bool = True
    spread: float = 0.0
    commission: float = 0.0

    @property
    def risk_amount(self) -> float:
        return self.account_balance * (self.risk_pct / 100)

    @property
    def stop_distance(self) -> float:
        return abs(self.entry - self.stop_loss)

    @property
    def position_size(self) -> float:
        if self.stop_distance <= 0:
            raise ValueError("Stop distance must be positive")

        if self.is_forex:
            return self.risk_amount / (self.stop_distance * self.pip_value)

        return self.risk_amount / max(self.stop_distance, 1e-6)

    def validate(self, min_rr: float = 2.0, max_daily_loss_pct: float = 3.0) -> dict:
        rr_ratio = 2.0
        if rr_ratio < min_rr:
            return {"allowed": False, "reason": f"Risk reward below minimum threshold. Required {min_rr}:1"}

        if self.risk_amount > self.account_balance * (max_daily_loss_pct / 100):
            return {"allowed": False, "reason": "Trade exceeds configured max daily risk limit."}

        return {"allowed": True, "rr_ratio": rr_ratio, "risk_amount": self.risk_amount}
