import pandas as pd
import xml.etree.ElementTree as ET

def load_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    records = []
    for record_elem in root.findall('record'):
        record = {}
        for field_elem in record_elem.findall('field'):
            name = field_elem.get('name')
            key = field_elem.get('key')
            value = field_elem.text
            record[name] = value
            if key:
                record[name + '_key'] = key

        records.append(record)

    df = pd.DataFrame(records)
    return df
