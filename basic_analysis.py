import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Data_cleaning_coffee():

    


    def get_data():

        Raw_coffee_data=pd.read_csv('./data/coffee.csv')   

        #removing irrelavant rows  
        coffee_data=Raw_coffee_data[Raw_coffee_data['Species']=="Arabica"]  
        #renaming columns  
        coffee_data=coffee_data.rename(columns={"Country.of.Origin" : "Country_of_Origin","Farm.Name":"Farm_Name","Total.Cup.Points" : "Total_Cup_Points","Processing.Method" : "Processing_Method"})

        #drop columns whose data is less than 70%  
        total_count=coffee_data.count()
        all_columns=coffee_data.columns

        j=0
        drop_columns=[]
        for i in total_count:  
            if (i/coffee_data.shape[0])<0.80:  
                drop_columns.append(all_columns[j])

            j=j+1      
        #After analysis which columns to keep and which ones to drop   

        coffee_data=coffee_data.drop(['Lot.Number', 'Mill'],axis=1)



        coffee_data.head()

        #checking the size of data 
        #print(coffee_data.shape[0])
        #print(pd.value_counts(coffee_data.Species))   

        #coffee_data.drop([f'{Typica}"',"09e3c859cac41901d54f4bd36cce80d19c9272f5"",f'{2013/2014}"' ,f''{unex guatemala, s.a.}'',f''{Specialty Coffee Association}"',"CQI Taiwan ICP CQI??????",f'{KlemOrganics}"'])   

        #Checking for owner column 
        #print(pd.value_counts(coffee_data.Owner)) 


        #Replacing missing values in Owner Column  
        coffee_data.loc[(coffee_data['Farm_Name'] =="los hicaques"), 'Owner'] = "bismarck castro"  
        coffee_data=coffee_data.drop([602,848,882])

        bool_series = pd.isnull(coffee_data["Owner"])  
        coffee_data[bool_series]   

        #only_Honduras=coffee_data[coffee_data['Country_of_Origin']=="Colombia"][['Owner','Country_of_Origin','Farm_Name']] 

        #only_Honduras= only_Honduras.groupby(['Owner', 'Farm_Name']).size().reset_index(name='Freq')  
        #only_Honduras[only_Honduras['Farm_Name']=="supply chain ecom cca s.a."]   

        #checking missing values in country of origin  
        #print(pd.value_counts(coffee_data.Country_of_Origin)) 
        bool_series = pd.isnull(coffee_data["Country_of_Origin"])  
        coffee_data[bool_series]   


        #Checking values in altitude   

        #print(pd.value_counts(coffee_data.Region)) 
        bool_series = pd.isnull(coffee_data["Region"]) 
        #print(coffee_data[bool_series])




        for i in range(18,31): 
            coffee_data[coffee_data.columns[i]]=pd.to_numeric(coffee_data[coffee_data.columns[i]], errors='coerce')


        #print(coffee_data.mean(axis=0,skipna=True))
        return coffee_data
