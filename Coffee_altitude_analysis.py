from basic_analysis import Data_cleaning_coffee
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb



coffee_data=Data_cleaning_coffee.get_data()



#Country-Wise Total cup point average

coffee_data=coffee_data[coffee_data.unit_of_measurement != 'ft']

grp_coffee_data=coffee_data.groupby(['Country_of_Origin'],sort=False).mean()


grp_coffee_data.reset_index(level=0, inplace=True)
grp_coffee_data=grp_coffee_data.sort_values(by=['Total_Cup_Points'],ascending=False)
grp_coffee_data=grp_coffee_data[grp_coffee_data['Country_of_Origin'].isin(['Brazil','Mexico','Vietnam','Colombia','Indonesia','Kenya','Ethiopia','Peru','Honduras','Uganda'])]

ax=sb.scatterplot(x='Total_Cup_Points',y='altitude_high_meters',data=grp_coffee_data,hue='Country_of_Origin')
plt.ylim(0,3000)

plt.show()
