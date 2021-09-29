import os
import sys
import shutil
from origin import read_origin
from destination import read_destination


def move():
    orig = read_origin()
    dest = read_destination()

    if not os.path.exists(orig):
        print(f'Provided origin path "{orig}" does\'t exist!')
        sys.exit()
    elif not os.path.exists(dest):
        print(f'Provided destination path "{dest}" does\'t exist!')
        sys.exit()

    print(os.listdir(orig))
    files = os.listdir(orig)
    for file in files:
        shutil.move(orig + file, dest + file)

    print(os.listdir(orig))
