from basic_analysis import Data_cleaning_coffee
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb



coffee_data=Data_cleaning_coffee.get_data()



#AS by research from google i found out that semi-dry and honey are almost same and can combine

coffee_data.loc[coffee_data['Processing_Method']=='Pulped natural / honey', 'Processing_Method'] = 'Semi-washed / Semi-pulped'



new_coffee_data=coffee_data[coffee_data['Country_of_Origin'].isin(['Brazil','Mexico','Vietnam','Colombia','Indonesia','Kenya','Ethiopia','Peru','Honduras','Uganda'])][['Country_of_Origin','Processing_Method']]

new_coffee_data_freq=pd.value_counts(new_coffee_data.Processing_Method)

new_coffee_data= new_coffee_data.groupby(['Country_of_Origin', 'Processing_Method']).size().reset_index(name='Freq') 
print(new_coffee_data)
print(new_coffee_data_freq)









