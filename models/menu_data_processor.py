import json
import pandas as pd


class MenuDataProcessor:
    """A class for processing the incoming JSON data from 10bis API.
    Builds a table data structure in memory for simpler data representation (Pandas dataframe)"""
    def __init__(self, json_data):
        menu_dict = json.loads(json_data)  # Convert JSON data to python dictionary
        self.menu_df = pd.DataFrame(menu_dict)



