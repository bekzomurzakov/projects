import pandas as pd

data = {
    "product": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    "sales": [250, 300, 150, 200, 300, 350, 400, 300, 450, 500]
}

df = pd.DataFrame(data)

mean_sales = df['sales'].mean()
print(f'Среднее значение продаж: {mean_sales}')

median_sales = df['sales'].median()
print(f'Медиана продаж: {median_sales}')

mode_sales = df['sales'].mode()[0]
print(f'Мода продаж: {mode_sales}')

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['sales'], kde=True, bins=10)
plt.title('Распределение продаж')
plt.xlabel('Продажи')
plt.ylabel('Частота')
plt.show()

from scipy.stats import ttest_1samp

test_stat, p_value = ttest_1samp(df['sales'], 300)
print(f'Статистика теста: {test_stat}')
print(f'p-value: {p_value}')

if p_value < 0.05:
    print('Отклоненяем нулевую гипотезу: Средний доход не равен 300')
else:
    print('Недостаточно доказательств для отклонение нулевой гипотезы')

from scipy.stats import shapiro

stat, p = shapiro(df['sales'])
print('Статистика: {stat}, p-value: {p}')

if p > 0.05:
    print('Данные подчиняются нормальному распределению')
else:
    print('Данные не подчиняются нормальному распределению')

