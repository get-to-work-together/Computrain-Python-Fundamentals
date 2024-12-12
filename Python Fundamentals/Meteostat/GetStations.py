import pandas as pd
from meteostat import Stations

pd.set_option('display.max_rows', 1000)

stations = Stations()
stations = stations.region('NL')

df = stations.fetch(1000)

print(df.columns)

print('Stations', stations.count())

print(df['name'])

de_bilt = df.loc['06260']   # de Bilt

print(de_bilt)