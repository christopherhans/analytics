import os


def print_debug(msg):
    if os.environ['DEBUG'] == '1':
        print(msg)
