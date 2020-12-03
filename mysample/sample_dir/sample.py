import random


class Sample(object):

    def bubble(self, alist):
        for i in range(len(alist)-1):
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]
        return alist