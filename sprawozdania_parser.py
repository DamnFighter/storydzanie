from xml_parser import get_data
from copy import copy


sprawo = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Wydatki.xml')
sprawo2 = get_data(r'dane_kutno\Sprawozdania[2023][IIKwartał] Wydatki.xml')
sprawo3 = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Dochody.xml')
# sprawo4 = get_data(r'dane_kutno\SIO 30.09.2022.xml')


def get_szkola(sprawozdanie, szkola):
    for sz in sprawozdanie["Jednostka"]["Jednostki"]:
        if sz["Nazwa"] == szkola:
            return sz


def get_wydatki(sprawozdanie, szkola, dzial=None, rozdzial=None, grupa=None, paragraf=None):
    szkola = get_szkola(sprawozdanie, szkola)["Sprawozdania"]["Rb-28s"]
    pozycje = copy(szkola["Pozycje"])

    for klucz, filtr in zip(("dzial", "rozdzial", "grupa", "paragraf"), (dzial, rozdzial, grupa, paragraf)):
        for pozycja in szkola["Pozycje"]:
            if filtr and filtr != pozycja[klucz]:
                pozycje.remove(pozycja)

    wydatki = sum([int(wydatek) for wydatek in pozycje["WW"]])
    return wydatki



pass