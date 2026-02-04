from random import choice

from quizzer.quizzer import Prompt, Q


def get_random_day():
    return choice(
        ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    )


def days_ask(day: str) -> Prompt:
    return {"type": "text", "value": day}


def days_check(day, ans: str):
    return {
        "lunes": "astelehen",
        "martes": "astearte",
        "miercoles": "asteazken",
        "jueves": "ostegun",
        "viernes": "ostiral",
        "sabado": "larunbat",
        "domingo": "igande",
    }[day] == ans


DaysQ = Q[str](
    get_seed=get_random_day,
    ask=days_ask,
    check=days_check,
    explain=lambda _: {"type": "text", "value": ""},
)


def get_random_month():
    return choice(
        [
            "enero",
            "febrero",
            "marzo",
            "abril",
            "mayo",
            "junio",
            "julio",
            "agosto",
            "septiembre",
            "octubre",
            "noviembre",
            "diciembre",
        ]
    )


def months_ask(month: str) -> Prompt:
    return {"type": "text", "value": month}


def months_check(month, ans: str):
    return {
        "enero": "urtarril",
        "febrero": "ostail",
        "marzo": "martxo",
        "abril": "apiril",
        "mayo": "maiatz",
        "junio": "ekain",
        "julio": "uztail",
        "agosto": "abuztu",
        "septiembre": "irail",
        "octubre": "urri",
        "noviembre": "azaro",
        "diciembre": "abendu",
    }[month] == ans


MonthsQ = Q[str](
    get_seed=get_random_month,
    ask=months_ask,
    check=months_check,
    explain=lambda _: {"type": "text", "value": ""},
)


def get_random_season():
    return choice(["primavera", "verano", "otoño", "invierno"])


def seasons_ask(season: str) -> Prompt:
    return {"type": "text", "value": season}


def seasons_check(season, ans: str):
    return {
        "primavera": "udaberri",
        "verano": "uda",
        "otoño": "udazken",
        "invierno": "negu",
    }[season] == ans


SeasonsQ = Q[str](
    get_seed=get_random_season,
    ask=seasons_ask,
    check=seasons_check,
    explain=lambda _: {"type": "text", "value": ""},
)
