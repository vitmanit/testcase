from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone

from sqlalchemy.orm import relationship

from app.backend.db import Base

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(String, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now())

    question = relationship("Question", back_populates="answers")