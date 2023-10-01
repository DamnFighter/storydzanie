from stanin_parser import get_stanin_level
from xml_parser import get_data
from sprawozdania_parser import get_wydatki, get_dochody
from read_sio import get_sio_list, get_szkola, get_max_uczniow


class Counter:
    def __init__(self, kwota_so=34719019):
        self.kwota_so = kwota_so
        self.spraw_wyd = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Wydatki.xml')
        self.spraw_doch = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Dochody.xml')
        self.sio = get_sio_list(r'dane_kutno\SIO 30.09.2022.xml')
        self.staniny = "./dane_kutno/Staniny.xlsx"

    def count_szkola(self, szkola, wydatki, dochody):
        sio_szkola = get_szkola(self.sio, szkola)
        subwencja_os = self.kwota_so / get_max_uczniow(self.sio)
        liczba_uczniow = float(sio_szkola["Liczba uczniów"]) + float(sio_szkola["Liczba uczniów poza szkołą"])
        subwencja_szkola = subwencja_os * liczba_uczniow
        saldo = dochody + subwencja_szkola - wydatki
        saldo_os = saldo / liczba_uczniow
        return saldo, saldo_os

    def count_for_all(self):
        szkoly = []
        if "Jednostki" in self.spraw_wyd:
            jednostki = self.spraw_wyd["Jednostki"]["Jednostka"]
        else:
            jednostki = self.spraw_wyd["PaczkaSprawozdan"]["Jednostki"]["Jednostka"]
        for szkola in jednostki:
            szkola_reg = szkola["Regon"]
            wydatki, lista_wydatkow = get_wydatki(self.spraw_wyd, szkola_reg)
            dochody, lista_dochodow = get_dochody(self.spraw_doch, szkola_reg)
            saldo, saldo_os = self.count_szkola(szkola_reg, wydatki, dochody)
            szkoly.append([szkola["Nazwa"], round(saldo, 2), round(saldo_os, 2), self.count_stanis(szkola)["Efektywnosc"], lista_wydatkow, lista_dochodow])
        return szkoly

    def count_stanis(self, szkola):
        return get_stanin_level(school=szkola["Nazwa"], file=self.staniny, year="2022")


if __name__ == "__main__":
    # Test countera
    a = Counter()
    x = a.count_for_all()
    print(x)

