import pandas as pd



data =  {
    'Name':['Abhi','Siddhi','Chetan'],
    'Age': [26,24,30],
    'City': ['Mysore','Hubli','Bangalore']
}

df = pd.DataFrame(data)
"""print(df)"""   


"""df = pd.read_csv('data.csv')
print(df.head())
print(df.tail())

print(df.info())
print(df.describe())

print(df.get('Email_ID'))

print(df.iloc[0])

filter_df = df[df['Emp#'] >= 58209 ]"""

df = df.drop(columns=['Name'])


df = df.drop(index=0)

print(df.head())


