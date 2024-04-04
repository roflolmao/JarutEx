import pandas as pd
fileName = 'data-travel-phetchaburi-2018.csv'
travels = pd.read_csv(fileName)
print("Pandas Version : ", pd.__version__)
print(travels.info())
print('Shape = ',travels.shape)
print(travels.head())
print(travels.tail())
print(travels.sample())
travels.to_csv('data-travel-result.csv')
travels.to_json('data-travel-result.json')
