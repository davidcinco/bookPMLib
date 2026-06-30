import pandas as pd

class Extract:
    def __init__(self, source):
        self.source = source

    def extract(self):
        print(f"Extracting and returning data")
        df = pd.read_csv(self.source)
        return df       