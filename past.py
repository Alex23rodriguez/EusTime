from ezquiz import Q

from util import get_time_key, get_times


def past_singular_ask(seed):
    prompt = "hace un " + get_times("s", "es")[seed]

    return prompt


def past_singular_correct(seed):
    return f"duela {get_times('s', 'eu')[seed]} bat"


def past_plural_ask(seed):
    prompt = "hace dos " + get_times("p", "es")[seed]

    return prompt


def past_plural_correct(seed):
    return f"duela bi {get_times('p', 'eu')[seed]}"


PastSingularQ = Q[str](
    get_seed=get_time_key,
    ask=past_singular_ask,
    correct=past_singular_correct,
)

PastPluralQ = Q[str](
    get_seed=get_time_key,
    ask=past_plural_ask,
    correct=past_plural_correct,
)
