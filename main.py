from extract import extract
from transform import transform
from load import load


data = extract()

clean_data = transform(data)

load(clean_data)

print("ETL terminé avec succès !")