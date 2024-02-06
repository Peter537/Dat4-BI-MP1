import pandas as pd
import glob

class XlsxLoader:
    
    @staticmethod
    def load_data():
        excel_file = glob.glob('./*/*.xlsx')
        print(len(excel_file).__str__() + " files found" or "No file found")

        if not excel_file:
            return None
        
        dataframes = []

        for file in excel_file:
            df = pd.read_excel(file)
            dataframes.append(df)
        
        return dataframes

