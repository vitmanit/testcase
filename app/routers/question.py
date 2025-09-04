from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import joinedload, selectinload

from app.backend.db_depends import get_db
from app.schemas import CreateQuestion, QuestionResponse
from app.models import *
from typing import List
from datetime import datetime

router = APIRouter(prefix='/questions', tags=['question'])

@router.get('/', response_model=List[QuestionResponse])
async def all_questions(db: AsyncSession = Depends(get_db)):
    query = select(Question).options(joinedload(Question.answers)).order_by(Question.created_at.desc())
    result = await db.execute(query)
    questions = result.unique().scalars().all()
    return questions

@router.post('/', response_model=CreateQuestion)
async def create_question(question: CreateQuestion, db: AsyncSession = Depends(get_db)):
    query = insert(Question).values(text=question.text, created_at=datetime.utcnow()).returning(Question)
    result = await db.execute(query)
    new_question = result.scalars().first()
    await db.commit()
    return new_question

@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Question)
        .where(Question.id == question_id)
        .options(selectinload(Question.answers))
    )
    question = result.unique().scalar()  # ✅ .unique() + scalar()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.delete('/{id}',  status_code=204)
async def delete_question(db: Annotated[AsyncSession, Depends(get_db)], question_id: int):
    question = await db.scalar(select(Question).where(Question.id == question_id))
    if not question:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Question is not found'
        )

    await db.delete(question)
    await db.commit()