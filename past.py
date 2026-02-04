from quizzer.quizzer import Prompt, Q

from util import get_time_key, get_times


def past_singular_ask(seed) -> Prompt:
    prompt = "hace un " + get_times("s", "es")[seed]

    return {"type": "text", "value": prompt}


def past_singular_check(seed, ans: str):
    return f"duela {get_times('s', 'eu')[seed]} bat" == ans


def past_plural_ask(seed) -> Prompt:
    prompt = "hace un " + get_times("p", "es")[seed]

    return {"type": "text", "value": prompt}


def past_plural_check(seed, ans: str):
    return f"duela bi {get_times('p', 'eu')[seed]}" == ans


PastSingularQ = Q[str](
    get_seed=get_time_key,
    ask=past_singular_ask,
    check=past_singular_check,
    explain=lambda _: {"type": "text", "value": ""},
)

PastPluralQ = Q[str](
    get_seed=get_time_key,
    ask=past_plural_ask,
    check=past_plural_check,
    explain=lambda _: {"type": "text", "value": ""},
)
