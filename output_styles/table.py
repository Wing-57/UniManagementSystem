
def print_field_names(names):
    # In the end will be in form to have the formatting of :<10 for the amount of field names there are
    end_formatting_string = ""
    for name in names:
        # aligns to the left and sets width of 10
        end_formatting_string += "{:<15s}"

    # '*' operator unpacks a tuple, putting each string as a seperate argument to the format function
    print(end_formatting_string.format(*names))


def print_list(list):
    # would look like:
    # [["Value1", "Value2"], ["Value1", "Value2"]]
    for item in list:
        end_formatting_string = ""
        for values in item:
            end_formatting_string += "{:<15}".format(str(values))
        print(end_formatting_string)


def output(list, field_names):
    print_field_names(field_names)
    print_list(list)
