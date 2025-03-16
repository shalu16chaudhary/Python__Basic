import pandas as pd
import numpy as np

data = pd.read_csv("student-mat.csv")
df = pd.DataFrame(data)

print(df.loc[:,'school':'guardian'])


capitalize = lambda s: s.capitalize()


print(capitalize("Mjob"))  
print(capitalize("Fjob"))

# Using lambda function to capitalize each name
# df['Mjob'] = df['Fjob'].apply(lambda x: x.capitalize())

print(df.iloc[-1])
print(df['guardian'].iloc[-1])




