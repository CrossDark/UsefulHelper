"""
The temple of manage
"""
from UsefulHelper.Tools import Setup

manage_list = ['setup', 'pack']


def setup(get):
    task = Setup(path=get)
    task.setup()
    return 'Down'


def pack(get):
    task = Setup(path=get)
    task.pack()
    return 'Down'
