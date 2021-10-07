import os
from Configurator import Configurator
from origin import read_origin


def configurate(configurator: Configurator):
    validate_config()
    configurator.configurate()


def validate_config():
    orig = read_origin()
    files = os.listdir(orig)

    with open("config.txt", "r") as f:
        config = f.readlines()

    to_remove = []
    for line in config:
        item = line.split(" -> ")[0]
        if not (item in files):
            print(
                f'Invalid item "{item.strip()}" with config entry "{line.strip()}", deleting it.'
            )
            to_remove.append(line)

    for item in to_remove:
        config.remove(item)

    with open("config.txt", "w") as f:
        for item in config:
            f.write(item)

    for file in files:
        if not any(file in line for line in config):
            print(f'Item "{file}" doesn\'t have any destination configurated.')

            answer = ""
            while answer not in ["y", "n"]:
                answer = input(
                    f'Do you wish to move it just to the "{orig}"? (Y/N): '
                ).lower()

            if answer == "y":
                append_enrty_to_config(file, "")
            elif answer == "n":
                file_destination = input(f'Where to move file "{file}": ')
                append_enrty_to_config(file, file_destination)


def analyze_origin():
    files = os.listdir(read_origin())

    config_file = open("config.txt", "r+")
    config = config_file.readlines()

    for file in files:
        if any(file in line for line in config):
            continue

        else:
            file_destination = input(f'Where to move file "{file}": ')
            append_enrty_to_config(file, file_destination)

    config_file.close()


def append_enrty_to_config(file: str, path: str):
    entry = f"{file} -> {path}\n"
    with open("config.txt", "a") as f:
        f.write(entry)
