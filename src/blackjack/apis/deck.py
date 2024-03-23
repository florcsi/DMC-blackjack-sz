import random
from typing import Dict

from fastapi import (
    APIRouter,
    Path,
    Query

)

from blackjack.models import Deck

router = APIRouter(
    tags=[__name__.split('.')[-1]]
)

decks: Dict[int, Deck] = {}

@router.post(
    path='/deck',
    response_model=int
)
def create_deck():
    next_id = max(decks.keys()) + 1 if decks else 1
    decks[next_id] = Deck(deck_id=next_id)

@router.get(
    path='/deck/{deck_id}',
    response_model=Deck
)

def get_deck(
        deck_id: int = Path()
):
    return decks[deck_id]

@router.get(
    path='/deck/{deck_id}/shuffle',
    response_model=Deck
)

def shuffle_deck(
        deck_id: int = Path()
):
    d = decks[deck_id]
    random.shuffle(d.cards)
    return d




