import pandas as pd
from scipy import stats

from main6 import mean_age

data = {
    'City_A': [23, 53, 25, 74, 35, 54, 47, 21, 17, 46, 43],
    'City_B': [37, 38, 71, 42, 17, 19, 27, 35, 23, 38, 44]
}

df = pd.DataFrame(data)

mean_age_A = df['City_A'].mean()
median_age_A = df['City_A'].median()
mode_age_A = df['City_A'].mode()[0]
variance_age_A = df['City_A'].var()
std_age_A = df['City_A'].std()

print(f"City A. Mean: {mean_age_A}, median: {median_age_A}, mode: {mode_age_A}, variance: {variance_age_A}, std: {std_age_A}")

mean_age_B = df['City_B'].mean()
median_age_B = df['City_B'].median()
mode_age_B = df['City_B'].mode()[0]
variance_age_B = df['City_B'].var()
std_age_B = df['City_B'].std()

print(f"City B. Mean: {mean_age_B}, median: {median_age_B}, mode: {mode_age_B}, variance: {variance_age_B}, std: {std_age_B}")

t_stat, p_value = stats.ttest_ind(df['City_A'], df['City_B'])
print(f"T-test: {t_stat}, P-value: {p_value}")