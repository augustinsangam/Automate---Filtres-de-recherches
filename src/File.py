# coding=utf-8

from Objectt import Objectt


class File(object):

    def __init__(self):
        self.myList = list()

    def lireFichier(self, filename):
        with open(filename) as file:
            content = file.readlines()
            content = content.strip()
            for line in content:
                line = content[0]
                content = content.split()
                self.myList.append(Objectt(line[2], line[1], line[0]))


