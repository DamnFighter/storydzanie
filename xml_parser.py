import xmltodict


def get_data(xml_path):
    with open(xml_path, encoding="utf8") as f:
        sio_xml = f.read()
    return xmltodict.parse(sio_xml)
