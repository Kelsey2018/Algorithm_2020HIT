# -*- coding: utf-8 -*-
# @Author: Xiang xi
# @Date:   2020-05-04 16:52:35
import random
import copy
import random
import time
import pulp
import numpy as np
import matplotlib.pyplot as plt

def generateSet(setNum):
    # #生成F
    # # F = []
    # # for i in range(0,setNum):
    # #     scale_s = random.randint(1,setNum)
    # #     s = set()
    # #     for j in range(0,scale_s):
    # #         k = random.randint(1,setNum)
    # #         s.add(k)
    # #     F.append(s)
    #
    # # for item in F:
    # #     print(item)
    # # print("===========")
    #
    # #根据F求X
    # X = set()
    # for s in F:
    #     for k in s:
    #         X.add(k)
    # # print(X)

    # 生成s0:随机选 X 中的 20 个点放入其中
    X = set(i for i in range(1,setNum+1))
    s0 = set(random.sample(X,20))
    print(s0)
    unionS = []
    unionS.append(set(s0))
    element = set()
    element.update(s0)
    res = X - s0

    # 保证生成可行解
    while len(res) >= 20:
        n = random.randint(1, 20)
        x = random.randint(1, n)
        s_1 = set(random.sample(res,x))
        s_2 = set(random.sample(element, (n-x)))
        s_1.union(s_2)
        element.update(s_1)
        res = X - element
        # print(len(element))
        unionS.append(set(s_1))

    unionS.append(X - element)
    print("可行解的集合个数:",len(unionS))
    for j in range(setNum-len(unionS)):
        # n = random.randint(1, 20)
        n = random.randint(1, 20)
        s = set(random.sample(X, n))
        unionS.append(s)

    for item in unionS:
        print(item)
    return unionS,X


def find_mostCover_set(F,U):
    max_length = 0
    max_item = []
    for item in F:
        # print(len(set(item)))
        intersectionSet = list(set(item).intersection(set(U)))
        if max_length < len(intersectionSet):
            max_length = len(intersectionSet)
            max_item = item
    max_index = F.index(max_item)
    return max_index

def greedySetCover(setNum):
    # F,X = generateSet(setNum)
    F = [{1,2,3,4,5,6},{5,6,8,9},{1,4,7,10},{2,5,7,8,11},{3,6,9,12},{10,11}]
    X = {1,2,3,4,5,6,7,8,9,10,11,12}
    U = X
    C = []
    while len(U) > 0:
        max_index = find_mostCover_set(F,U)
        maxSet = F[max_index]
        U = U - maxSet
        C.append(maxSet)

    # union_set = {}
    # for item in C:
    #     union_set = set(union_set).union(item)
    # print(union_set)
    print_c(C)

def lpSetCover(setNum):
    F,X = generateSet(setNum)
    # 定义问题
    prob = pulp.LpProblem("minSet", pulp.LpMinimize)
    # 定义变量
    var = []
    for i in range(len(F)):  # n个变量，大于0
        name = "x" + str(i)
        var.append(pulp.LpVariable(name=name, lowBound=0))
    # 定义目标函数
    prob += pulp.lpSum(v for _, v in enumerate(var))
    # 定义约束条件
    for _, x in enumerate(X):  # n个约束条件
        xs = 0.0
        for i, S in enumerate(F):
            if x in S:
                xs += var[i]
        prob += xs >= 1.0

    # 求解
    status = prob.solve()

    # print(pulp.LpStatus[status])

    # 求X中元素的最大频率maxf
    f = [0] * len(X)
    for _, subF in enumerate(F):
        for i, subX in enumerate(X):  # X是1-n组成的
            if subX in subF:
                f[i] += 1
    maxf = max(f)

    C = []
    ans = set()
    i = 0
    for p in prob.variables():  # 获得解在F中的位置
        if p.varValue >= 1 / maxf:
            ans.add(i)
        i += 1
    # print("LP rounding:", ans)

    for i in ans:
        C.append(F[i])

    # union_set = {}
    # for item in C:
    #     union_set = set(union_set).union(item)
    # print(union_set)
    print_c(C)


def print_c(C):
    for item in C:
        print(item)
    print("最小集合覆盖个数为：", len(C))


if __name__ == '__main__':
    start = time.time()
    # generateSet(setNum=100)
    
    greedySetCover(setNum = 30)
    # lpSetCover(setNum = 500)

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))
