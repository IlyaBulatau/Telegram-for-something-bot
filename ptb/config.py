from environs import Env


class Settings:
    env = Env()
    env.read_env()

    token = env("TOKEN")
