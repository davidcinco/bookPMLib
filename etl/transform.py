class Transform:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def transform(self):
        print("Transforming data (cleaning)")
        #Verify how many NaN/Null values are in our dataframe
        print(self.df.isnull().sum())
        
        #Set NaN/Null values in the "Author" column to "Unknown"
        self.df["Author"] = self.df["Author"].fillna("Unknown")
        
        # Set NaN/Null values in the "Publisher" column to "Unknown"
        self.df["Publisher"] = self.df["Publisher"].fillna("Unknown")
        
        return self.df