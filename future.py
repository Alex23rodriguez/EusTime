from quizzer import Q

from util import get_time_key, get_times


def future_singular_ask(seed):
    prompt = "en un " + get_times("s", "es")[seed]

    return prompt


def future_singular_correct(seed):
    return f"{get_times('s', 'eu')[seed]} batean"


def future_plural_ask(seed):
    prompt = "en dos " + get_times("p", "es")[seed]

    return prompt


def future_plural_correct(seed):
    return f"bi {get_times('p', 'eu')[seed]}etan"


FutureSingularQ = Q[str](
    get_seed=get_time_key,
    ask=future_singular_ask,
    correct=future_singular_correct,
)

FuturePluralQ = Q[str](
    get_seed=get_time_key,
    ask=future_plural_ask,
    correct=future_plural_correct,
)
