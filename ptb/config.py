from environs import Env


class Settings:
    env = Env()
    env.read_env()

    token = env("TOKEN")

    _db_login = env("POSTGRES_LOGIN")
    _db_password = env("POSTGRES_PASSWORD")
    _db_port = env("POSTGRES_PORT")
    _db_host = env("POSTGRES_HOST")
    _db_name = env("POSTGRES_NAME")

    db_url = f"postgresql+asyncpg://{_db_login}:{_db_password}@{_db_host}:{_db_port}/{_db_name}"
    