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
        self.state = None
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
                pre = doing[-1][0]
                doing[-1] = [pre] + [level, True]
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

    def split(self, data=None, leveled=0):
        if data is None:
            data = self.Describe
        self.state = None
        doing = []
        final = []
        son = False
        for i in data:
            level = i[1]
            print(doing)
            print(final)
            print('--------------------------')
            if i[2]:
                continue
            if level > leveled:
                doing.append([i[0:2] + [True]])
                leveled = level
            elif level < leveled:
                doing.append([i[0:2] + [False]])
                son = True
            elif level == leveled:
                doing.append([i[0:2] + [True]])
            else:
                raise TabError
            if son:
                final.append(self.split(doing, leveled + 1))
                doing = []
        return final

    def tree(self, data=None):
        if data is None:
            data = self.Describe
            print(data)
        pass
