#1 import necessary library
import pandas as pd
import numpy as np



#2 import data set
#3 assign it to variable called crime 
crime = pd.read_csv("US_Crime_Rates_1960_2014.csv")
print(crime.head())



#4 wahts is the type of column
print(crime.dtypes)  # attribute to get the data tyoe of each column




#5 covert the type column year into datetime64
crime['Year'] = pd.to_datetime(crime['Year'], errors='coerce')
print(crime.dtypes)





#6 set the year column as index of dataframe
# crime.set_index('Year', inplace=True)
# print(crime.head())






#7 delete the total column
# print(crime.drop(columns=['Total'], inplace=True))






#8 group the year by decade and sum the value
crime['Year'] = crime['Year'].astype(int)
crime['Decade'] = (crime['Year'] // 10) * 10  # Convert Year to Decade
result = crime.groupby('Decade')['Total'].sum().reset_index()  # Group by Decade and Sum Values
print(result)




#9 what is most dangerous decade in the us
most_dangerous_decade = crime.loc[crime['Total'].idxmax()]


print(f"Most Dangerous Decade: {most_dangerous_decade['Decade']}")
print(f"Total Crime/Danger Value: {most_dangerous_decade['Total']}")




