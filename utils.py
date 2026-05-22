import pandas as pd

"""def load_data():
    return pd.read_csv('data/titanic.csv')"""
#Change in utils.py the function, so that only men are returned.

def load_data():
    data = pd.read_csv('data/titanic.csv')
    return data[data['sex'] == 'male']

# function to clean data that has as input a pd data frame. it drops missing values, converts categorical variables to lowercase and returns a cleaned data frame.
def clean_data(df):
    """Cleans the data by dropping missing values and converting categorical variables to lowercase"""
    df = df.copy()
    df = df.dropna()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()
    return df