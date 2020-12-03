import random
from itertools import permutations
from collections import Counter


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
                    isOrdered = False  # 如果出现有元素交换，则表明此躺可能没有完成排序
            if isOrdered:  # 如果当前趟都没有进行元素的交换，证明前面一趟比较已经排好序
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
        只要我们记录下当前趟最后一次交换的位置，在下一趟只比较到这个位置即可
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

    def select(self, alist):
        '''
        从未排序找到一个合适的数放到已排序序列后，保持有序列已经有序
        '''
        for i in range(len(alist)):
            minIndex = i
            for j in range(i+1, len(alist)):
                if alist[j] < alist[minIndex]:
                    j, minIndex = minIndex, j
            if i != minIndex:
                alist[minIndex], alist[i] = alist[i], alist[minIndex]
        return alist

    def insert(self, alist):
        '''
        插入
        从未排序选择一个数插入到已排序数列中，要求插入之后已排序列已经有序
        '''
        for i in range(len(alist)):
            j = i
            while j > 0 and alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
                j -= 1
        return alist

    def combination(self, astring):
        '''
        按照字符顺序排列组合
        '''
        alist = list(permutations(astring))
        for x in sorted(alist):
            print(''.join(x))

    def count(self, astring):
        '''
        计算每个字符出现的次数
        使用collections的Counter()方法
        '''
        cnt = Counter(astring)
        return cnt

    def count2(self, astring):
        '''
        计算字符揣出现次数
        '''
        dict = {}
        for x in astring:
            dict[x] = dict.get(x, 0) + 1
        return dict

    def duplicate_removal(self, astring):
        '''
        set()返回一个集合可迭代对象
        可以使用list()输出一个列表
        '''
        for x in set(astring):
            print(''.join(x), end='')
        print()

    def duplicate_removal2(self, astring):
        '''
        去重实现
        '''
        alist = []
        for x in astring:
            if x not in alist:
                alist.append(x)
        return alist

    def is_prime_number(self, num):
        '''
        判断一个数是不是质数
        '''
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            print('Y')

    def print_prime_numbers(self, num):
        '''
        打印质数并计算num以内质数的个数
        '''
        count = 0
        alist = []
        for i in range(1, num):
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                count += 1
                alist.append(i)
        return [alist, count]

    def palindrome(self, astring):
        '''
        判断是不是回文
        '''
        alist = list(astring)
        blist = list(reversed(astring))
        if alist == blist:
            print('Y')
        else:
            print('N')

    def palindrome2(self, astring):
        '''
        使用切片list[::-1]
        '''
        alist = list(astring)
        if alist == alist[::-1]:
            print('Y')
        else:
            print('N')

    def print_palindrome_num(self):
        '''
        输出1000以内的回文数字
        '''
        count = 0
        alist = []
        for i in range(10):
            count += 1
            alist.append(i)
        for i in range(10, 100):
            if i % 11 == 0:
                count += 1
                alist.append(i)
        for i in range(100, 1000):
            hundred = i % 10
            single = i // 100
            if hundred == single:
                count += 1
                alist.append(i)
        return [alist, count]

    def find_longest_palindrome_num(self, astring):
        '''
        找出最长的回文
        '''
        size = len(astring)
        found = 0
        for sub_size in range(size, -1, -1):
            for offset in range(size-sub_size+1):
                sub_string = astring[offset:offset+sub_size]
                if sub_string == sub_string[::-1]:
                    found = 1
                    print(sub_string)
            if found == 1:
                break

    def change(self, astring):
        for x in astring:
            if x.isupper():
                print(''.join(x.lower()), end='')
            elif x.islower():
                print(''.join(x.upper()), end='')
            else:
                print(''.join(x), end='')
        print()

    def random_distribution_gift(self):
        '''
        随机分配
        '''
        giftIn = [['joy', 'apple'], ['jane', 'banana'], ['sim', 'pear'], ['coco', 'orin']]
        giftOut = []
        flag = 0
        gifts = [i[1] for i in giftIn]
        for i in range(len(giftIn)):
            person = giftIn[i][0]
            mygift = giftIn[i][1]
            if mygift in gifts:
                flag = 1
                gifts.remove(mygift)
            getGift = random.choice(gifts)
            giftOut.append([person, getGift])
            gifts.remove(getGift)
            if flag:
                gifts.append(mygift)
        return giftOut

    def distribution_gifts(self):
        giftInDict = {'joy': 'apple', 'sim': 'pear', 'jane': 'banana', 'coco': 'orin'}
        giftOutDict = {}
        persons = giftInDict.keys()
        # for person in persons:





































