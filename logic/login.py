def check_validity(userName, password, credentials):
    if (userName in credentials):
        if (credentials[userName]["password"] == password):
            return True

    return False


def login(credentials):
    while True:
        user_name = input("Enter username\n> ")
        password = input("Enter password\n> ")

        if (check_validity(user_name, password, credentials)):
            break
