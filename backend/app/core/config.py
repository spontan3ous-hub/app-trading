from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_env: str = "development"
    database_url: str = "sqlite:///./trading_assistant.db"
    claude_api_key: str = ""
    broker_mode: str = "paper"
    jwt_secret: str = "replace_with_secure_secret"
    enable_ai_analysis: bool = True
    notification_webhook_url: str = ""


settings = Settings()
