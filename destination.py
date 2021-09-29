import sys
import os
from consts import SET_DEST_COMMAND


def set_destination():
    """
    Sets destination to a passed command line argument.
    """

    try:
        dest_i = sys.argv.index(SET_DEST_COMMAND) + 1
        path = sys.argv[dest_i]
    except:
        print("Please provide a path for output destination!")
        sys.exit()

    if os.path.exists(path):
        with open("dest.txt", "w") as f:
            f.write(f"DESTINATION={path}\\")
        print(f"Set destination to - {path}")

    else:
        print(f'Provided path "{path}" is not a valid absolute path!')


def print_destination():
    print(get_destination())


def read_destination():
    return get_destination()


def get_destination():
    with open("dest.txt", "r") as f:
        try:
            dest = f.readlines()[0].split("=")[1]
        except:
            print("No destination path provided!")
            sys.exit()

    return dest
