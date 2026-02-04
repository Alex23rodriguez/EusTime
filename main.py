from quizzer import APIGame

from future import FuturePluralQ, FutureSingularQ
from past import PastPluralQ, PastSingularQ
from vocab import DaysQ, MonthsQ, SeasonsQ

game = APIGame(
    "Euskera - Time",
    {
        "future_s": FutureSingularQ,
        "future_p": FuturePluralQ,
        "past_s": PastSingularQ,
        "past_p": PastPluralQ,
        "days": DaysQ,
        "months": MonthsQ,
        "seasons": SeasonsQ,
    },
)

game.start()
