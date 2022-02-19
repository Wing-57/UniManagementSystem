import json
from multiprocessing.sharedctypes import Value
from turtle import title
from output_styles import options

DATA_FILE = "data/seats.json"


def edit_capacity(subject: str):
    file = json.load(open(DATA_FILE))
    try:
        new_seats = int(input(f"Enter new {subject} capacity: "))
        file[subject] = new_seats
        json.dump(file, open(DATA_FILE, "w"))
    except:
        print("Something went wrong. Please make sure your input is a valid number.")


def output_seats():
    output_string = ""
    file = json.load(open(DATA_FILE))
    for name in file:
        seats = file[name]
        output_string += f"{name} : {seats}\n"

    print(output_string)


MENU_OPTIONS = [
    "Edit CS capacity",
    "Edit CE capacity",
    "Edit EE capacity",
    "View seats",
    "Back"
]

SEATS_OPTIONS = ["CS", "CE", "EE"]


def seats_menu():
    options.output(table=MENU_OPTIONS, title="Pick option:", borders=True)
    command_input = int(input())
    print("")
    return command_input


def execute():
    command_number = seats_menu()
    if (command_number in range(3)):
        subject = SEATS_OPTIONS[command_number]
        edit_capacity(subject)
    elif (command_number == 3):
        output_seats()
    else:
        return
