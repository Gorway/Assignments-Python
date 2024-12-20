import os
from typing import Optional
from datetime import datetime, timedelta

import pytz
from jose import JWTError, jwt
from settings.config import Config
from passlib.context import CryptContext

config = Config()

pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    data: dict, expires_minutes: int = config.TOKEN_EXPIRY
) -> str:
    to_encode = data.copy()
    expire = datetime.now(pytz.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.JWT_TOKEN, algorithm=config.ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        if payload["exp"] >= datetime.now(pytz.utc).timestamp():
            return payload
    except JWTError:
        return None
