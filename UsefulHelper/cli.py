#!/usr/bin/python3.9 cli.py
import click
# from UsefulHelper import Start

key_list = ['start', 'setup', 'pack', 'build']


def start(get):
    with open('./manage.py', 'w') as manage:
        manage.write("""
from UsefulHelper.manager import *
import click

manage_list = ['setup']


@click.command()
@click.option(
    '--get', prompt='manage>>'
)
def main(get):
    split = get.split(' ')
    first = split[0]
    if first in manage_list:
        info = eval(first)(split.remove(first))
        print(info)
    else:
        print(get + " isn't support")
        get = None
        main(get)


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
    else:
        print(things + " isn't support")
        things = None
        main(things)


if __name__ != '__main__':
    main()
