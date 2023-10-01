# -*- coding: utf-8 -*-
from xml_parser import get_data


def pp(d, ind=''):
    if isinstance(d, dict):
        for k, v in d.items():
            print("{}{}:".format(ind, k))
            pp(v, ind+4*' ')
    elif isinstance(d, (list, tuple)):
        for i in d:
            pp(i, ind)
    else:
        print("{}{}".format(ind, d))


def get_sio_list(sio_file_path):
    sio = get_data(sio_file_path)

    headers = {}
    sio_list = []

    for ind, i in enumerate(sio['Workbook']['Worksheet'][0]["Table"]["Row"]):
        if ind < 5:
            continue
        sio_dict = {}
        if 'Cell' in i:
            for idx, j in enumerate(i["Cell"]):
                if isinstance(j, dict):
                    if ind == 5:
                        headers[idx] = j["Data"]["#text"]
                    else:
                        sio_dict[headers[idx]] = j["Data"].get("#text", None)
            sio_list.append(sio_dict)
    return sio_list


def get_szkola(sio, szkola):
    for sz in sio:
        if "Regon".upper() in sz and sz["Regon".upper()] == szkola:
            return sz


def get_max_uczniow(sio):
    return float(sio[-1]["Liczba uczniów"]) + float(sio[-1]["Liczba uczniów poza szkołą"])


def get_sio_students(sio_file_path):
    sio = get_data(sio_file_path)

    headers = {}
    sio_list = []

    for ind, i in enumerate(sio['Workbook']['Worksheet']['Table']['Row']):
        if ind < 2:
            continue
        sio_dict = {}
        for idx, j in enumerate(i['Cell']):
            if 'Data' in j:
                if ind == 2:
                    headers[idx] = j['Data']['#text']
                else:
                    sio_dict[headers[idx]] = j['Data'].get("#text", None)
        sio_list.append(sio_dict)
    return sio_list


get_sio_works = get_sio_students
