from pydantic import BaseModel, SecretStr, Field, ConfigDict, field_validator
from fastapi import HTTPException, status

class BaseUser(BaseModel):
    login: str

class CreateUser(BaseUser):
    password: str

class User(BaseUser):
    model_config = ConfigDict(from_attributes=True)
    password: SecretStr = Field(min_length=8)


    @field_validator("login", mode="after")
    @staticmethod
    def check_login(login: str) -> str:
        if 'bot' in str.lower(login):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Логин пользователя не должен содержать слова bot"
            )