class Transform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def transform(self):
        print("Transforming data (cleaning)")
        print(self.dataframe)
        
        # return data