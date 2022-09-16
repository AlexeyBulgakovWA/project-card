from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import engine, SessionLocal, Base
from app.schemas.schemas import CardDetailsModel, CardBase
from app.utils import crud

Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("/card/", response_model=List[CardDetailsModel])
def get_cards(
        skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    card = crud.get_cards(session=session, skip=skip, limit=limit)
    return [i for i in card]


@router.post("/card/", response_model=CardDetailsModel)
def create_card(card: CardBase, session: Session = Depends(get_session)):
    db_card = crud.get_project_by_name(session, name=card.name)
    if db_card:
        raise HTTPException(status_code=400, detail="Employee already created")
    else:
        return crud.create_card(session=session, card=card)


@router.delete("/card/{card_id}", status_code=204)
def delete_card(employee_id: int, session: Session = Depends(get_session)):
    crud.delete_card(session, employee_id)
    return None


@router.put("/card/{card_id}", response_model=CardDetailsModel)
def update_card(card_id: int, data: CardBase, session: Session = Depends(get_session)):
    card = crud.update_card(session, card_id, data)
    if card is None:
        raise HTTPException(status_code=404)
    return card
