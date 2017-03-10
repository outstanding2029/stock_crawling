import sys
import os

GOOGLE_PASSWORD = ''
RUN_TYPE = ''

def load_from_command_line():
    global GOOGLE_PASSWORD
    global RUN_TYPE
    for arg in sys.argv:
        if arg[:2] != '--':
            continue
        arg = arg[2:]
        name, value = arg.split('=')
        if name == 'pw':
            GOOGLE_PASSWORD = value
        elif name == 'run':
            RUN_TYPE = value

load_from_command_line()
