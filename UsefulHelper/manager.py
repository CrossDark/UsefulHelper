"""
The temple of manage
"""
import os

import click

from UsefulHelper.Tools import Setup, TreeBuild

key_list = ['prepare']
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
        eval(first)()
        get = None
        main(get)
    elif first == 'stop':
        exit(0)
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


def prepare():
    # Describe
    make_dir('./Describe')
    open('./Describe/grammar.usg', 'w').close()
    # Build
    make_dir('Build')
    print('Down')


def make_dir(name):
    os.mkdir(name)
    open('./' + name + '/__init__.py', 'w').close()


def build():
    """
    build
    """
    build_ = TreeBuild()
    print(0)
    print(build_.Level0)
    print(build_.Level1)
    print(build_.Level2)
