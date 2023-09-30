from xml_parser import get_data
from copy import copy


sprawo = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Wydatki.xml')
sprawo2 = get_data(r'dane_kutno\Sprawozdania[2023][IIKwartał] Wydatki.xml')
sprawo3 = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Dochody.xml')
# sprawo4 = get_data(r'dane_kutno\SIO 30.09.2022.xml')


def get_szkola(sprawozdanie, szkola):
    for sz in sprawozdanie["Jednostki"]["Jednostka"]:
        if sz["Nazwa"] == szkola:
            return sz


def get_wydatki(sprawozdanie, szkola, dzial=None, rozdzial=None, grupa=None, paragraf=None):
    szkola = get_szkola(sprawozdanie, szkola)["Sprawozdania"]["Rb-28s"]
    pozycje = copy(szkola["Pozycje"]["Pozycja"])
    wydatki = 0
    for klucz, filtr in zip(("Dzial", "Rozdzial", "Grupa", "Paragraf"), (dzial, rozdzial, grupa, paragraf)):
        for pozycja in szkola["Pozycje"]["Pozycja"]:
            if filtr and filtr != pozycja[klucz]:
                try:
                    pozycje.remove(pozycja)
                except ValueError:
                    pass
            else:
                try:
                    wydatki += float(pozycja["WW"])
                except KeyError:
                    pozycja["WW"] = "0"
    return wydatki, pozycje

print(get_wydatki(sprawo2, 'SZKOŁA PODSTAWOWA NR 5 IM. HENRYKA SIENKIEWICZA', rozdzial="80101"))

