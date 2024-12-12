# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Hourly

# Set time period
start = datetime(2023, 1, 1, 0, 0, 0)
end = datetime(2023, 12, 31, 23, 0, 0)

# Create Point for De Bilt, NL
de_bilt = Point(52.1, 5.1833, 2.0)

# Get daily data for 2023
data = Hourly('06260', start, end)
data = data.fetch()

data.to_excel('data.xlsx', sheet_name='meteostat')

# # Plot line chart including average, minimum and maximum temperature
# data.plot(y=['tavg', 'tmin', 'tmax'])
# plt.show()