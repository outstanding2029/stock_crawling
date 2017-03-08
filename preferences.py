import sys
import os

GOOGLE_PASSWORD = ''

def load_from_command_line():
    global GOOGLE_PASSWORD
    for arg in sys.argv:
        if arg[:2] != '--':
            continue
        arg = arg[2:]
        name, value = arg.split('=')
        if name == 'pw':
            GOOGLE_PASSWORD = value

load_from_command_line()
