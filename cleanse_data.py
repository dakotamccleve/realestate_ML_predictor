import pandas as pd

data = pd.read_csv('./data/realtor-data.csv')
data.drop_duplicates(inplace=True)
data = data.drop(columns=['status', 'sold_date', 'street', 'full_address'])
data.dropna(inplace=True)
data.drop(data[data.price > 10000000].index, inplace=True)
data.drop(data[data.house_size > 10000].index, inplace=True)
data.info()
data.to_csv('./data/parsed_data.csv')
data = data.drop(columns=['bed', 'bath', 'acre_lot', 'city', 'state', 'zip_code'])
data.info()
data.to_csv('./data/predict_data.csv')
