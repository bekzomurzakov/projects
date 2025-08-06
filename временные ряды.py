import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Данные
data = {
    "date": pd.date_range(start='2022-01-01', periods=24, freq='M'),
    "sales": [305, 356, 378, 399, 450, 478, 505, 512, 490, 475, 460, 455,
              480, 520, 540, 580, 600, 630, 650, 670, 690, 710, 700, 680]
}

df = pd.DataFrame(data)
df.set_index("date", inplace=True)

# График продаж
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sales'], marker='o', label='Продажи')
plt.title('Динамика продаж')
plt.xlabel('Дата')
plt.ylabel('Объем продаж')
plt.legend()
plt.grid()
plt.show()

# Сезонное разложение
result = seasonal_decompose(df['sales'], model='additive', period=12)
result.plot()
plt.tight_layout()
plt.show()

# Обучение модели SARIMAX
model = SARIMAX(df['sales'], order=(1, 1, 1), seasonal_order=(1, 0, 0, 12))
model_fit = model.fit(disp=False)

# Прогноз на следующий месяц
forecast = model_fit.forecast(steps=1)
print(f'Прогноз продаж на следующий месяц: {forecast.values[0]:.2f}')

df['forecast'] = result.predict(start=0, end=len(df) - 1)
future = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=1, freq='ME')
forecast_df = pd.DataFrame({'sales': forecast.values}, index=future)
df = pd.concat([df, forecast_df])

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sales'], marker='0', label='Исторические данные')
plt.plot(forecast_df.index, forecast_df['sales'], markers='x', color='red', label='Прогноз')
plt.title('Прогноз продаж')
plt.xlabel('Дата')
plt.ylabel('Объем продаж')
plt.legend()
plt.grid()
plt.show()