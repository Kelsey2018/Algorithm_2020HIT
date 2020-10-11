# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 20:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : max_map.py
import time
import numpy as np
import math

def max_map(A,B):
    n = len(A)
    f = np.zeros((n,2))
    sum = 0
    for i in range(0,n):
        f[i][0] = A[i]
        f[i][1] = B[i]
        sum += A[i]**B[i]

    return f,sum

if __name__ == '__main__':
    start = time.time()
    A = [9,1,3,5,7,6]
    B = [4,6,3,7,9,0]

    A = sorted(A,reverse=True)
    B = sorted(B,reverse=True)

    f,sum = max_map(A,B)
    print(f)
    print("最大代价为{}".format(sum))

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))