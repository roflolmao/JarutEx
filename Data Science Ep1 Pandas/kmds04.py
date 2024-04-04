import pandas as pd
fileName = 'data-travel-phetchaburi-2018.csv'
travels = pd.read_csv(fileName)
travels['total'] = travels.sum(axis=1)
print(travels)
Jan = travels['Jan']
print(":::::::: Jan. ::::::::")
print('\tsum = ',Jan.sum())
print('\tmin = ',Jan.min())
print('\tmax = ',Jan.max())
print('\tmean = ',Jan.mean())
