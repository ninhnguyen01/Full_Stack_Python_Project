# Import package
import pandas as pd

# Specify the file name
file_name = 'automation_excel/insurance.csv'
    
# Read the data in the dataframe
if file_name.endswith('.csv'):
    df = pd.read_csv(file_name)
    print(df.info())
    print(df.head())
elif file_name.endswith('.xlsx'):
    df = pd.read_excel(file_name)
    print(df.info())
    print(df.head())
