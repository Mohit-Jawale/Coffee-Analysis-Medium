from basic_analysis import Data_cleaning_coffee
import matplotlib.pyplot as plt
import seaborn as sb


#This is rough analysis of various columns.
coffee_data=Data_cleaning_coffee.get_data()

#print(coffee_data.info())
#print(coffee_data.describe())


#plt.ylim(0,3000)
#plt.xlim(40,100)
#plt.scatter(data=coffee_data,x='Total_Cup_Points',y='altitude_high_meters',alpha=0.05)
#plt.show()

ethopia_coffee=coffee_data[coffee_data['Country_of_Origin']=="Kenya"][['Total_Cup_Points','Country_of_Origin','Altitude','Moisture','unit_of_measurement','altitude_high_meters','Region','Processing_Method']]



print(ethopia_coffee)

R_coffee_data=ethopia_coffee.groupby(['Region']).size().reset_index(name='Freq')
print(R_coffee_data)

#plt.scatter(data=ethopia_coffee,x='Total_Cup_Points',y='altitude_high_meters',alpha=0.5)
#plt.xlim(75,90)
#plt.ylim(0,2000)
ax=sb.scatterplot(x='Total_Cup_Points',y='altitude_high_meters',data=ethopia_coffee,hue='Region')

plt.show()











