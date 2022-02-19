import json
from output_styles import options
from models import students as students_

PREFERENCES_OPTIONS = [
    {
        "full_name": "Computer Science",
        "abbreviate": "CS"
    },
    {
        "full_name": "Computer Engineering",
        "abbreviate": "CE"
    },
    {
        "full_name": "Electrical Engineering",
        "abbreviate": "EE"
    }
]

students = json.load(open("./data/students.json")) or {}


def get_abbreviates():
    abbreviates = []

    for specialisation in PREFERENCES_OPTIONS:
        abbreviates.append(specialisation["abbreviate"])

    return abbreviates


def get_preferences():
    names = []

    for specialisation in PREFERENCES_OPTIONS:
        names.append(specialisation["full_name"])

    return names


def insert_to_table(studentName, settings):
    students[studentName] = settings
    json.dump(students, open("./data/students.json", "w"))


def output_preferences():
    preferences = []
    options.output(table=get_preferences(),
                   title="Choose from the following:", borders=True)

    for i in range(3):
        preference_index = int(input(f"Preference {i+1}: "))
        preferences.append(get_abbreviates()[preference_index])

    return preferences


def execute():
    student_name = input("Student Name: ")
    settings = {}
    students_model = students_.model()

    for key in students_model:
        if (key == "Preferences"):
            continue
        settings[key] = input(f"{key} ({type(students_model[key])}): ")

    settings["Preferences"] = output_preferences()

    insert_to_table(studentName=student_name, settings=settings)
