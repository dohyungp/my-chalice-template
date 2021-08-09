from pydantic import BaseSettings


class Settings(BaseSettings):
    """HolyCafe Configurations"""

    APP_NAME: str = "holycafe"
    STAGE: str = "dev"
    MEDITHERAPHY_CAFE24_WEBHOOK_KEY: str = "this-is-not-real-key"
    MEDITHERAPHY_MP_TOKEN: str = "this-is-not-real-key"

    class Config:
        """Pydantic Config"""

        case_sensitive = False


settings = Settings()
