import pandas as pd
fileName = 'data-travel-phetchaburi-2018.csv'
travels = pd.read_csv(fileName)
desc = travels.describe()
print(desc)
