# import pandas package as pd
import pandas as pd
  
# Define a dictionary containing students data
data = {'Name': ['Mary', 'Joseph', 'John', 'Jane'],
                'Age': [21, 19, 20, 18],
                'Subjects': ['Math', 'English', 'Arts', 'Biology'],
                'Score': [88, 92, 95, 70] }
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Subjects', 'Score'])
  
print("Given Dataframe :\n", df)
  
print("\nIterating over rows using iterrows() method :\n")
  
# iterate through each row and select 
# 'Name' and 'Score' column respectively.
for index, row in df.iterrows():
    print (row["Name"], row["Score"])