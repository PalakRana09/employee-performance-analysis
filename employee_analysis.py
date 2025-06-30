
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Cleaning
df = pd.read_csv("employee_performance.csv")
df['JoinDate'] = pd.to_datetime(df['JoinDate'], format='%d-%m-%Y', errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['PerformanceRating'] = pd.to_numeric(df['PerformanceRating'], errors='coerce')
df = df.dropna()

# 2. Feature Engineering
df['Tenure'] = 2025 - df['JoinDate'].dt.year

def salary_category(salary):
    if salary < 50000:
        return "Low"
    elif salary <= 90000:
        return "Medium"
    else:
        return "High"

df['SalaryCategory'] = df['Salary'].apply(salary_category)

# 3. Aggregated Analysis
avg_salary_by_dept = df.groupby('Department')['Salary'].mean().reset_index()
gender_count_by_dept = df.groupby(['Department', 'Gender']).size().reset_index(name='Count')
avg_rating_by_dept = df.groupby('Department')['PerformanceRating'].mean().reset_index()
low_performers = df[df['PerformanceRating'] <= 2]

# 4. Output Excel File
with pd.ExcelWriter("employee_summary.xlsx") as writer:
    df.to_excel(writer, sheet_name='CleanedData', index=False)
    avg_salary_by_dept.to_excel(writer, sheet_name='AvgSalaryDept', index=False)
    gender_count_by_dept.to_excel(writer, sheet_name='GenderCountDept', index=False)
    avg_rating_by_dept.to_excel(writer, sheet_name='AvgRatingDept', index=False)
    low_performers.to_excel(writer, sheet_name='LowPerformers', index=False)

# Bonus: Visualizations
# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(avg_salary_by_dept['Department'], avg_salary_by_dept['Salary'], color='skyblue')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_avg_salary_by_dept.png")
plt.close()

# Pie Chart
category_counts = df['SalaryCategory'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title("Salary Category Distribution")
plt.axis('equal')
plt.tight_layout()
plt.savefig("pie_salary_category.png")
plt.close()
