from random import choice

from ezquiz import Q


def get_random_day():
    return choice(
        ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    )


def days_ask(day: str):
    return day


def days_correct(day):
    return {
        "lunes": "astelehen",
        "martes": "astearte",
        "miercoles": "asteazken",
        "jueves": "ostegun",
        "viernes": "ostiral",
        "sabado": "larunbat",
        "domingo": "igande",
    }[day]


DaysQ = Q[str](
    get_seed=get_random_day,
    ask=days_ask,
    correct=days_correct,
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


def months_ask(month: str):
    return month


def months_correct(month):
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
    }[month]


MonthsQ = Q[str](
    get_seed=get_random_month,
    ask=months_ask,
    correct=months_correct,
)


def get_random_season():
    return choice(["primavera", "verano", "otoño", "invierno"])


def seasons_ask(season: str):
    return season


def seasons_correct(season):
    return {
        "primavera": "udaberri",
        "verano": "uda",
        "otoño": "udazken",
        "invierno": "negu",
    }[season]


SeasonsQ = Q[str](
    get_seed=get_random_season,
    ask=seasons_ask,
    correct=seasons_correct,
)
