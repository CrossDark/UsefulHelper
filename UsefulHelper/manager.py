"""
The temple of manage
"""
import os

import click

from UsefulHelper.Tools import Setup

key_list = ['stop']
manage_list = ['setup', 'pack', 'clean']


@click.command()
@click.option(
    '--get', prompt='manage>>'
)
def main(get):
    split = get.split(' ')
    first = split[0]
    if first in manage_list:
        info = eval(first)(split[1:])
        print(info)
        get = None
        main(get)
    elif first in key_list:
        eval(first)
    else:
        print(get + " isn't support")
        get = None
        main(get)


def setup(get):
    task = Setup(path=get)
    task.setup()
    return 'Down'


def pack(get):
    task = Setup(path=get)
    task.pack()
    return 'Down'


def clean(get):
    if not get:
        for i in os.listdir('./'):
            os.remove(i)
    else:
        for i in get:
            os.remove(i)


def stop():
    exit()
