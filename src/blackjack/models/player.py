from typing import Optional, List

from pydantic import (
    BaseModel,
    Field
)
from blackjack.models.card import Card

class Player():
    player_id: int = Field()
    username: str = Field()
    current_game_id: Optional[int] = Field(default=None)
    hand: List[Card] = Field(default=[])
    balance: float = Field(default=0)
    bet: float = Field(default=0)