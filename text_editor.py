# This is the practise for my project -> Text editor!!!!

import os

# Working with the operating system -> to work with their files
# Read and writing in another file -> File handling


def read_data(filename):
    with open(filename, "r") as f:
        return f.read()

# Function creation for the writing into another file


def write_data(filename, content):
    with open(filename, "w") as f:
        return f.write(content)

# receiving or fetching the user input


def get_user_input():
    print("\n Enter your text you wanna edit ( type 'save' on a new line to save and exit):")

    lines = []
    while True:
        lines = input()
        if lines == "save":
            break
        lines.append(lines)

    return '\n'.join(lines)

# Calling of the main function


def main():
    filename = input("Enter the filename to open or create: ").strip()
    try:
        if os.path.exists(filename):
            print(read_data(filename))
        else:
            write_data(filename, '')

        content = get_user_input()
        write_data(filename, content)
        print(f'{filename} saved!...')
    except OSError:
        print(f'{filename} cannot be found/opened.')


if __name__ == '__main__':
    main()
