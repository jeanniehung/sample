import random
from itertools import permutations
from collections import Counter


class Sample(object):

    def sample_random_gift(self):
        giftIn= [['a', 'A'], ['b', 'B'], ['c', 'C']]
        giftOut = []
        n = len(giftIn)
        gifts = [i[1] for i in giftIn]
        for x in range(n):
            flag = 0
            mygift = giftIn[x][1]
            person = giftIn[x][0]
            if mygift in gifts:
                flag = 1
                gifts.remove(mygift)
            getgift = random.choice(gifts)
            giftOut.append([person, getgift])
            gifts.remove(getgift)
            if flag:
                gifts.append(mygift)
        return giftOut

    def gift_sample(self):
        dictIn = {'a': 'A', 'b': 'B', 'c': 'C'}
        dictOut = {}
        person = list(dictIn.keys())
        for p in person:
            flag = 0
            if p in dictIn:
                flag = 1
                mygift = dictIn.pop(p)
            getgift = dictIn.popitem()
            dictOut[p] = getgift[1]
            if flag:
                dictIn[p] = mygift
        return dictOut

    def find(self, alist):
        a = 0
        for i in alist:
            a ^= i
        return a

    def single(self, n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [[1], [1, 1]]
        n = n - 2
        alist = [[1], [1, 1]]
        while n > 0:
            newlist = [1]
            for i in range(len(alist[-1])-1):
                newlist.append(alist[-1][i]+alist[-1][i+1])
            newlist.append(1)
            alist.append(newlist)
            n -= 1
        return alist

    def target(self, alist, tag):
        n = len(alist)
        for i in range(n-1):
            for j in range(i+1, n):
                if alist[i] + alist[j] == tag:
                    return [i, j]
        return [-1, -1]

    def dicttag(self, alist, tag):
        dict = {}
        for i in range(len(alist)):
            num = tag - alist[i]
            if num not in dict:
                dict[alist[i]] = i
            else:
                return [dict[num], i]

    def bubble(self, alist):
        for i in range(len(alist)):
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist

    def select(self, alist):
        for i in range(len(alist)):
            min = i
            for j in range(i+1, len(alist)):
                if alist[j] < alist[min]:
                    j, min = min, j
            if min != i:
                alist[min], alist[i] = alist[i], alist[min]
        return alist

    def insert(self, alist):
        for i in range(len(alist)):
            j = i
            while j > 0 and alist[j-1] > alist[j]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j -= 1
        return alist

    def palindrome(self, ss):
        a = list(ss)
        b = list(reversed(ss))
        if a == b:
            return True
        else:
            return False

    def palindrome_nums(self):
        count = 0
        alist = []
        for i in range(10):
            alist.append(i)
            count += 1
        for i in range(10, 100):
            if i % 11 == 0:
                alist.append(i)
                count += 1
        for i in range(100, 1000):
            a = i % 10
            b = i // 100
            if a == b:
                alist.append(i)
                count += 1
        return [alist, count]

    def palindrome_string(self, astring):
        size = len(astring)
        found = 0
        for sub_size in range(size, -1, -1):
            for offset in range(size-sub_size+1):
                sub_string = astring[offset: offset+sub_size]
                if sub_string[::-1] == sub_string:
                    print(sub_string)
                    found = 1
                    break
            if found:
                break

    def zuhe(self, ss):
        alist = permutations(list(ss))
        for item in sorted(alist):
            print(''.join(item))

    def quchong(self, ss):
        alist = list(set(ss))
        for item in alist:
            print(''.join(item), end='')
        print('')

    def count(self, string):
        cnt = Counter(string)
        return cnt

    def countDcit(self, ss):
        dict = {}
        alist = list(ss)
        for x in alist:
            dict[x] = dict.get(x, 0)+1
        return dict

    def is_prime(self, n):
        flag = 0
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break
        if flag:
            print('N')
        else:
            print('Y')

    def prime(self, n):
        alist = []
        count = 0
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                alist.append(i)
                count += 1
        return [alist, count]

    def change(self, ss):
        for i in ss:
            if i.isupper():
                print(''.join(i.lower()), end='')
            elif i.islower():
                print(''.join(i.upper()), end='')
            else:
                print(''.join(i), end='')
        print()
    '''
    ​ 冒泡排序可以通过增加boolean标识是否已经排好序来进行优化；
    还可以记录下最后一次交换元素的位置来进行优化，防止无意义的比较。
    冒泡排序是稳定排序，时间复杂度为O(n^2)，空间复杂度为O(1)。
    '''
    def bubble_optimization(self, alist):
        for i in range(len(alist)-1):
            isOrdered = True  # 假设一开始已经有序
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    isOrdered = False  # 发生一次交换说明一开始无序
            # 如果已经有序，直接跳出本次循环 i++
            if isOrdered:
                break
        return alist

    def bubble_optimization2(self, alist):
        for i in range(len(alist)-1):
            flag = False  # 表示是否发生交换
            for j in range(len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    flag = True  # 交换
            # flag=True 说明发生了一次交换，完成一轮排序后，交换排序的方向
            if flag:
                flag = False
                for j in range(len(alist)-i-2, 0, -1):  # 从后往前开始相邻元素比较大小
                    if alist[j] < alist[j-1]:
                        alist[j], alist[j-1] = alist[j-1], alist[j]
                        flag = True
            if not flag:
                break
        return alist

    def bubble_optimization3(self, alist):
        lastChangeIndex = 0
        unorderBorder = len(alist)-1  # 当前趟无序边界
        for i in range(len(alist)-1):
            isOrdered = True  # 假设开始时元素都是有序的
            for j in range(unorderBorder):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    isOrdered = False  # 如果出现有元素交换，则表明此趟没有完成排序
                    lastChangeIndex = j  # 记录下最后发生交换元素的位置
            unorderBorder = lastChangeIndex
            if isOrdered:
                break
        return alist










































