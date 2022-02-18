
def border_line():
    print("----------------------------------------------")


def output(table, **kwargs):
    count = 0
    title = kwargs.get("title", None)
    borders = kwargs.get("borders", False)

    if (borders):
        border_line()
    if (title):
        print(title)

    for option in table:
        print(f"{count} - {option}")
        count += 1

    if (borders):
        border_line()
