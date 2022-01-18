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
        with open('./try/Describe/grammar.usg') as describe:
            describe_line = describe.readlines()
        for i in describe_line:
            level = re.search('[^ ]', i).span()[0] // 4
            if re.findall('~(.+?)~', i):
                continue
            self.Describe.append([i.replace('\n', '').replace(' ', ''), level])

    def build(self, data=None, level=0):
        doing = []
        final = {}
        son = False
        if data is None:
            data = self.Describe
        """Iter"""
        for datum in data:
            if datum[1] < level:
                break
            elif datum[1] > level:
                son = True
                doing.append([datum[0], datum[1] - 1])
            elif datum[1] // 4 == level:
                final[datum[0]] = doing
            else:
                raise TabError
        if son:
            final[''] = self.build(doing)
        return final
