import xml.etree.ElementTree as ET


def parse_xml_to_dict(element):
    result = {}
    if len(element) == 0:
        return element.text
    for child in element:
        child_data = parse_xml_to_dict(child)
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result


def get_data(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    xml_dict = parse_xml_to_dict(root)
    return xml_dict
