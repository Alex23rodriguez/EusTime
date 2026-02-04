from random import choice
from typing import Literal


def get_times(count: Literal["s", "p"], lang="es"):
    if lang == "es":
        if count == "s":
            return {
                "s": "segundo",
                "m": "minuto",
                "h": "hora",
                "d": "dia",
                "w": "semana",
                "M": "mes",
                "Y": "año",
            }

        else:
            return {
                "s": "segundos",
                "m": "minutos",
                "h": "horas",
                "d": "dias",
                "w": "semanas",
                "M": "meses",
                "Y": "años",
            }

    elif lang == "eu":
        if count == "s":
            return {
                "s": "segundu",
                "m": "minutu",
                "h": "ordu",
                "d": "egun",
                "w": "aste",
                "M": "hilabete",
                "Y": "urtu",
            }

        else:
            return {
                "s": "segundu",
                "m": "minutu",
                "h": "ordu",
                "d": "egun",
                "w": "aste",
                "M": "hilabete",
                "Y": "urtu",
            }
    raise NotImplementedError()


def get_count_and_td():
    count = ["s", "p"]
    time = ["s", "m", "h", "d", "w", "M", "Y"]

    return choice(count), choice(time)


def get_count():
    return choice(["s", "p"])


def get_time_key():
    return choice(["s", "m", "h", "d", "w", "M", "Y"])
