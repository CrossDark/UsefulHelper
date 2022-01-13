#!/usr/bin/python3.9
import click
from UsefulHelper import Start

key_list = ['start']


@click.command()
@click.option(
    "--key", prompt="Method",
    help="NONE."
)
@click.option(
    '--value', prompt='Properties',
    help='__'
)
def begin(key, value):
    print(key, value)
    try:
        key(value)
    except TypeError:
        print(0)
    else:
        print(1)


def start(name, path):
    try:
        Start(name, path)
    except IsADirectoryError:
        pass


if __name__ != '__main__':
    begin()
else:
    print('Error')
