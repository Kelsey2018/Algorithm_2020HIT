# -*- coding: utf-8 -*-
# @Author: Xiang xi
# @Date:   2020-05-05 10:32:35
import random
import copy
import random
import time
import math


def quickSort(A,p,r):
    if p < r:
        q = rand_partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    return A

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A[i],A[j]

def rand_partition(A,p,r):

    # key = A[p]  #基准元素
    # while p < r:
    #     while p<r and A[r]>=key:
    #         r = r - 1
    #     A[p] = A[r]
    #     while p<r and A[p]<=key:
    #         p = p +1
    #     A[r] = A[p]
    # A[p] = key
    # return p
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]
    key = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= key:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def generateA(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(1,100))
    return random_list

def generateNewA(length,i):
    dup_num = int(length * 10 * i * 0.01)  #第i个数据集重复元素的个数
    random_dup_list = []
    if dup_num > 0:
        dup_number = random.randint(1,math.pow(10,6))
        print("重复元素为：",dup_number)
        print("重复次数：",dup_num)
        for i in range(dup_num):
            random_dup_list.append(dup_number)
        while len(random_dup_list) <= length:
            random_dup_list.append(random.randint(1, math.pow(10,6)))
        # random.shuffle(random_dup_list[1:])
        print(random_dup_list)
        return random_dup_list
    else:
        while len(random_dup_list) <= length:
            random_dup_list.append(random.randint(1, math.pow(10,6)))
        return random_dup_list


def three_partition(A,p,r):
    if (p >= r):
        return
    pivot = A[p]
    gt = r
    lt = p
    i = p + 1

    while i <= gt:
        if A[i] > pivot:
            A[i],A[gt] = swap(A,i,gt)
            gt = gt - 1
        elif A[i] < pivot:
            # A[i], A[lt] = A[lt], A[i]
            A[i], A[lt] = swap(A,i,lt)
            lt = lt + 1
            i = i + 1
        else:
            i = i + 1
    three_partition(A,p,lt-1)
    three_partition(A,gt+1,r)
    return A

if __name__ == '__main__':

    start = time.time()
    #=================单个数据集===================
    # A = generateA(length = 20)
    # print("排序前：",A)
    # p = 0
    # r = len(A) - 1
    # print("排序后：",quickSort(A,p,r))
    # =================单个数据集===================

    # =================11个数据集===================
    length = math.pow(10,6)
    # length = 5000
    for i in range(7,11):
        start = time.time()
        A = generateNewA(length,i)
        # print("第{}个数据集------排序前：".format(i), A)
        p = 0
        r = len(A) - 1
        print("第{}个数据集------排序后：".format(i), three_partition(A,p,r))
        end = time.time()
        print("Running Time(ms):{:.4f}".format((end - start) * 1000))
    # =================11个数据集===================

    # end = time.time()
    # print("Running Time(ms):{:.4f}".format((end - start) * 1000))


