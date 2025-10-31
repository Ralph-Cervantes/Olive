"""
The main endpoint for returning dog data

ASSUMPTIONS:
1) The amount of data is reasonable and does not need advanced pagination like cursor based pagination.

"""


from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from data.db import get_db
from data.models.dogs import Dog
from data.schemas.dogs import DogResponse, TotalDogs

router = APIRouter()


@router.get("/api/dogs", response_model=List[DogResponse])
def get_dogs(
    db: Session = Depends(get_db),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=15, gt=0, le=16)
):
    """Gets a list of dogs with pagination"""
    return db.query(Dog).order_by(Dog.breed).offset(offset).limit(limit).all()


@router.get("/api/dogs/count", response_model=TotalDogs)
def get_dogs_count(db: Session = Depends(get_db)):
    """Gets the total number of dogs"""
    return TotalDogs(total=db.query(Dog).count())
