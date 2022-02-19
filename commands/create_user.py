import json
from turtle import title
from models import credentials
from enums import rank
from output_styles import options

CREDENTIALS_MODEL = credentials.model()
CREDENTIALS_FILE_PATH = "data/credentials.json"


def insert_credentials(username, settings):
    file = json.load(open(CREDENTIALS_FILE_PATH))
    file[username] = settings
    json.dump(file, open(CREDENTIALS_FILE_PATH, "w"))


def get_input_for_fields():
    settings = {}

    for field in CREDENTIALS_MODEL:
        if (CREDENTIALS_MODEL[field] == rank.Rank):
            options.output(
                rank.Rank, title="Pick from the following:", borders=True)
            choice = int(input(f"{field}: "))
            field_value = rank.Rank(choice+1).name
        else:
            field_value = input(f"{field}: ")

        settings[field] = field_value

    return settings


def execute():
    username = input("Username: ")
    settings = get_input_for_fields()

    insert_credentials(username=username, settings=settings)
