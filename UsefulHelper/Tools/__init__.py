"""
Some helpful tools
"""
import os
import re


class Setup:
    def __init__(self, path: list):
        self.path = path[0]

    def setup(self):
        if os.path.exists(self.path + '/setup.py'):
            pass
        else:
            with open(self.path + '/setup.py', 'w') as setup:
                setup.write("""
from setuptools import setup, find_packages


setup(
    name='<NAME>',
    version='<VERSION>',
    author='<YOUR NAME>',
    author_email='<EMAIL>',
    packages=find_packages(),
    zip_safe='<BOOL>',
    platforms=['<OS>'],
    install_requires=['<REQUIRES>'],
    python_requires='>=<PYTHON VISION>',
    description='<DESCRIPTION>',
    long_description='<LONG DESCRIPTION>',
    license='<LICENSE>',
    url='<URL>',
    classifiers=[],
    scripts=['<SCRIPTS>']
)
            """)

    def pack(self):
        if os.path.isfile(os.path.abspath(self.path)):
            os.system('python' + self.path)
        else:
            with open(self.path + 'pack.py', 'w') as pack:
                pack.write("""
import os
import re

from UNKnownDB.DB import LocalDB

with open('./setup.py', 'r+') as setup:
    setup.seek(0, 0)
    read = setup.read()
    find = re.findall('version=(.+?),', read)
    v_id = float(eval(find[0].replace('.', '')))
    setup.seek(0, 0)
    num = str(v_id + 1)
    writing = read.replace(find[0], "'" + num[0] + '.' + num[1] + '.' + num[2] + "'")
    setup.write(writing[:-1])
os.system('python3 setup.py sdist bdist_wheel')
os.system('twine upload dist/*')
db = LocalDB('')
db.delete_all('./dist')

                """)


class Node:
    # 初始化一个节点
    def __init__(self, name=None, val=None):
        self.name = name  # 节点值
        self.val = val
        self.l_child = []  # 子节点列表

    # 添加子节点
    def add_child(self, node):
        self.l_child.append(node)


class Build:
    def __init__(self):
        super(Build, self).__init__()
        with open('./Describe/grammar.usg') as describe:
            self.Describe = describe.readlines()
        for i in self.Describe:
            if re.findall('~(.+?)~', i):
                continue
            split = re.findall('(.+?):(.+?)', i)
            print(split)
            try:
                level = re.search('[^ ]', i).span()[0]//4
            except TypeError:
                level = 0
            except AttributeError:
                level = 0
            try:
                exec('self.Level' + str(level) + '["' + split[0][0] + '"] = "' + split[0][1] + '"')
            except AttributeError:
                exec("self.Level" + str(level) + " = {}")
                exec('self.Level' + str(level) + '["' + split[0][0] + '"] = "' + split[0][1] + '"')
