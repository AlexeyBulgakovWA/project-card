from typing import List
from typing import Union

from sqlalchemy.orm import Session

from app import Card
from app.schemas.schemas import CardBase, CardDetailsModel


def get_cards(session: Session, skip: int = 0, limit: int = 100) -> List[Card]:
    return session.query(Card).offset(skip).limit(limit).all()


def create_card(session: Session, card: CardBase):
    db_card = Card(name=card.name, projectManager=card.projectManager, stack=card.stack, productOwner=card.productOwner)
    session.add(db_card)
    session.commit()
    return CardDetailsModel.from_orm(db_card)


def get_project_by_name(session: Session, name: str):
    return session.query(Card).filter(Card.name == name).first()


def delete_card(session: Session, card_id: int):
    session.query(Card).filter(Card.id == card_id).delete()
    session.commit()
    return None


def get_card(session: Session, id: int):
    return session.query(Card).get(id)


def update_card(session: Session, card: Union[int, Card], data: CardBase):
    if isinstance(card, int):
        card = get_card(session, card)
    if card is None:
        return None
    for key, value in data:
        setattr(card, key, value)
    session.commit()
    return card
