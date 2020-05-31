# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : greedy_DNA.py
import time
import numpy as np

class dna():
    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        self.length = end - begin

def max_dna(s,n,end):
    N = 1
    sub_s = []
    sub_s.append(0)
    newbegin = s[0].end
    for i in range(1, n):
        # while newbegin < end:
        if s[i].begin >= newbegin:
            sub_s.append(i)
            newbegin = s[i].end
            N += 1

    return N


if __name__ == '__main__':
    start = time.time()

    n = int(input("n:"))
    s = []
    end = 6
    for i in range(n):
        print("第{}长度相同的个区间".format(i + 1))
        print("p{}<q{}".format(i + 1, i+1))
        p = int(input("p:"))
        q = int(input("q:"))
        z = dna(p, q)
        s.append(z)

    # print(s)
    print(max_dna(s,n,end))

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))