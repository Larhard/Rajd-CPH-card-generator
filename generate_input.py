#!/usr/bin/env python3

import pandas as pd
import re
import sys
from contacts import contacts

GENERATE_COMMANDANT=True

def escaped(text):
    result = str(text)
    result = re.sub(r"{", r"\{", result)
    result = re.sub(r"}", r"\}", result)
    result = re.sub(r"^Kompot – kompozycja własna$", r"Kompot – kompozycja~własna", result)
    result = re.sub(r"^Browarem przez życie \(vel Misie-Wy-Pysie\)$", r"Browarem~przez~życie (vel~Misie-Wy-Pysie)", result)
    result = re.sub(r"^Sekret Zielarza \(vel Ślimaczki 2.0\)$", r"Sekret~Zielarza (vel~Ślimaczki~2.0)", result)
    return result

def elongated(text):
    result = str(text)
    result = re.sub(r"^Sekret Zielarza$", r"Sekret Zielarza (vel Ślimaczki 2.0)", result)
    return result

def shortened(text):
    result = str(text)
    result = re.sub(r"\s*– kompozycja własna$", r"", result)
    result = re.sub(r"\s*\(vel.*\)$", r"", result)
    return result

def show_entry(name, *args):
    print("\\{}".format(name), end="")

    for arg in args:
        print("{{{}}}".format(escaped(elongated(arg))), end="")

    print()

def main(source):
    data = pd.read_excel(source)

    for person in data.iterrows():
        person = person[1]
        name            = person["imię"]
        surname         = person["nazwisko"]
        route_number    = person["numer trasy"]
        route_name      = person["nazwa trasy"]

        route_master    = contacts[route_number]

        routes_master   = contacts["routes_master"]
        metha           = contacts["metha"]
        commandant      = contacts["commandant"]

        gopr            = contacts["gopr"]

        show_entry("entry", name, surname, route_number, route_name, *route_master, *routes_master, *metha, *commandant, *gopr)

        if GENERATE_COMMANDANT and "{} {}".format(name, surname) == contacts["commandant"][0]:
            bus = route_master[0]

            routes_lines = []
            routes = sorted(set(zip(data["numer trasy"], data["nazwa trasy"])))
            for number, name in routes:
                _, master, phone = contacts[number]
                routes_lines.append("{}. {}&{}&{}\\\\".format(number, escaped(shortened(name)), master, phone))

            routes_master   = contacts["routes_master"]
            metha           = contacts["metha"]
            gopr            = contacts["gopr"]

            show_entry("commandant", contacts["commandant"][0], route_name, bus, *gopr, "".join(routes_lines), *metha, *routes_master)

if __name__ == "__main__":
    main(sys.argv[1])
