from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)
get_db = database.get_db


@router.post('', response_model=schemas.showUser, status_code=status.HTTP_201_CREATED, tags=['Users'])
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.showUser, status_code=status.HTTP_200_OK, tags=['Users'])
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
