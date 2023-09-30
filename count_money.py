from xml_parser import get_data
from sprawozdania_parser import get_wydatki, get_dochody
from read_sio import get_sio_list, get_szkola, get_max_uczniow

spraw_wyd = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Wydatki.xml')
# sprawo2 = get_data(r'dane_kutno\Sprawozdania[2023][IIKwartał] Wydatki.xml')
spraw_doch = get_data(r'dane_kutno\Sprawozdania[2022][IVKwartał] Dochody.xml')

kwota_so = 34719019
# szkola = "SZKOŁA PODSTAWOWA NR 6"
szkola = '000903280'
wydatki, _ = get_wydatki(spraw_wyd, szkola)
dochody, _ = get_dochody(spraw_doch, szkola)
sio = get_sio_list(r'dane_kutno\SIO 30.09.2022.xml')
sio_szkola = get_szkola(sio, szkola)
subwencja_os = kwota_so / get_max_uczniow(sio)
liczba_uczniow = float(sio_szkola["Liczba uczniów"]) + float(sio_szkola["Liczba uczniów poza szkołą"])
subwencja_szkola = subwencja_os * liczba_uczniow
saldo = dochody + subwencja_szkola - wydatki
saldo_os = saldo / liczba_uczniow
pass
