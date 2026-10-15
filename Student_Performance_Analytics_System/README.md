# Student Performance Analytics System

A Python mini project that analyzes student marks using **Pandas** and **NumPy**. It calculates totals, averages, grades, pass/fail status, class statistics, subject-wise performance, and top performers.

## Features
- Loads student data from `data/students.csv` into a Pandas DataFrame.
- Validates subject marks and attendance (0–100).
- Uses NumPy for averages and pass/fail classification.
- Uses reusable functions and loops.
- Calculates total and average marks for each student.
- Assigns grades using a clear grading scale.
- Finds class average, highest/lowest average, pass/fail counts, and pass percentage.
- Performs subject-wise analysis and lists the top 3 students.
- Saves detailed results to `output/student_results.csv`.

## Requirements
- Python 3.10 or newer (Python 3.12/3.13 is a good choice if installing packages gives trouble).
- Internet is required only to install the libraries; running the program is local.

## Run in VS Code
1. Extract the ZIP file.
2. Open the extracted `Student_Performance_Analytics_System` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:
   - Windows: `py -m venv .venv`
   - macOS/Linux: `python3 -m venv .venv`
5. Activate it:
   - Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
   - Windows Command Prompt: `.venv\Scripts\activate.bat`
   - macOS/Linux: `source .venv/bin/activate`
6. Install packages: `python -m pip install -r requirements.txt`
7. Run: `python main.py`
8. Find the generated report at `output/student_results.csv`.

If `py` is not recognized on Windows, try `python -m venv .venv`. If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`.

## Grading rule
| Average marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 40–59.99 | D |
| Below 40 | F |

## Pass/fail rule
A student passes only when **each subject mark is at least 35 and attendance is at least 75%**. Otherwise, the result is Fail. This is a sample rule chosen for the project; an institution may use different rules.

## Dataset
The included CSV contains ten fictional sample records. Replace it with authorized data if required. Keep these column names: `Student_ID`, `Name`, `Department`, `Python`, `Maths`, `AI`, `Attendance`. Marks and attendance must be numbers from 0 to 100.

## Project structure
```text
Student_Performance_Analytics_System/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── students.csv
├── docs/
│   ├── PROJECT_DOCUMENTATION.md
│   └── GITHUB_SUBMISSION_GUIDE.md
└── output/                  # generated when the program runs
```

## Limitations and future scope
This is a command-line data-analysis project, not a machine-learning system or web application. Possible future improvements include charts, CSV upload support, and a simple dashboard.
