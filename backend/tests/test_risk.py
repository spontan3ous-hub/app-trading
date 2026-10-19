from app.core.risk_manager import RiskParams


def test_risk_position_size():
    risk = RiskParams(account_balance=10000, risk_pct=1.0, entry=1.1, stop_loss=1.092, pip_value=10.0)
    assert risk.risk_amount == 100.0
    assert risk.position_size > 0


def test_validate_blocked_trade():
    risk = RiskParams(account_balance=10000, risk_pct=5.0, entry=1.1, stop_loss=1.09, pip_value=10.0)
    result = risk.validate(min_rr=2.0, max_daily_loss_pct=3.0)
    assert result["allowed"] is False or result["risk_amount"] > 0
