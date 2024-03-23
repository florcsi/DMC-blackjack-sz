from typing import Optional, List

from pydantic import (
    BaseModel,
    Field
)

from blackjack.models.deck import Deck
from blackjack.models.player import Player

class Game(BaseModel):
    game_id: int = Field()
    deck: Deck
    players: List[Player] = Field(default=[])
    current_player_id: Optional[int] = Field(default=None)