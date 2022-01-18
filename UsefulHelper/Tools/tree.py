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

    def split(self):
        self.state = None
        doing = []
        final = []
        for i in self.Describe:
            state = i[2]
            if state:
                doing = [i]
                final.append(doing)
                self.state = True
            elif self.state:
                if state:
                    doing.append(self.split())
                else:
                    doing.append(i)
        return final

    def tree(self, data=None):
        if data is None:
            data = self.Describe
            print(data)
        pass
