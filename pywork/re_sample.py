def maopao(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j+1], alist[j] = alist[j], alist[j+1]
    return alist


def insert(alist):
    for i in range(len(alist)):
        j = i
        while j>0 and alist[j] < alist[j-1]:
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1
    return alist

def select(alist):
    for i in range(len(alist)):
        min = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min]:
                j, min = min, j
        if min != i:
            alist[min], alist[i] = alist[i], alist[min]
    return alist

Alist = [78, 9, 56, 23, 2, 3]
print(maopao(Alist))


from itertools import permutations\

def zuhe(ss):
    if ss:
        alist = list(permutations(ss))
        for item in sorted(alist):
            print(''.join(item))

zuhe("ASB")


def count_nums(alist):
    dict = {}
    for a in alist:
        dict[a] = dict.get(a, 0)+1
    return dict

Alist = [2, 1, 22, 1, 4, 2, 5]
# print(count_nums(Alist))


from collections import Counter
def counter(ss):
    cnt = Counter(ss)
    return cnt

print(counter(Alist))


def zhishu(n):
    alist = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j ==0:
                break
        else:
            alist.append(i)
    return alist
print(zhishu(100))



def assert_zhishu(num):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print('Y')
assert_zhishu(97)


def change(ss):
    if ss:
        for i in ss:
            if i.islower():
                print(''.join(i.upper()), end='')
            elif i.isupper():
                print(''.join(i.lower()), end='')
            else:
                print(''.join(i), end='')
    print('\n')

ss = "AnnnjkhbhhJKlhj"
change(ss)

def quchong(ss):
    if ss:
        alist=sorted(set(ss))
        for i in alist:
            print(''.join(i), end='')

quchong(ss)


