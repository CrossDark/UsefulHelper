"""
Helper
"""


class Start:
    def __init__(self, name):
        with open('./helper') as self.Project:
            self.Project.write('Name:' + name + '\n')
