import numpy as np

salaries = np.array([50, 23, 60, 26, 19, 43, 26, 64, 60, 45, 26, 57, 54])

# average salary
mean_salary = np.mean(salaries)
print(f"Average salary: {mean_salary}K")

# Max and Min
max_salary = np.max(salaries)
min_salary = np.min(salaries)
print(f"Max salary: {max_salary}K")
print(f"Min salary: {min_salary}K")

std_salary = np.std(salaries)
print(f"Std salary: {std_salary}K")

above_mean = salaries[salaries > mean_salary]
print(f"Above mean: {above_mean}K")