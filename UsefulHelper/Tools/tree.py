"""
Grammar Tree
"""
# import os
import re


class Node:
    def __init__(self, name='~'):
        super(Node, self).__init__()
        self.Name = name
        self.Tree = {}

    def add(self, name, things):
        self.Tree[name] = things

    def __repr__(self):
        return {self.Name: self.Tree}

    def __str__(self):
        return str({self.Name: self.Tree})


class Tree:
    def __init__(self):
        super(Tree, self).__init__()
        self.Dict = {}
        self.state = None
        self.Leval = 0
        self.Describe = []
        doing = []
        final = []
        with open('./try/Describe/grammar.usg') as describe:
            describe_line = describe.readlines()
        for i in describe_line:
            level = re.search('[^ ]', i).span()[0] // 4
            print(level)
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
        self.Describe = final

    def dict(self):
        for i in self.Describe:
            split = i[0].split(':')
            self.Dict[split[0]] = i[1:3]

    def tree(self, leveled=0, father=Node('~'), data=None):
        doing = {}
        final = {}
        son = False
        if data is None:
            data = self.Dict
        for k, v in data.items():
            if leveled == v[0]:
                print(v)
                if v[1]:
                    final[k] = None
                    doing = {}
                else:
                    final[k] = v
        return final
