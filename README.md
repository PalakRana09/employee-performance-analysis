### 🧠 Employee Data Analysis with Python
This project performs data cleaning, feature engineering, and insightful analysis on employee performance data using Pandas, and visualizes trends using Matplotlib and Seaborn. The output is saved as an organized multi-sheet Excel report.

## ✅ Tasks Performed
# 🔹 1. Data Cleaning
Loaded employee data using pandas.

Converted JoinDate to datetime format (dd-mm-yyyy).

Ensured Salary and PerformanceRating columns are numeric.

Handled any missing values by dropping or correcting records.

# 🔹 2. Feature Engineering
Added a Tenure column to show how many years each employee has been with the company:

Tenure = 2025 - Year(JoinDate)
Added a SalaryCategory column based on salary:

Low: Salary < 50,000

Medium: 50,000 ≤ Salary ≤ 90,000

High: Salary > 90,000

# 🔹 3. Aggregated Analysis (GroupBy / Pivot)
Generated key summary tables:

avg_salary_by_dept: Average salary per department

gender_count_by_dept: Count of employees by gender and department

avg_rating_by_dept: Average performance rating per department

low_performers: Employees with a performance rating ≤ 2

# 🔹 4. Output
All cleaned data and summary reports are exported to an Excel file employee_summary.xlsx with multiple sheets using pandas.ExcelWriter.

🧪 Bonus: Visualizations
Visualizations were created to make insights clearer:

📊 Bar Chart: Average Salary by Department

🥧 Pie Chart: Salary Category Distribution

Charts are saved as PNG files in the project directory.

