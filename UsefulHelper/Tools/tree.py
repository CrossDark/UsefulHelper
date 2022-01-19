"""
Grammar Tree
"""
# import os
import re


class Build:
    def __init__(self):
        super(Build, self).__init__()
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
                doing[-1] = [pre] + [level]
                doing.append([i.replace('\n', '').replace(' ', ''), level])
                self.Leval = level
            elif level < self.Leval:
                doing.append([i.replace('\n', '').replace(' ', ''), level])
                final += doing
                doing = []
                self.Leval = 0
            elif level == self.Leval:
                doing.append([i.replace('\n', '').replace(' ', ''), level])
            else:
                raise TabError
        self.Describe = final

    def split(self, data=None):
        if data is None:
            data = self.Describe
        self.state = None
        self.Leval = 0
        self.Describe = []
        doing = []
        final = []
        for i in data:
            level = i[1]
            print(doing)
            if level > self.Leval:
                # pre = doing[-1][0]
                # doing[-1] = [pre] + [level]
                doing.append([i[0], level - 1])
                self.Leval = level
            elif level < self.Leval:
                doing.append([i[0], level - 1])
                final.append(doing)
                doing = []
                self.Leval = 0
            elif level == self.Leval:
                doing.append([i[0], level - 1])
            else:
                raise TabError
        return final

    def tree(self, data=None):
        if data is None:
            data = self.Describe
            print(data)
        pass
