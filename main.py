import pandas as pd

from etl.extract import Extract
from etl.transform import Transform
from etl.load import Load


#ETL Process
#Extract 
extractor = Extract(source="./source/books.csv")    
data = extractor.extract()

#Transform
transformer = Transform(data)
transformer.transform()

# loader = Load(destination="./destination/books.csv")
# loader.load(data)