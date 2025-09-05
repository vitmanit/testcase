from pydantic import BaseModel, field_serializer
from datetime import datetime

class CreateAnswer(BaseModel):
    user_id: str
    text: str
    question_id: int

class CreateQuestion(BaseModel):
    text: str


class AnswerResponse(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime) -> str:
        return value.strftime("%Y-%m-%d %H:%M:%S")  # Формат: "2025-09-05 08:35:03"

    class Config:
        from_attributes = True

class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: list[AnswerResponse] = []

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime) -> str:
        return value.strftime("%Y-%m-%d %H:%M:%S")  # Формат: "2025-09-05 08:35:03"

    class Config:
        from_attributes = True