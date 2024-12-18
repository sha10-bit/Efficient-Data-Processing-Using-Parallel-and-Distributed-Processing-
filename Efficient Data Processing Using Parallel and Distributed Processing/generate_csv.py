import pandas as pd
from datetime import datetime, timedelta
import random

def generate_csv_files():
    # Generate data for students.csv
    num_students = 100
    students_data = {
        "student_id": [i + 1 for i in range(num_students)],
        "name": [f"Student_{random.randint(1000, 9999)}" for _ in range(num_students)],
        "roll_number": [f"RN{random.randint(10000, 99999)}" for _ in range(num_students)],
        "semester": [random.randint(1, 8) for _ in range(num_students)],
    }
    students_df = pd.DataFrame(students_data)
    students_df.to_csv("students.csv", index=False)

    # Generate data for fees.csv
    num_fees = 200
    fees_data = {
        "student_id": [random.randint(1, num_students) for _ in range(num_fees)],
        "fee_submission_date": [
            (datetime(2022, 1, 1) + timedelta(days=random.randint(0, 730))).strftime("%Y-%m-%d")
            for _ in range(num_fees)
        ],
    }
    fees_df = pd.DataFrame(fees_data)
    fees_df.to_csv("fees.csv", index=False)

    print("CSV files generated: students.csv and fees.csv")

if __name__ == "__main__":
    generate_csv_files()
