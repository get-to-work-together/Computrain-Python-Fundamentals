import pandas as pd

filename_in = 'data.xlsx'
filename_out = 'resampled.xlsx'

df = pd.read_excel(filename_in, sheet_name='meteostat', index_col='time')

df_resampled = df.resample('15min').ffill()   # or .fillna, .nearest, .interpolate

df_resampled.to_excel(filename_out, sheet_name='resampled')
