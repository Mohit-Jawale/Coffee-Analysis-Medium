from basic_analysis import Data_cleaning_coffee
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb



coffee_data=Data_cleaning_coffee.get_data()

select_countries=['Guatemala','Colombia','Indonesia','Kenya','Ethiopia','Brazil']


Regions_in_countries={}

count=0

cols=['ID', 'Species', 'Owner', 'Country_of_Origin', 'Farm_Name',
       'ICO.Number', 'Company', 'Altitude', 'Region', 'Producer',
       'Number.of.Bags', 'Bag.Weight', 'In.Country.Partner', 'Harvest.Year',
       'Grading.Date', 'Owner.1', 'Variety', 'Processing_Method', 'Aroma',
       'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity',
       'Clean.Cup', 'Sweetness', 'Cupper.Points', 'Total_Cup_Points',
       'Moisture', 'Category.One.Defects', 'Quakers', 'Color',
       'Category.Two.Defects', 'Expiration', 'Certification.Body',
       'Certification.Address', 'Certification.Contact', 'unit_of_measurement',
       'altitude_low_meters', 'altitude_high_meters', 'altitude_mean_meters']

Country=pd.DataFrame(columns=cols)


for i in select_countries:
    for j in range(0,coffee_data.shape[0]):
        if coffee_data.iloc[j].Country_of_Origin == i:
            Country=Country.append(coffee_data.iloc[j], ignore_index=True)
             

#finding out which countries have data in ft
foot_data=Country[Country['unit_of_measurement']=='ft'][['Country_of_Origin','Total_Cup_Points']]

#Deleting foot rows
Country=Country[Country.unit_of_measurement != 'ft']

     
g = sb.FacetGrid(Country, col="Country_of_Origin", hue="Region",col_wrap=2)
g.map(plt.scatter, "Total_Cup_Points", "altitude_high_meters", alpha=0.5)
g.set(xlim=(65,95), ylim=(0, 2500))


plt.show()