import os
import sys
import shutil
from origin import read_origin
from destination import read_destination
from tqdm import tqdm


def move():
    orig = read_origin()
    dest = read_destination()

    if not os.path.exists(orig):
        print(f'Provided origin path "{orig}" does\'t exist!')
        sys.exit()
    elif not os.path.exists(dest):
        print(f'Provided destination path "{dest}" does\'t exist!')
        sys.exit()

    files = os.listdir(orig)
    pbar = tqdm(files)
    for file in pbar:
        pbar.set_description(f'Moving "{file}"')
        shutil.move(orig + file, dest + file)

    print("Moving completed!")
