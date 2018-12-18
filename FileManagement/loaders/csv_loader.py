import csv

class CsvLoader(object):
    
    
    # ===========================
    # Constructor
    # ===========================
    def __init__(self, file_name):
        
        self.__file_name = file_name
        
        self.__rows = []
        
        self.__read_csv_file__(self.__file_name)
    
    # ==========================
    # Read Csv File
    # ==========================
    def __read_csv_file__(self, file_name):
        with open(file_name, 'rU') as file:
            self.__rows = [{key: value for key, value in row.items()} 
            for row in csv.DictReader(file, skipinitialspace=True)]
    
    # ==========================
    # Get Rows
    # ==========================
    @property        
    def rows(self):
        return self.__rows