# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : least_zone.py
import time
import numpy as np

class zone():
    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        self.length = end - begin

def least(s,n):
    # 假设s中区间已按照ai排序
    same_a = []
    # sorted(s,key=lambda x:x.begin)
    # print(s)
    n = int(n)
    newbegin = 1
    N = 0
    while newbegin < n:
        newlist = [x for x in s if x.begin == newbegin]
        if len(newlist)==0:
            print("不能覆盖整个区间")
            return 0
        # print(newlist[0].length)
        max_len = 0
        for item in newlist:
            if max_len < item.length:
                max_len = item.length

        for item in newlist:
            if item.length == max_len:
                newbegin = item.end
                N += 1
    return N

if __name__ == '__main__':
    start = time.time()
    n = int(input("n:"))
    s = []
    for i in range(n):
        print("第{}个区间".format(i+1))
        print("1<=a<={}<=b<={}".format(i+1,n))
        a = int(input("a:"))
        b = int(input("b:"))
        z = zone(a,b)
        s.append(z)

    # print(s)
    print(least(s,n))

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))