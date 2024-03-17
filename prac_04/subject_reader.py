"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def get_data():
    """Read data from file and return it as a list of lists: subject, lecturer, number of students."""
    data = []  # Initialize an empty list to store the data
    input_file = open(FILENAME, 'r')
    for line in input_file:
        line = line.strip()  # Remove the newline character
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        data.append(parts)  # Append this list of parts to the data list
    input_file.close()
    return data

def display_subject_details(data):
    """Display the details of each subject from the data list."""
    for subject_detail in data:
        subject_code, lecturer, student_count = subject_detail
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

def main():
    data = get_data()
    display_subject_details(data)

main()
