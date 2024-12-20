import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Config:
  __instance = None
  def __new__(cls):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
      cls.__instance.init_env()
    return cls.__instance
    
  def init_env(self):
    self.HOST = os.getenv("HOST")
    self.PORT = os.getenv("PORT", cast=int)
    self.JWT_TOKEN = os.getenv("JWT_SECRET_KEY")
    self.ALGORITHM = os.getenv("ALGORITHM")
    self.TOKEN_EXPIRY = os.getenv("ACCESS_TOKEN_EXPIRED_MINUTES")

  def get_env(self, key: str, cast: Optional[type] = None):
    value = os.environ.get(key)
    if not value:
      raise ValueError(f"env does not have specified key: {key}")
    if cast is not None:
      return cast(value)
    return value