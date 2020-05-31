# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : min_SumAbs.py
import time
import numpy as np

def min_SumAbs(A,B):
    sum_abs = 0
    n = len(A)
    for i in range(n):
        sum_abs += abs(A[i] - B[i])

    return sum_abs/n

if __name__ == '__main__':
    start = time.time()
    A = [9.1,3,5,7,6]
    B = [4,6,3,7,9,0]

    A = sorted(A,reverse=True)
    B = sorted(B,reverse=True)

    print(min_SumAbs(A,B))

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))