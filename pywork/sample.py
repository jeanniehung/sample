def huiwen(str):
    '''
    判断是否是回文
    '''
    alist = list(str)
    blist = list(reversed(str))
    if alist == blist:
        print('Y')
    else:
        print('N')


huiwen('ssllss')
huiwen('jkllko')

print(191 % 10)
print(191 // 100)


def count_huiwen_number():
    '''
    计算1000以内的回文
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
        a = i % 10
        b = i // 100
        if a == b:
            count += 1
            alist.append(i)
    return [alist, count]


print(count_huiwen_number())


def long_huiwen_str(astr):
    '''
    最长回文
    '''
    size = len(astr)
    found = 0
    for sub_size in range(size, -1, -1):
        for offset in range(0, size-sub_size+1):
            sub_string = astr[offset:offset+sub_size]
            if sub_string[::-1] == sub_string:
                print(sub_string)
                found = 1
        if found == 1:
            break


long_huiwen_str('hkhkahjkkjh')


def counter(alist):
    dict = {}
    for a in alist:
        dict[a] = dict.get(a, 0)+1
    return dict


Alist = [1, 4, 1, 2, 3, 1, 2]
print(counter(Alist))


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
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


Alist = [12, 45, 2, 34, 90, 21]
print(bubble(Alist))


def bubble1(blist):
    '''
    [2, 3, 1, 4, 5]
    '''
    for i in range(len(blist)-1):
        isOrdered = True
        for j in range(len(blist)-i-1):
            if blist[j] > blist[j+1]:
                blist[j], blist[j+1] = blist[j+1], blist[j]
                isOrdered = False
        if isOrdered:
            break
    return blist


Blist = [12, 45, 2, 34, 90, 21]
print(bubble1(Blist))


def bubble2(alist):
    '''
    鸡尾酒排序
    [2, 3, 4, 5, 1]
    '''
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
    return alist


Clist = [12, 45, 2, 34, 90, 21]
print(bubble2(Clist))


def bubble3(alist):
    lastChangeIndex = 0
    unOrderBorder = len(alist)-1
    for i in range(len(alist)-1):
        isOrdered = True
        for j in range(unOrderBorder):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                isOrdered = False
                lastChangeIndex = j
        unOrderBorder = lastChangeIndex
        if isOrdered:
            break
    return alist


Dlist = [12, 3, 4, 78, 9, 45]
print(bubble3(Dlist))

