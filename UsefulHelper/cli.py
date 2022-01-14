#!/usr/bin/python3.9 cli.py
import click
# from UsefulHelper import Start

key_list = ['start', 'setup', 'pack', 'build']


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
    return get


@click.command()
@click.option(
    "--things", prompt="UsefulHelper>>",
    help="NONE."
)
def main(things):
    split = things.split(' ')
    first = split[0]
    if first in key_list:
        info = eval(first)(split.remove(first))
        print(info)
        things = None
        main(things)
    else:
        print(things + " isn't support")
        things = None
        main(things)


if __name__ == '__main__':
    print('Debugging')
    main()
else:
    main()
