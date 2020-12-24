from collections import Counter


def count(astring):
    cnt = Counter(astring)
    return cnt


print(count('ahaaaavsd'))


def count2(astring):
    dict = {}
    for i in astring:
        dict[i] = dict.get(i, 0) + 1
    return dict


print(count2('najlvjljli'))





















