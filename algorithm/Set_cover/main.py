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
    # 生成s0:随机选 X 中的 20 个点放入其中
    X = [i for i in range(1,setNum+1)]
    s0 = random.sample(X,20)

    unionS = []
    unionS.append(s0)
    element = s0

    # 保证生成可行解
    while len(list(set(X) - set(element))) >= 20:
        n = random.randint(1, 20)
        x = random.randint(1, n)
        X_s = [ i for i in X if i not in element ]
        s_1 = random.sample(X_s,x)
        ret = [i for i in element]
        s_2 = random.sample(ret, (n-x))
        s_1.extend(s_2)
        element = set(element).union(s_1)
        # print(len(element))
        unionS.append(s_1)

    unionS.append(list(set(X) - set(element)))
    print("可行解的集合个数:",len(unionS))
    for j in range(setNum-len(unionS)):
        # n = random.randint(1, 20)
        n = random.randint(1, setNum)
        s = random.sample(X, n)
        unionS.append(s)

    # for item in unionS:
    #     print(item)
    return unionS


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
    X = [i for i in range(1, setNum + 1)]
    U = X
    F = generateSet(setNum)
    C = []
    while len(U) > 0:
        max_index = find_mostCover_set(F,U)
        maxSet = F[max_index]
        resU = list(set(U).difference(set(maxSet)))
        U = resU
        C.append(maxSet)

    # union_set = {}
    # for item in C:
    #     union_set = set(union_set).union(item)
    # print(union_set)
    print_c(C)

def lpSetCover(setNum):
    X = [i for i in range(1, setNum + 1)]
    F = generateSet(setNum)
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

    union_set = {}
    for item in C:
        union_set = set(union_set).union(item)
    print(union_set)
    # print_c(C)


def print_c(C):
    for item in C:
        print(item)
    print("最小集合覆盖个数为：", len(C))


if __name__ == '__main__':
    start = time.time()
    # generateSet(setNum=100)
    # greedySetCover(setNum = 50)
    lpSetCover(setNum = 500)

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))
