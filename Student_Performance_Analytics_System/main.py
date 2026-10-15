"""
Student Performance Analytics System
Python + NumPy + Pandas mini project.
Run: python main.py
"""
from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "output"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load student records from a CSV file."""
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            "Keep students.csv inside the data folder."
        )
    df = pd.read_csv(path)
    required = {"Student_ID", "Name", "Department", "Python", "Maths", "AI", "Attendance"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {', '.join(sorted(missing))}")
    return df


def validate_marks(df: pd.DataFrame) -> None:
    """Check that marks are numeric and within 0..100."""
    subjects = ["Python", "Maths", "AI"]
    for subject in subjects:
        df[subject] = pd.to_numeric(df[subject], errors="coerce")
        if df[subject].isna().any() or not df[subject].between(0, 100).all():
            raise ValueError(f"{subject} marks must be numbers between 0 and 100.")
    df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")
    if df["Attendance"].isna().any() or not df["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be a number between 0 and 100.")


def calculate_grade(average: float) -> str:
    """Assign grade according to the documented grading scale."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def calculate_results(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with total, average, grade, and pass/fail fields."""
    result = df.copy()
    subjects = ["Python", "Maths", "AI"]
    result["Total"] = result[subjects].sum(axis=1)
    result["Average"] = np.round(result[subjects].mean(axis=1), 2)
    result["Grade"] = result["Average"].apply(calculate_grade)
    # Pass rule: at least 35 in every subject and attendance >= 75%.
    passed = result[subjects].ge(35).all(axis=1) & result["Attendance"].ge(75)
    result["Result"] = np.where(passed, "Pass", "Fail")
    return result


def print_report(df: pd.DataFrame) -> None:
    """Print summary, subject analysis, and top performers."""
    subjects = ["Python", "Maths", "AI"]
    print("\n" + "=" * 72)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print("\nSTUDENT RESULTS")
    columns = ["Student_ID", "Name", "Department", *subjects, "Total", "Average", "Grade", "Result"]
    print(df[columns].to_string(index=False))

    print("\nCLASS SUMMARY")
    print(f"Number of students : {len(df)}")
    print(f"Class average      : {df['Average'].mean():.2f}")
    print(f"Highest average    : {df['Average'].max():.2f}")
    print(f"Lowest average     : {df['Average'].min():.2f}")
    print(f"Pass count         : {(df['Result'] == 'Pass').sum()}")
    print(f"Fail count         : {(df['Result'] == 'Fail').sum()}")
    print(f"Pass percentage    : {(df['Result'] == 'Pass').mean() * 100:.2f}%")

    print("\nSUBJECT-WISE ANALYSIS")
    for subject in subjects:  # Loop required by the assignment
        print(
            f"{subject:8} | Average: {df[subject].mean():6.2f} "
            f"| Highest: {df[subject].max():3.0f} | Lowest: {df[subject].min():3.0f}"
        )

    print("\nTOP PERFORMERS (by average marks)")
    top = df.nlargest(min(3, len(df)), "Average")[["Student_ID", "Name", "Department", "Average", "Grade"]]
    print(top.to_string(index=False))


def main() -> None:
    try:
        raw = load_data()
        validate_marks(raw)
        results = calculate_results(raw)
        print_report(results)
        OUTPUT_DIR.mkdir(exist_ok=True)
        output_path = OUTPUT_DIR / "student_results.csv"
        results.to_csv(output_path, index=False)
        print(f"\nDetailed results saved to: {output_path}")
        print("Note: The provided dataset is sample/demo data; replace it with authorized real data if needed.")
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
        print(f"\nERROR: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
