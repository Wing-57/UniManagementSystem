import json
from output_styles import table
from models import students as students_

# This function will create a new students table which will remove headers, such as: ECAT, Preferences etc.


def sort_students(students):
    listed_students = []

    for student in students:  # variable `student` is the name of each student
        # Gets values of each key, eg `"ECAT": 322` will give `322`. We then typecast it to a list.
        values = list(students[student].values())
        # Since the name is not already part of the table, we must insert it in
        values.insert(0, student)
        # Add list to the overall list of students
        listed_students.append(values)

    return listed_students


def execute():
    students = json.load(open("./data/students.json")) or {}

    if (len(students) == 0):
        # Checking if number of students is equal to 0
        print("There are no students currently indexed")
        return

    table.output(sort_students(students),
                 ["Name"]+list(students_.model().keys()))
