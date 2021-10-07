from os import path
from typing import List
from collections import defaultdict


class Configurator:
    file_to_path: defaultdict = defaultdict(lambda: "")

    def configurate(self):
        with open("config.txt", "r") as f:
            config: List[str] = f.readlines()

        for entry in config:
            file_and_path = entry.strip().split(" -> ")

            try:
                file = file_and_path[0]
                path = f"{file_and_path[1]}\\"
            except IndexError:
                path = ""

            self.file_to_path[file] = path
