import pandas as pd

from src.etl.extract import Extract
from src.etl.transform import Transform
from src.etl.load import Load

from src.etl.visualize import genre_distribution


#ETL Process
#Extract 
extractor = Extract(source="./data/raw/books.csv")    
data = extractor.extract()

#Transform
transformer = Transform(data)
transformed_data = transformer.transform()

print(transformed_data)
loader = Load()
loader.load(transformed_data)

genre_distribution(transformed_data)