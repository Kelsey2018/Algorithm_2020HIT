# -*- coding: utf-8 -*-
import time
# 递归
def fab(n):
    # 终止条件 边界
    if n <= 2:
        return 1
    else:
        # 最优子结构 状态转移公式
        return fab(n - 1) + fab(n - 2)

# 动态规划
def fab_3(x):
    arr=[]
    arr.append(1)
    arr.append(1)
    for i in range(2,x+1,1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[x]


if __name__ == '__main__':
    start = time.time()
    # fab_3(10)
    print(fab_3(10))
    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))