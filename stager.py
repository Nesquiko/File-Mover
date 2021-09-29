import sys
from command_table import command_table


def main():

    commands = sys.argv

    for i in range(1, len(commands)):
        command = commands[i]

        if "--" not in command:
            continue

        if command in command_table:
            command_table[command]()

        else:
            print(
                f'Unknown command "{command}", use --help to get more information about each command.'
            )


if __name__ == "__main__":
    main()
