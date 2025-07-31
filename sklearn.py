import pandas as pd

data = {
    'area': [1500, 2200, 800, 1200, 1800, 2500],
    'bedrooms': [3, 4,2, 3, 4, 5],
    'age': [10, 5, 20, 15, 7, 3],
    'category': ['Standart', 'Luxury', 'Affordable', 'Affordable', 'Standart', 'Luxury']
}

df = pd.DataFrame(data)

from sklearn.model_selection import train_test_split

X = df[['area', 'bedrooms', 'age']]
y = df['category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(f'Обучающие данные: {X_train}')
# print(f'Тестовые данные: {X_test}')

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f'Прогнозируемые категории: {y_pred}')

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f'Точность модели: {accuracy}')

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plot_tree(model, feature_names=['area', 'bedrooms', 'age'], class_names=model.classes_, filled=True)
plt.show()