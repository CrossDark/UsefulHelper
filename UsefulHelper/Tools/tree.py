"""
Grammar Tree
"""
# import os
import re


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
        self.Describe = final

    def tree(self, data=None):
        if data is None:
            data = self.Describe
        doing = []
        final = []
        child = False
        for datum in data:
            if datum[2]:
                final.append(doing)
                child = True
                doing = []
            elif not datum[2]:
                doing.append(datum)
            elif child:
                final.append(self.tree(doing))
            else:
                final.append(datum)
        return final

    def build(self, father=None, data=None):
        if father is None:
            father = self.Describe[0]
        doing = []
        final = {}
        child = False
        for datum in self.Describe:
            if datum[2]:
                child = True
            elif child:
                doing.append(datum[0])
            elif not datum[2]:
                final[''] = doing
                doing = []
            else:
                raise TabError
        return final
