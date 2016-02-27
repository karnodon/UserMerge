# coding=UTF-8

import os
from os.path import isfile
import re

__author__ = 'Frostbite'


class Merger:
    users = {}
    errors = {}

    def merge(self):
        pattern = re.compile('\d{2}\.txt')
        files = [f for f in os.listdir('.') if isfile(f) and pattern.match(f)]
        for f in files:
            [self.store_error(f, l) for l in open(f).readlines() if not self.parse_line(l)]
        self.write()
        self.write_errors()

    def store_error(self, file, line):
        if not file in self.errors:
            self.errors[file] = []
        self.errors[file].append(line)

    def write_errors(self):
        e = open('errors.txt', mode='w')
        for f in self.errors:
            e.write(f + '\n')
            [e.write(l) for l in self.errors[f]]
            e.write('*******************************')
        e.close()

    def parse_line(self, l):
        try:
            d = l.split('=')
            if not d[0] in self.users:
                self.users[d[0]] = []
            self.users[d[0]].append(d[1].strip())
            return True
        except:
            return False

    def convert_roles(self, roles, prefix):
        res = ''
        for r in roles:
            res += r[len(prefix):] + ','
        res = res[:-1]
        return res

    def write(self):
        r = open('roles.txt', mode='w')
        for u in self.users:
            r.write(u + '=' + self.convert_roles(self.users[u], 'beznal_')+'\n')
        r.close()


def main():
    m = Merger()
    m.merge()

main()
