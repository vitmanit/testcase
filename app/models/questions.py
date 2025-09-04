from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from sqlalchemy.orm import relationship

from app.backend.db import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now())

    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")