import time
import numpy as np


# 辅助表 m 保存代价 m[i,j]
# 辅助表 s 记录最优值 m[i,j]对应的分割点 k
def maxChain(p):
    n = len(p)
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]

    for l in range(2,n):  # 对角线
        for i in range(1,n-l+1):  # 行
            j = i+l-1
           # m[i][j] = 9999999999
            for k in range(i,j):
                if(k == i):
                    m[i][j] = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                    s[i][j] = k

                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

# 输出矩阵链的最优括号化方法
def printOpt(s, i, j):
    if i == j:
        print("A",i, end='')
    else:
        print("(", end='')
        printOpt(s, i, s[i][j])
        printOpt(s, s[i][j]+1, j)
        print(")", end='')

if __name__ == '__main__':
    start = time.time()

    p = [10, 6, 5, 7, 10, 20]
    m, s = maxChain(p)
    print(np.array(m))
    print(np.array(s))
    print("最优括号化方案为：")
    printOpt(s, 1, 5)
    print("")
    print("其标量乘法次数为：", m[1][5])  # 二维数组访问的下标是可以人为设定的

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))