import pandas as pd
import json


def create_json(excel_file, output_file, sheet_name):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    json_data = df.to_dict(orient='records')
    json_file = output_file

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_school_stanins(school, file):
    with open(file, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

    for item in data:
        for key, value in item.items():
            if school.lower() in value.lower():
                return item
            else:
                break


def get_skala_item(file, stanin, przedmiot):
    with open(file, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

    for item in data:
        for key, value in item.items():
            if key == "Stanin" and value == stanin:
                return item[przedmiot]

    raise Exception("No skala zmaczowana")


def count_efektywnosc(max_stanin, szkola_suma_stanin):
    wynik = round(100 * szkola_suma_stanin / max_stanin, 2)
    return str(wynik) + " %"


def get_stanin_level(school, file, year, subject_1="Język polski", subject_2="Matematyka", subject_3="Język angielski"):
    ilosc_subjectow = 3
    max_stanin_per_przedmiot = 9
    create_json(excel_file=file, output_file="staniny_szkol.json", sheet_name=year)

    item_json = get_school_stanins(school, file="staniny_szkol.json")
    sub1_stanin = item_json[subject_1]
    sub2_stanin = item_json[subject_2]
    sub3_stanin = item_json[subject_3]
    stanin_sum = item_json["Suma"]

    create_json(excel_file="./dane_kutno/Staniny2.xlsx", output_file="staniny_skala.json", sheet_name=year)

    sub1_percent = get_skala_item("staniny_skala.json", sub1_stanin, "Język polski")
    sub2_percent = get_skala_item("staniny_skala.json", sub2_stanin, "Matematyka")
    sub3_percent = get_skala_item("staniny_skala.json", sub3_stanin, "Język angielski")
    efektywnosc = count_efektywnosc(ilosc_subjectow*max_stanin_per_przedmiot, stanin_sum)

    return {subject_1: sub1_percent, subject_2: sub2_percent, subject_3: sub3_percent, 'Efektywność szkoły': efektywnosc}


print(get_stanin_level(school="Szkoła podstawowa nr 7", file="./dane_kutno/Staniny.xlsx", year="2022"))







