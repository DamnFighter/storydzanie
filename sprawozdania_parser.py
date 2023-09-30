from xml_parser import get_data


sprawo = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Wydatki.xml')
sprawo2 = get_data(r'dane_kutno\Sprawozdania[2023][IIKwartał] Wydatki.xml')
sprawo3 = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Dochody.xml')


def get_szkola(sprawozdanie, szkola):
    for sz in sprawozdanie["Jednostka"]["Jednostki"]:
        if sz["Nazwa"] == szkola:
            return sz["Nazwa"]


def get_wydatki(sprawozdanie, szkola, dzial=None, rozdzial=None, grupa=None, paragraf=None):
    def get_szkola():
        for sz in sprawozdanie["Jednostka"]["Jednostki"]:
            if sz["Nazwa"] == szkola:
                return sz["Nazwa"]
    szkola = get_szkola()["Sprawozdania"]["Rb-28s"]
    # for pozycja in szkola["jednostka"]:
    #     if dzial
