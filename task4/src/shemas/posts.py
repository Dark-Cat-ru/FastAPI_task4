from pydantic import BaseModel, Field, field_validator, ConfigDict
from fastapi import HTTPException, status
from datetime import datetime

class Post(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(max_length=256)
    text: str = Field(max_length=80)
    id: int
    pub_date: datetime
    author_login: str
    location_name: str
    category_title: str

    @field_validator("title", mode="after")
    @staticmethod
    def check_title(title: str):
        if title[:1] != title[:1].upper():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Заголовок поста должен начинаться с большой буквы"
            )
        return title