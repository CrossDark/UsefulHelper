#!/usr/bin/python3.9 cli.py
import click
from UNKnownDB.DB import LightDB

key_list = ['start']


def start(get):
    with open('./manage.py', 'w') as manage:
        manage.write("""
from UsefulHelper.manager import *


if __name__ == '__main__':
    print('Debugging')
    main()
else:
    main()
        """)
    with LightDB.Data(path='./info', name=get) as db:
        print(db)
    return 'Done'


def stop():
    exit()


@click.command()
@click.option(
    "--things", prompt="UsefulHelper>>",
    help="NONE."
)
def main(things):
    split = things.split(' ')
    first = split[0]
    if first in key_list:
        info = eval(first)(split[1])
        print(info)
        things = None
        main(things)
    elif first == 'stop':
        stop()
    else:
        print(things + " isn't support")
        things = None
        main(things)


if __name__ == '__main__':
    print('Debugging')
    main()
else:
    main()
