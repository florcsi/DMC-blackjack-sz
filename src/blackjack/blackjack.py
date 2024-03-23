from fastapi import (
    FastAPI
)
import uvicorn

from blackjack.apis.deck import router as deck_router
from blackjack.apis.player import router as player_router

app = FastAPI(
    title=__name__,
    version='0.1.0'
)

app.include_router(deck_router)
app.include_router(player_router)

def main():
    uvicorn.run(
        'blackjack.blackjack:app',
        reload=True,
        port=3000
    )


if __name__ == '__main__':
    main()
