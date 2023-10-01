from copy import copy


def get_szkola(sprawozdanie, szkola):
    if "Jednostki" in sprawozdanie:
        for sz in sprawozdanie["Jednostki"]["Jednostka"]:
            if sz["Regon"] == szkola:
                return sz
    else:
        for sz in sprawozdanie["PaczkaSprawozdan"]["Jednostki"]["Jednostka"]:
            if sz["Regon"] == szkola:
                return sz


def get_wydatki(sprawozdanie, szkola, dzial=None, rozdzial=None, grupa=None, paragraf=None):
    szkola = get_szkola(sprawozdanie, szkola)["Sprawozdania"]["Rb-28s"]
    pozycje = copy(szkola["Pozycje"]["Pozycja"])

    # przygotowanie kodu pod filtrowanie per rozdzial czy paragraf

    # for klucz, filtr in zip(("Dzial", "Rozdzial", "Grupa", "Paragraf"), (dzial, rozdzial, grupa, paragraf)):
    #     for pozycja in szkola["Pozycje"]["Pozycja"]:
    #         if filtr and filtr != pozycja[klucz]:
    #             try:
    #                 pozycje.remove(pozycja)
    #             except ValueError:
    #                 pass
    #         else:
    for pozycja in pozycje:
        if "WW" not in pozycja:
            pozycja["WW"] = "0"
    wydatki = round(sum([float(wydatek["WW"]) for wydatek in pozycje]), 2)
    return wydatki, pozycje


def get_dochody(sprawozdanie, szkola, dzial=None, rozdzial=None, paragraf=None):
    szkola = get_szkola(sprawozdanie, szkola)["Sprawozdania"]["Rb-27s"]
    pozycje = copy(szkola["Pozycje"]["Pozycja"])

    # przygotowanie kodu pod filtrowanie per rozdzial czy paragraf

    # for klucz, filtr in zip(("Dzial", "Rozdzial", "Paragraf"), (dzial, rozdzial, paragraf)):
    #     for pozycja in szkola["Pozycje"]["Pozycja"]:
    #         if filtr and filtr != pozycja[klucz]:
    #             try:
    #                 pozycje.remove(pozycja)
    #             except ValueError:
    #                 pass
    #         else:
    for pozycja in pozycje:
        if "DW" not in pozycja:
             pozycja["DW"] = "0"
    dochody = round(sum([float(dochod["DW"]) for dochod in pozycje]), 2)
    return dochody, pozycje
