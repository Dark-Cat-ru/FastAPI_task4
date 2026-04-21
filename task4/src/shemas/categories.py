from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status

class Category(BaseModel):
    title: str = Field(max_length=256, min_length=3)
    description: str = Field(min_length=5)
    slug: int = Field(min_length=1)

    @field_validator("title", mode="after")
    @staticmethod
    def check_title(title: str):
        if title[:1] != str.upper(title[:1]):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Заголовок категории должен начинаться с большой буквы"
            )