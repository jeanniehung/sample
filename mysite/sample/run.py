from sample import Sample
import json
from sample_requests import Request
# from sample_mysql import PyMysql
# from data.dir_data import Mysql

if __name__ == '__main__':
    sample = Sample()
    req = Request()
    # mysql = PyMysql()
    print(sample.sample_random_gift())
    print(sample.gift_sample())
    print(sample.find([1, 2, 1, 1, 2]))
    print(sample.single(6))
    print(sample.target([1, 2, 3, 9], 10))
    print(sample.dicttag([1, 2, 3, 9], 5))
    print(sample.bubble([23, 2, 12, 56, 3]))
    print(sample.select([10, 8, 9, 78, 23]))
    print(sample.insert([78, 89, 34, 5, 2]))
    print(sample.palindrome('xuioiux'))
    print(sample.palindrome_nums())
    sample.palindrome_string('hgihoopppoonnkhk')
    sample.zuhe('ACB')
    sample.quchong('hhahjkhaa')
    print(sample.count('hkalpoqncaaaa'))
    print(sample.countDcit('akhkaavx'))
    sample.is_prime(12)
    print(sample.prime(100))
    sample.change('jkHKAKHKAjlsdkl')
    alist = [12, 34, 1, 3, 90]
    b = alist.sort()
    print(b)
    print(alist)
    print(alist.sort())
    blist = [12, 34, 1, 3, 90, 4, 89]
    c = sorted(blist)
    print(c)
    print(blist)
    print('bubble_optimization-->', sample.bubble_optimization(blist))
    blist = [12, 34, 1, 3, 90, 4, 89]
    print('bubble_optimization3-->', sample.bubble_optimization3(blist))
    payload = {'some': 'data'}

    print(req.get_api())

    # print(mysql.connect())
    # print('mysql-->', mysql.option(Mysql.sql))















