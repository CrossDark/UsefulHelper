"""
Grammar Tree
"""
# import os
import re


tree = {}


class Node:
    def __init__(self, name):
        super(Node, self).__init__()
        global tree
        exec('tree[' + name + ']')


class Build:
    def __init__(self):
        super(Build, self).__init__()
        self.Leval = 0
        self.Describe = []
        doing = []
        final = []
        with open('./try/Describe/grammar.usg') as describe:
            describe_line = describe.readlines()
        for i in describe_line:
            level = re.search('[^ ]', i).span()[0] // 4
            if re.findall('~(.+?)~', i):
                continue
            elif level > self.Leval:
                pre = doing[-1][0:2]
                doing[-1] = pre + [True]
                doing.append([i.replace('\n', '').replace(' ', ''), level, False])
                self.Leval = level
            elif level < self.Leval:
                doing.append([i.replace('\n', '').replace(' ', ''), level, False])
                final += doing
                doing = []
                self.Leval = 0
            elif level == self.Leval:
                doing.append([i.replace('\n', '').replace(' ', ''), level, False])
            else:
                raise TabError
            print(self.Leval)
        self.Describe = final

    def build(self, father='~', data=None):
        doing = []
        final = {}
        if data is None:
            data = self.Describe
        """Iter"""
        for datum in data:
            if datum[2]:
                break
            else:
                raise TabError
