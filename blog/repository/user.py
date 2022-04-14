from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    data = request.dict()
    data['password'] = Hash.bcrypt(request.password)
    new_user = models.User(**data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'No found user {id}'
        )

    return user
