def format_name(full_name: str):
    return full_name.title()


if __name__ == '__main__':
    print("Enter full name: ")
    full_name_input = input()
    print("Formatted name =", format_name(full_name_input))
