# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : least_element.py
import time
import numpy as np

def least(s,w):
    sub_s = []
    s = np.sort(s)[::-1]
    if s[0] >= w:
        sub_s.append(s[0])
        return sub_s

    sub_s.append(s[0])
    w = w - s[0]

    for i in range(1,len(s)):
        if s[i] >= w:
            sub_s.append(s[i])
            return sub_s
        else:
            sub_s.append(s[i])


if __name__ == '__main__':
    start = time.time()

    s = [1,3,7,5,2,1,9,13]
    w = 14
    print(least(s,w))

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))