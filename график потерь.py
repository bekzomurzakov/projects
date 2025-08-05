import numpy as np
import pandas as pd

np.random.seed(42)
age = np.random.randint(18, 65, size=100)
income = np.random.randint(20000, 120000, size=100)

# Метки
labels = np.array([1 if (a > 30 and i > 50000) else 0 for a, i in zip(age, income)])

# Создаем DataFrame
data = pd.DataFrame({"age": age, "income": income, "label": labels})
print(data.head())

from sklearn.model_selection import train_test_split

X = data[['age', 'income']].values
y = data['label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Обучающая выборка: {X_train.shape}')
print(f'Тестовая выборка: {X_test.shape}')

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Model
model = Sequential([
    Dense(16, input_dim=2, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Complete
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print(model.summary())

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=8)

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Точность модели: {accuracy:.2f}')

predictions = model.predict(X_test)

predicted_labels = (predictions > 0.5).astype(int)

comprarison = pd.DataFrame({"Actual": y_test, "Predicted": predicted_labels.flatten()})
print(comprarison.head())

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Обучение')
plt.plot(history.history['val_accuracy'], label='Валидация')
plt.title('Точность модели')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()
plt.show()

# График потерь
plt.plot(history.history['loss'], label='Обучение')
plt.plot(history.history['val_loss'], label='Валидация')
plt.title('Потери модели')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()
plt.show()