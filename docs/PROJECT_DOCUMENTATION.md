# Project Documentation
## Student Performance Analytics System

### 1. Introduction
The Student Performance Analytics System is a Python-based data analysis mini project. It reads student records from a CSV dataset, processes marks, and produces summaries that can help users understand student and subject performance.

### 2. Problem Statement
Manually calculating totals, averages, grades, pass/fail status, and class-level summaries for multiple students can take time and lead to calculation errors. This project automates these calculations for a small dataset.

### 3. Objectives
- Organize student records in tabular form.
- Calculate total and average marks.
- Assign grades with a documented rule.
- Determine pass/fail results.
- Summarize class and subject performance.
- Identify the top-performing students.
- Export calculated results to a CSV report.

### 4. Technologies Used
- **Python:** program logic, functions, conditions, and loops.
- **Pandas:** CSV input, DataFrame operations, and tabular reporting.
- **NumPy:** numerical averages, rounding, and conditional result classification.
- **CSV:** lightweight input and output data format.
- **Visual Studio Code:** suggested development environment.

### 5. System Requirements
- Python 3.10 or newer.
- NumPy and Pandas installed from `requirements.txt`.
- VS Code or another Python editor.
- Windows, macOS, or Linux.

### 6. Input Data
The file `data/students.csv` contains these fields:
- `Student_ID`: unique sample identifier.
- `Name`: student's sample name.
- `Department`: academic department.
- `Python`, `Maths`, `AI`: marks out of 100.
- `Attendance`: attendance percentage.

The included data is fictional sample data.

### 7. Processing and Rules
1. Load the CSV into a Pandas DataFrame.
2. Check required columns and numeric ranges.
3. Add subject marks to calculate total marks (maximum 300).
4. Calculate the mean of the three subjects.
5. Assign grades:
   - 90 and above: A+
   - 80 to below 90: A
   - 70 to below 80: B
   - 60 to below 70: C
   - 40 to below 60: D
   - Below 40: F
6. Mark a student Pass only if every subject is at least 35 and attendance is at least 75%; otherwise mark Fail.
7. Calculate class statistics and subject averages, maximums, and minimums.
8. List up to three students with the highest average marks.
9. Export the calculated records to `output/student_results.csv`.

### 8. Modules / Functions
- `load_data()`: loads and checks the required columns.
- `validate_marks()`: validates marks and attendance.
- `calculate_grade()`: returns a grade for a student's average.
- `calculate_results()`: adds total, average, grade, and result columns.
- `print_report()`: displays student results and summaries.
- `main()`: coordinates execution and saves the output.

### 9. How to Run
1. Extract the project ZIP.
2. Open the project folder in VS Code.
3. Open a terminal and create/activate a virtual environment (see `README.md`).
4. Run `python -m pip install -r requirements.txt`.
5. Run `python main.py`.
6. Review the terminal report and `output/student_results.csv`.

### 10. Expected Output
The terminal displays each student's total, average, grade, and result, followed by class statistics, subject-wise averages, and top performers. The generated CSV contains the original fields plus `Total`, `Average`, `Grade`, and `Result`.

### 11. Testing
- **Normal input:** valid marks and attendance produce a report.
- **Invalid marks:** text or values outside 0–100 produce a clear validation error.
- **Missing columns:** a clear error identifies missing required columns.
- **Pass/fail boundary:** each subject must be at least 35 and attendance at least 75% to pass.

### 12. Conclusion
The project demonstrates fundamental Python programming, reusable functions, loops, Pandas DataFrames, NumPy calculations, and practical data analysis without requiring advanced machine learning.

### 13. Future Scope
- Add charts for subject averages and grade distribution.
- Support user-provided CSV files.
- Add department-wise reports.
- Create a simple web dashboard.
- Add export to PDF.
