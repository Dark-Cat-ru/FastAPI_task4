from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status
from datetime import datetime
from shemas.users import User
from shemas.locations import Location
from shemas.categories import Category

class Post(BaseModel):
    title: str = Field(max_length=256, min_length=3)
    text: str = Field(min_length=5, max_length=80)
    id: int = Field(min_length=1)
    pub_date: datetime
    author: User
    location: Location
    category: Category

    @field_validator("title", mode="after")
    @staticmethod
    def check_title(title: str):
        if title[:1] != str.upper(title[:1]):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Заголовок поста должен начинаться с большой буквы"
            )