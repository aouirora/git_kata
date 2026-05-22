import pandas as pd

"""def load_data():
    return pd.read_csv('data/titanic.csv')"""
#Change in utils.py the function, so that only men are returned.

def load_data():
    data = pd.read_csv('data/titanic.csv')
    return data[data['sex'] == 'male']