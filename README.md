# Coffee-Beans-Analysis-Medium-Code

Here i'm trying to Understand different factors which affects coffee beans.After the brief analysis of dataset by coffee Quality Institute which is availabe on kaggle.

I found that data needed lot of cleaning,which in have performed in my basic_analysis module.Futher i'm trying to get various answers here related to coffee which in have mentioned in my medium blog "Understanding Arabica coffee beans with altitude".Here is link to the blog https://medium.com/@jawale.mohit123/understanding-arabica-coffee-beans-with-altitude-794063302905

The analysis is mostly focused on the fact that haunt me for long time when i heard it from my friend that coffee taste varies with the altitude at which it is grown.so to answer my curiosity i have perform this analysis and also im coffee lover.

Here in the analysis i have used python as my analysis language and various data science libraries which are as follows-:

1)Pandas.
2)Numpy.
3)Seaborn.
4)matplotlib.

I have mainly used descriptive analysis for analysis above dataset.

Note-: Main_analysis jupyter notebook have all the codes in it.

## Question Discussion

**1)Does the Altitude of the coffee plantation affects its characteristics?**

* Business Understanding-: To understand what are the effects on the characterisctics of coffee.
* Data Understanding-: Found that various place has different taste rating whcih was facinating as coffee at same place have different rating.
* Prepare Data-:clean data which has lot of null values there was not point imputing them as there was ambiguity.
* Data Modeling-: Choose top 6 countries which has highest coffee produciton with different regions with different altitude.
* Evaluate the Results-:used scatter plot to evalutate the result that with altitude the characteristics changes.



**2)Among the top 10 Coffee Producing Nations which one has the Best Coffee?**

* Business Understanding- If someone has to select which coffee to choose for his new cafe or just to buy it from lot of overwhelmming chooses how he/she will select it.
* Data Understanding-: Grouped all the data from the top 10 coffee producing nation together.
* Prepare Data-: cleaed all the unnessesary data like outliers in the brazil data even etc.
* Data Modeling-: Took avg of the top 10 countries total cup points and grouped them in dataframe.
* Evaluate the Results-: ploted scatter plot of countries vs altitude to understand which coffee has better charactertics.


**3)Among the top 10 Coffee Producing Nations which Processing Method is used by Most of them?**

* Business Understanding-:Try to understand which processing method is good after select the coffee.after so much effort we dont want to ruin our coffee just by not knowing the right processing method.
* Data Understanding-:Grouped all the data on the processing method .
* Prepare Data-:There were cleaning as well as merging of two data columns.
* Data Modeling-:country-wise modeled all the data based on different method they use.
* Evaluate the Results-:Most of them have Natural /dry processing methods (8/10), All of them used the washed /wet(10/10)processing method and some of them have semi-washed /semi-pulped.


