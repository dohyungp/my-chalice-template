from pydantic import BaseSettings


class Settings(BaseSettings):
    """Template Configurations"""

    APP_NAME: str = "template"
    STAGE: str = "dev"

    class Config:
        """Pydantic Config"""

        case_sensitive = False


settings = Settings()
