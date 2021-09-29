import sys
import os
from consts import SET_ORIGIN_COMMAND


def set_origin():
    """
    Sets origin to a passed command line argument.
    """

    try:
        orig_i = sys.argv.index(SET_ORIGIN_COMMAND) + 1
        path = sys.argv[orig_i]
    except:
        print("Please provide a path for origin!")
        sys.exit()

    if os.path.exists(path):
        with open("orig.txt", "w") as f:
            f.write(f"ORIGIN={path}\\")
        print(f"Set origin to - {path}")

    else:
        print(f'Provided path "{path}" is not a valid absolute path!')


def print_origin():
    print(get_origin())


def read_origin():
    return get_origin()


def get_origin():
    with open("orig.txt", "r") as f:
        try:
            dest = f.readlines()[0].split("=")[1]
        except:
            print("No origin path provided!")
            sys.exit()

    return dest
