from quizzer.quizzer import Prompt, Q

from util import get_time_key, get_times


def future_singular_ask(seed) -> Prompt:
    prompt = "en un " + get_times("s", "es")[seed]

    return {"type": "text", "value": prompt}


def future_singular_check(seed, ans: str):
    return f"{get_times('s', 'eu')[seed]} batean" == ans


def future_plural_ask(seed) -> Prompt:
    prompt = "en dos " + get_times("p", "es")[seed]

    return {"type": "text", "value": prompt}


def future_plural_check(seed, ans: str):
    return f"bi {get_times('p', 'eu')[seed]}etan" == ans


FutureSingularQ = Q[str](
    get_seed=get_time_key,
    ask=future_singular_ask,
    check=future_singular_check,
    explain=lambda _: {"type": "text", "value": ""},
)

FuturePluralQ = Q[str](
    get_seed=get_time_key,
    ask=future_plural_ask,
    check=future_plural_check,
    explain=lambda _: {"type": "text", "value": ""},
)
