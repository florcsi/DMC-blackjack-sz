from typing import Dict

from fastapi import (
    APIRouter,
    Path,
    Query

)

from blackjack.models import Deck
from blackjack.models import Player

router = APIRouter(
    tags=[__name__.split('.')[-1]]
)

players: Dict[int, Player] = {}


@router.post(
    path='/player',
    response_model=int
)

def register(
        username: str = Query()
):
    next_id = max(players.keys()) + 1 if players else 1
    players[next_id] = Player(
        player_id=next_id,
        username=username
    )
    return next_id

@router.get(
    path='/player/{player_id}',
    response_model=Player
)

def get_player(
        player_id: int = Path()
):
    return players[player_id]