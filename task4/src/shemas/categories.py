from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status

class Category(BaseModel):
    title: str = Field(max_length=256)
    description: str
    slug: int

    @field_validator("title", mode="after")
    @staticmethod
    def check_title(title: str):
        if title[:1] != title[:1].upper():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Заголовок категории должен начинаться с большой буквы"
            )
        return title