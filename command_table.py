from consts import *
from origin import set_origin, print_origin
from destination import set_destination, print_destination
from mover import move

command_table = {
    SET_ORIGIN_COMMAND: set_origin,
    SET_DEST_COMMAND: set_destination,
    READ_ORIGIN_COMMAND: print_origin,
    READ_DEST_COMMAND: print_destination,
    MOVE_COMMAND: move,
}
