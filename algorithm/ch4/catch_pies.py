import time
import random
import numpy as np

# 辅助表 m 保存代价 memo[i][j]
def xianbing(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    print(m)
    print(n)
    memo = [[0 for i in range(n)] for i in range(m)]
    d = [[None for i in range(n)] for i in range(m)]
    maxnum = 0

    s = 5
    t_maxnum = max(matrix[0][s], matrix[0][s - 1], matrix[0][s + 1])
    for j in range(0,n):
        memo[0][j] = matrix[0][j]
    if matrix[0][s] == t_maxnum:  # 如果当前位置馅饼数最多
        d[0][s] = 'stay'
        maxnum = matrix[0][s]
    elif matrix[0][s - 1] == t_maxnum:  # 如果当前位置-1馅饼数最多
        d[0][s - 1] = 'left'
        maxnum = matrix[0][s-1]
        s = s-1
    elif matrix[0][s + 1] == t_maxnum:  # 如果当前位置+1馅饼数最多
        d[0][s + 1] = 'right'
        maxnum = matrix[0][s+1]
        s = s+1

    for t in range(1,m):
        t_maxnum = max(matrix[t][s], matrix[t][s-1], matrix[t][s+1])
        if matrix[t][s]==t_maxnum: #如果当前位置馅饼数最多
            memo[t][s] = memo[t-1][s] + matrix[t][s]
            d[t][s] = 'stay'
            maxnum = memo[t][s]
        elif matrix[t][s-1]==t_maxnum: #如果当前位置-1馅饼数最多
            memo[t][s-1] = memo[t - 1][s] + matrix[t][s-1]
            d[t][s-1] = 'left'
            maxnum = memo[t][s - 1]
            s = s-1
        elif matrix[t][s+1]==t_maxnum: #如果当前位置+1馅饼数最多
            memo[t][s+1] = memo[t - 1][s] + matrix[t][s+1]
            d[t][s+1] = 'right'
            maxnum = memo[t][s + 1]
            s = s+1
        # print("当前位置：",s)


    print("maxnum = ",maxnum)
    return memo,d


if __name__ == '__main__':
    start = time.time()
    matrix = np.random.randint(0, 10, (6, 11))
    print(np.array(matrix))
    maxnum,d = xianbing(matrix)
    print(np.array(maxnum))
    print(np.array(d))
    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))