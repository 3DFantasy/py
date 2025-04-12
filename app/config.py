from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NODE_ENV: str
    APP_SECRET: str
    REDIS_USERNAME: str
    REDIS_QUEUE: str
    REDIS_HOST: str
    REDIS_PASSWORD: str
    REDIS_PORT: str
    DATABASE_URL: str
    TEAM_1_URL: str
    TEAM_2_URL: str
    TEAM_3_URL: str
    TEAM_4_URL: str
    TEAM_5_URL: str
    TEAM_6_URL: str
    TEAM_7_URL: str
    TEAM_8_URL: str
    TEAM_9_URL: str
    PXP_API_URL: str
    FLY_WORKER_TOKEN: str
    RQ_WORKER_NUMBER: str
    RQ_QUEUE_NUMBER: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
