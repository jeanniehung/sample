def counter(alist):
    dict = {}
    for a in alist:
        dict[a] = dict.get(a, 0)+1
    return dict

Alist = [1, 4, 1, 2, 3, 1, 2]
print(counter(Alist))


from collections import Counter
def count(ss):
    cnt = Counter(ss)
    return cnt

print(count('Aliistuii'))


def count1(alist):
    dict = {}
    for a in alist:
        dict[a] = dict.get(a, 0)+1
    return dict

print(count1(Alist))


from collections import Counter

def count2(alist):
    cnt = Counter(alist)
    return cnt

print(count2(Alist))


import random
def distribution():
    listIn = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']]
    listOut = []
    gifts = [i[1] for i in listIn]
    n = len(listIn)
    for x in range(n):
        flag = 0
        name = listIn[x][0]
        mygift = listIn[x][1]
        if mygift in gifts:
            flag = 1
            gifts.remove(mygift)
        getgift = random.choice(gifts)
        listOut.append([name, getgift])
        gifts.remove(getgift)
        if flag:
            gifts.append(mygift)
    return listOut

print(distribution())


def change():
    dictIn = {'a':'A', 'b':'B', 'c':'C', 'd':'D'}
    dictOut = {}
    persons = list(dictIn.keys())
    for p in persons:
        flag = 0
        if p in dictIn:
            flag = 1
            myGift = dictIn.pop(p)
        getOut = dictIn.popitem()
        dictOut[p] = getOut[1]
        if flag:
            dictIn[p] = myGift
    return dictOut

print(change())

def bubble(alist):
    count = 0
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        count += 1
    return [alist, count]


def bubble_optimization(alist):
    count = 0
    for i in range(len(alist)-1):
        isOrdered = True
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                isOrdered = False
        if isOrdered:
            break
        else:
            count += 1
    return [alist, count]


def bubble_optimization2(alist):
    count = 0
    for i in range(len(alist)-1):
        isOrdered = True
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                isOrdered = False
        if not isOrdered:
            for j in range(len(alist)-i-2, 0, -1):
                if alist[j] < alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]
                    isOrdered = True
        if isOrdered:
            break
        else:
            count += 1
    return [alist, count]

def bubble_optimization3(alist):
    lastChangeIndex = 0  # 最后一次交换元素的位置
    unorderedBorder = len(alist)-1  # 当前趟未排序位置
    for i in range(len(alist)-1):
        isOrdered = True
        for j in range(unorderedBorder-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                isOrdered = False  # 发生一个元素交换说明此趟排序未完成
                lastChangeIndex = j  # 记录最后一次交换元素的位置
        unorderedBorder = lastChangeIndex
        if isOrdered:
            break
        return alist



print(bubble([12, 3, 4, 78, 9, 45]))
print(bubble_optimization([12, 3, 4, 78, 9, 45]))
print(bubble_optimization2([12, 3, 4, 78, 9, 45]))
print(bubble_optimization3([12, 3, 4, 78, 9, 45]))