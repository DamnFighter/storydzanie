import pandas as pd
import json


def xls_json(excel_file, output_file):
    def get_subjects(excel):
        df = pd.read_excel(excel, nrows=1)
        column_names = df.columns.tolist()
        columns_to_remove = [col for col in column_names if "Unnamed" in col or "Zakres danych" in col]
        df.drop(columns=columns_to_remove, inplace=True)
        temp = []
        for element in df:
            temp.append(element)
        return temp

    subjects = get_subjects(excel_file)

    def modify_json_keys(data, subjects):
        modified_data = []
        column_set = ["liczba zdających", "wynik średni (%)", "odchylenie standardowe (%)",
                      "mediana (%)", "modalna (%)"]

        for item in data:
            new_item = {}
            for key, value in item.items():
                if any(element in key for element in column_set):
                    try:
                        idx = int(key[-1])
                        new_key = key
                        new_key = new_key[:-2]
                        new_key += f"_{subjects[idx]}"
                    except Exception as e:
                        idx = 0
                        new_key = key
                        new_key += f"_{subjects[idx]}"
                    finally:
                        new_item[new_key] = value
                else:
                    new_item[key] = value

            modified_data.append(new_item)

        return modified_data

    df = pd.read_excel(excel_file, skiprows=1)
    json_data = df.to_dict(orient='records')
    json_file = output_file

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    with open(output_file, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

    modified_data = modify_json_keys(data, subjects)

    with open(output_file, "w", encoding='utf-8') as json_file:
        json.dump(modified_data, json_file, indent=4, ensure_ascii=False)


xls_json("./dane_kutno/Wyniki_e8_szkoly_2022.xlsx")
xls_json("./dane_kutno/Wyniki_E8_szkoly_2023.xlsx")
