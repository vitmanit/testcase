from pydantic import BaseModel
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

    class Config:
        from_attributes = True

class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: list[AnswerResponse] = []

    class Config:
        from_attributes = True