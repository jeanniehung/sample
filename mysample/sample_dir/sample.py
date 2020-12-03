import random


class Sample(object):

    def bubble(self, alist):
        for i in range(len(alist)-1):
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist

    def bubble_optimize1(self, alist):
        '''
        排序，设置一个标志
        '''
        for i in range(len(alist)-1):
            isOrdered = True  # 设置一个标志，假设数组是有序的
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    isOrdered = False  # 发生元素位置交换，说明该趟排序未完成
            if isOrdered:  # 排序已经完成
                break
        return alist

    def bubble_optimize2(self, alist):
        '''
        鸡尾酒排序
        '''
        for i in range(len(alist)-1):
            isOrdered = True
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    isOrdered = False  # 发生元素位置交换，说明该趟排序未完成
            if not isOrdered:
                for j in range(len(alist)-i-2, 0, -1):
                    if alist[j] < alist[j-1]:
                        alist[j], alist[j-1] = alist[j-1], alist[j]
                        isOrdered = False
            if isOrdered:
                break
        return alist

    def bubble_optimize3(self, alist):
        '''
        找到已排序和未排序的分割点
        '''
        lastExchangeIndex = 0
        unorderBorder = len(alist)-1
        for i in range(len(alist)-1):
            isOrdered = True
            for j in range(unorderBorder):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    isOrdered = False  # 发生元素位置交换，说明该趟排序未完成
                    lastExchangeIndex = j
            unorderBorder = lastExchangeIndex
            if isOrdered:
                break
        return alist
































