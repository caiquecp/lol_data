from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    api_url_champions: str
    champions_key_selection: List[str]
    champions_data_path: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
