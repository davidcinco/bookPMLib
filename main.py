import pandas as pd

from etl.extract import Extract
from etl.transform import Transform
from etl.load import Load

from etl.visualize import genre_distribution


#ETL Process
#Extract 
extractor = Extract(source="./source/books.csv")    
data = extractor.extract()

#Transform
transformer = Transform(data)
transformed_data = transformer.transform()

genre_distribution(transformed_data)
# loader = Load(destination="./destination/books.csv")
# loader.load(data)