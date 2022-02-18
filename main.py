import json
from logic import login
from output_styles import options
from commands import add_student, print_record_in_merit_order, view_all_students

CREDENTIALS = json.load(open("./data/credentials.json"))
COMMANDS_MAP = [
    {
        "name": "Add Student",
        "module": add_student
    },
    {
        "name": "Print Record In Merit Order",
        "module": print_record_in_merit_order
    },
    {
        "name": "View All Students",
        "module": view_all_students
    }
]


def getCommandNames():
    names = []

    for command in COMMANDS_MAP:
        names.append(command["name"])

    return names


def open_menu():
    options.output(table=getCommandNames(), title="Menu", borders=True)
    command_number = int(input("Enter command number: "))
    print("")  # Gap between input and output
    COMMANDS_MAP[command_number]["module"].execute()
    open_menu()


if __name__ == "__main__":
    login.login(CREDENTIALS)
    open_menu()
