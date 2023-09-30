import mxltodict


def get_data(xml_path):
    with open(SIO_PATH) as f:
        sio_xml = f.read()
    return xmltodict.parse(sio_xml)
