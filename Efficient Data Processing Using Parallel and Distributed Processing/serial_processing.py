import pandas as pd

def serial_processing():
    students_df = pd.read_csv("students.csv")
    fees_df = pd.read_csv("fees.csv")

    # Ensure student_id columns are cleaned and converted to integers
    students_df["student_id"] = students_df["student_id"].astype(str).str.strip().astype(int)
    fees_df["student_id"] = fees_df["student_id"].astype(str).str.strip().astype(int)

    # Function to find the most relevant fee submission date for a group
    def find_most_relevant_fee_date(group):
        date_counts = group["fee_submission_date"].value_counts()
        if all(date_counts == 1):  # If all dates are unique, return the latest one
            return group["fee_submission_date"].max()
        else:  # If there are duplicate dates, return the most frequent one
            return date_counts.idxmax()

    # Create a mapping of student_id to the most relevant fee submission date
    relevant_dates_mapping = fees_df.groupby("student_id").apply(find_most_relevant_fee_date).reset_index()
    relevant_dates_mapping.columns = ["student_id", "most_relevant_date"]

    # Process each student and print the most relevant fee submission date
    results = []
    for _, student_row in students_df.iterrows():
        student_id = student_row["student_id"]
        relevant_date_row = relevant_dates_mapping[relevant_dates_mapping["student_id"] == student_id]
        if not relevant_date_row.empty:
            relevant_date = relevant_date_row["most_relevant_date"].iloc[0]
            results.append(f"Student ID {student_id}: Most relevant fee submission date: {relevant_date}")
        else:
            results.append(f"Student ID {student_id}: No fee records found.")

    return results
