import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee_attrition.csv")

print("First 5 rows of dataset:")
print(df.head())

total_emp = len(df)
print("\nTotal Employees:", total_emp)

attrition_count = df['Attrition'].value_counts()
print("\nAttrition Count:\n", attrition_count)

attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
print("\nAttrition Rate (%):\n", attrition_rate)

# Department-wise Attrition

dept_attrition = df[df['Attrition']=="Yes"].groupby('Department').size()
print("\nDepartment-wise Attrition:\n", dept_attrition)

# Salary Analysis

salary_analysis = df.groupby('Attrition')['Salary'].mean()
print("\nAverage Salary by Attrition:\n", salary_analysis)

# Job Satisfaction & Work-Life Balance

satisfaction_attrition = df[df['Attrition']=="Yes"].groupby('JobSatisfaction').size()
print("\nJob Satisfaction vs Attrition:\n", satisfaction_attrition)

wlb_attrition = df[df['Attrition']=="Yes"].groupby('WorkLifeBalance').size()
print("\nWork-Life Balance vs Attrition:\n", wlb_attrition)

# Experience Analysis

exp_attrition = df[df['Attrition']=="Yes"].groupby('Experience').size()
print("\nExperience vs Attrition:\n", exp_attrition)

# Visualization
# Attrition Count

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Attrition')
plt.title("Attrition Count")
plt.show()

# Department-wise Attrition

plt.figure(figsize=(8,5))
sns.countplot(data=df[df['Attrition']=="Yes"], x='Department')
plt.title("Department-wise Attrition")
plt.show()

# Salary vs Attrition
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='Attrition', y='Salary')
plt.title("Salary vs Attrition")
plt.show()

# Job Satisfaction vs Attrition
plt.figure(figsize=(6,4))
sns.countplot(data=df[df['Attrition']=="Yes"], x='JobSatisfaction')
plt.title("Job Satisfaction vs Attrition")
plt.show()

# Work-Life Balance vs Attrition
plt.figure(figsize=(6,4))
sns.countplot(data=df[df['Attrition']=="Yes"], x='WorkLifeBalance')
plt.title("Work-Life Balance vs Attrition")
plt.show()

# Save Analysis Results

dept_attrition.to_csv("dept_attrition_python.csv", header=True)
salary_analysis.to_csv("salary_analysis_python.csv", header=True)
satisfaction_attrition.to_csv("satisfaction_attrition_python.csv", header=True)
wlb_attrition.to_csv("wlb_attrition_python.csv", header=True)
exp_attrition.to_csv("exp_attrition_python.csv", header=True)

print("\n✅ All analysis CSV files saved successfully!")