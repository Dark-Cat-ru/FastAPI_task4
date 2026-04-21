from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status

class Location(BaseModel):
    name: str = Field(max_length=20, min_length=3)

    @field_validator("name", mode="after")
    @staticmethod
    def check_name(name: str):
        if name[:1] != str.upper(name[:1]):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Название локации должно начинаться с большой буквы"
            )