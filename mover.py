import os
from re import sub
import sys
import shutil
from Configurator import Configurator
from configurate import validate_config, configurate
from origin import read_origin
from destination import read_destination
from tqdm import tqdm


def move():
    orig = read_origin()
    dest = read_destination()

    configurator = Configurator()

    if not os.path.exists(orig):
        print(f'Provided origin path "{orig}" does\'t exist!')
        sys.exit()
    elif not os.path.exists(dest):
        print(f'Provided destination path "{dest}" does\'t exist!')
        sys.exit()

    configurate(configurator)

    files = os.listdir(orig)
    pbar = tqdm(files)
    for file in pbar:
        pbar.set_description(f'Moving "{file}"')

        dest_sub_path = configurator.file_to_path[file]

        shutil.move(orig + file, dest + dest_sub_path + file)

    print("Moving completed!")
