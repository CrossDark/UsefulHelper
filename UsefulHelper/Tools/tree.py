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
        with open('./try/Describe/grammar.usg') as describe:
            self.Describe = describe.readlines()

    def split(self, data):
        self.Leval = 0
        leval = 0
        final = []
        doing = []
        son = False
        for datum in data:
            if re.findall('~(.+?)~', datum):
                continue
            split = re.findall('(.+?):(.+?)', datum)
            print(split)
            doing.append(split[0][0] + ':' + split[0][1])
            if re.search('[^ ]', datum).span()[0]//4 < leval:
                break
            elif re.search('[^ ]', datum).span()[0]//4 > leval:
                son = True
            leval = re.search('[^ ]', datum).span()[0]//4
        if son:
            final.append(self.split(final))
        return final

    def add(self, data):
        pass
