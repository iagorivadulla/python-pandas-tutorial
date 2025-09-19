import pandas as pd
import numpy as np

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

print(data_frame)

series = pd.Series([23,45,7,34,6,63,36,78,54,34])

dates = pd.date_range('2021-05-01', '2021-05-12')

my_series = pd.Series([2, 4, 6, 8, 10])
my_series = my_series.apply(lambda x: x/2 )

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    }
]


df = pd.DataFrame(data)
new_data = { "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"}
df.loc[len(df)] = new_data 



df = pd.read_csv('.learn/assets/pokemon_data.csv')
printeable = df.iloc[133, 6]

printable2 = df.head(3)
printable3 = df.tail(3)

printable4 = df[['Name', 'Type 1']][0:10]
printable5 = df.loc[df['Attack'] > 80]

printable6 = len(df.loc[df['Legendary'] == True])


'''Exercices 6'''

df = pd.read_csv('.learn/assets/us_baby_names_right.csv')

printable7= df.head(5)

df = df.drop('Unnamed: 0', axis=1)
printable8 = df.head(5)
printable9 = df.value_counts('Gender')

printable10 = len(df.groupby(by='Name').sum())
print(printable10)