import json
from logic import login
from output_styles import options
from commands import add_student, print_record_in_merit_order, view_all_students, seat_management, create_user

CREDENTIALS = json.load(open("./data/credentials.json"))
COMMANDS_MAP = [
    {
        "name": "Add Student",
        "module": add_student
    },
    {
        "name": "View All Students",
        "module": view_all_students
    },
    {
        "name": "Print Record In Merit Order",
        "module": print_record_in_merit_order
    },
    {
        "name": "Seat Management",
        "module": seat_management
    },
    {
        "name": "Create User",
        "module": create_user
    }
]


def getCommandNames():
    names = []

    for command in COMMANDS_MAP:
        names.append(command["name"])

    return names


def open_admin_menu():
    options.output(table=getCommandNames(), title="Menu", borders=True)
    command_number = int(input("Enter command number: "))
    print("")  # Gap between input and output
    COMMANDS_MAP[command_number]["module"].execute()
    open_admin_menu()


def open_student_menu():
    print("Student menu yet to come")


def start():
    user_name = login.login(CREDENTIALS)
    user_rank = CREDENTIALS[user_name]["rank"]

    if (user_rank == "ADMIN"):
        open_admin_menu()
    elif (user_rank == "STUDENT"):
        open_student_menu()


if __name__ == "__main__":
    start()
