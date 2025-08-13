# from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# y_true = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
# y_pred = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1]
#
# accuracy = accuracy_score(y_true, y_pred)
# precision = precision_score(y_true, y_pred)
# recall = recall_score(y_true, y_pred)
# f1 = f1_score(y_true, y_pred)
#
# print(f'Accuracy: {accuracy}')
# print(f'Precision: {precision}')
# print(f'Recall: {recall}')
# print(f'F1-Score: {f1}')

# from sklearn.model_selection import cross_val_score
# from sklearn.ensemble import RandomForestClassifier
# import numpy as np
#
# X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# y = [0, 1, 0, 1, 0]
#
# model = RandomForestClassifier()
#
# scores = cross_val_score(model, X, y, cv=2)
# print(f'Оценки точности для каждого разбиения: {scores}')
# print(f'Средняя точность модели: {np.mean(scores)}')

# from sklearn.model_selection import GridSearchCV
# param_grid = {
#     'n_estimators': [10, 50, 100],
#     'max_depth': [None, 10, 20],
#     'min_samples_split': [2, 5, 10]
# }
#
# model = RandomForestClassifier()
#
# grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=2)
# grid_search.fit(X, y)
#
# print(f'Лучшие параметры: {grid_search.best_params_}')

import pandas as pd

data = {
    'age': [25, 45, 35, 50, 23, 40, 60, 30, 47, 38],
    'income': [50000, 120000, 70000, 150000, 40000, 80000, 30000, 60000, 100000, 75000],
    'years_with_bank': [1, 10, 5, 20, 2, 7, 25, 3, 15, 8],
    'is_active': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    'churned': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
print(df)

from sklearn.model_selection import train_test_split

X = df[['age', 'income', 'years_with_bank', 'is_active']]
y = df['churned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Обучающая выборка: {X_train.shape}')
print(f'Тестовая выборка: {X_test.shape}')

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

from sklearn.metrics import classification_report

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.1, 1, 10],
    'solver': ['liblinear', 'lbfgs']
}

grid_search = GridSearchCV(estimator=LogisticRegression(max_iter=1000), param_grid=param_grid, cv=2)
grid_search.fit(X_train, y_train)

print(f'Лучшие параметры: {grid_search.best_params_}')

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

print(classification_report(y_test, y_pred))