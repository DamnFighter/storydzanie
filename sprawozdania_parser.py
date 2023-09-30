from copy import copy


def get_szkola(sprawozdanie, szkola, is_dochody=False):
    if is_dochody:
        for sz in sprawozdanie["PaczkaSprawozdan"]["Jednostki"]["Jednostka"]:
            if sz["Regon"] == szkola:
                return sz
    else:
        for sz in sprawozdanie["PaczkaSprawozdan"]["Jednostki"]["Jednostka"]:
            if sz["Regon"] == szkola:
                return sz


def get_wydatki(sprawozdanie, szkola, dzial=None, rozdzial=None, grupa=None, paragraf=None):
    szkola = get_szkola(sprawozdanie, szkola)["Sprawozdania"]["Rb-28s"]
    pozycje = copy(szkola["Pozycje"]["Pozycja"])
    for klucz, filtr in zip(("Dzial", "Rozdzial", "Grupa", "Paragraf"), (dzial, rozdzial, grupa, paragraf)):
        for pozycja in szkola["Pozycje"]["Pozycja"]:
            if filtr and filtr != pozycja[klucz]:
                try:
                    pozycje.remove(pozycja)
                except ValueError:
                    pass
            else:
                if "WW" not in pozycja:
                    pozycja["WW"] = "0"
    wydatki = sum([float(wydatek["WW"]) for wydatek in pozycje])
    return wydatki, pozycje


def get_dochody(sprawozdanie, szkola, dzial=None, rozdzial=None, paragraf=None):
    szkola = get_szkola(sprawozdanie, szkola, is_dochody=True)["Sprawozdania"]["Rb-27s"]
    pozycje = copy(szkola["Pozycje"]["Pozycja"])

    for klucz, filtr in zip(("Dzial", "Rozdzial", "Paragraf"), (dzial, rozdzial, paragraf)):
        for pozycja in szkola["Pozycje"]["Pozycja"]:
            if filtr and filtr != pozycja[klucz]:
                try:
                    pozycje.remove(pozycja)
                except ValueError:
                    pass
            else:
                if "DW" not in pozycja:
                     pozycja["DW"] = "0"
    dochody = sum([float(dochod["DW"]) for dochod in pozycje])
    return dochody, pozycje
