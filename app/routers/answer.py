from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from sqlalchemy import insert, select, update, delete, func

from app.backend.db_depends import get_db
from app.schemas import CreateAnswer, AnswerResponse
from app.models import *


router = APIRouter(tags=['answer'])

@router.post('/questions/{question_id}/answers/', response_model=AnswerResponse, status_code=status.HTTP_201_CREATED)
async def create_answer(question_id: int, give_answer: CreateAnswer, db: Annotated[AsyncSession, Depends(get_db)]):
    question = await db.scalar(select(Question).where(Question.id == question_id))
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Question is not found'
        )

    max_answers_per_user = 2

    answer_count = await db.scalar(
        select(func.count(Answer.id)).where(
            Answer.question_id == question_id,
            Answer.user_id == give_answer.user_id
        )
    )

    if answer_count >= max_answers_per_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Limit questions for user"
        )

    answer = Answer(
        text=give_answer.text,
        user_id=give_answer.user_id,
        question_id=question_id
    )

    db.add(answer)
    await db.commit()
    await db.refresh(answer)

    return answer

@router.get('/answers/{answer_id}', response_model=AnswerResponse)
async def get_answer(answer_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    answer = await db.scalar(select(Answer).where(Answer.id == answer_id))
    if not answer:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Answer is not found'
        )
    return answer

@router.delete('/answers/{answer_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer(answer_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    answer = await db.scalar(select(Answer).where(Answer.id == answer_id))
    if not answer:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Answer is not found'
        )
    await db.delete(answer)
    await db.commit()