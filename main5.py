import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Alex'],
    'Age': [28, 54, 23, 57],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
# print(df[df['Age'] > 28])

# Первые 5 или последние 5 строк
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())