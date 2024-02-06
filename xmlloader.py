import pandas as pd
import xml.etree.ElementTree as ET

def load_xml():
    tree = ET.parse('data/xmldata.xml')
    root = tree.getroot()

    # Extract data from XML and create a list of dictionaries
    data_list = []
    for record in root.findall('.//record'):
        data_dict = {}
        for field in record.findall('.//field'):
            data_dict[field.get('name')] = field.text if field.text else None
        data_list.append(data_dict)

    # Create a DataFrame
    df = pd.DataFrame(data_list)

    # Pivot the DataFrame
    df_pivot = df.pivot(index='Year', columns=['Country or Area', 'Item'], values='Value').reset_index()
    return df
