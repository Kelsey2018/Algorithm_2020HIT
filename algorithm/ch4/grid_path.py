import time
import random
import numpy as np

# 辅助表 m 保存代价 m[i][j]
def grid_path(matrix):
    # path = [[1,2],[2,3]]
    path = []
    len = 0
    m = matrix.shape[0]
    n = matrix.shape[1]
    d = [[None for i in range(n)] for i in range(m)]
    memo = [[0 for i in range(n)] for i in range(m)]

    # 初始化第一行和第一列
    memo[0][0] = matrix[0][0]
    for h in range(1,m):
        d[h][0] = 'down'
        memo[h][0] = matrix[h][0] + memo [h-1][0]
    for l in range(1,n):
        d[0][l] = 'right'
        memo[0][l] = matrix[0][l] + memo[0][l-1]

    for i in range(1,m):
        for j in range(1,n):
            up = memo[i-1][j]
            left = memo[i][j-1]
            if up < left:
                d[i][j] = 'down'
                memo[i][j] = up + matrix[i][j]
            else:
                d[i][j] = 'right'
                memo[i][j] = left + matrix[i][j]
    # 保存路径
    i = m-1
    j = n-1
    path.append((m - 1, n - 1))
    while d[i][j]:
        if d[i][j] == 'right':
            path.append((i, j - 1))
            j = j - 1
        if d[i][j] == 'down':
            path.append((i - 1, j))
            i = i-1
    path.reverse()

    return memo,d,path


if __name__ == '__main__':
    start = time.time()
    matrix = np.random.randint(0,10,(3,3))
    print(np.array(matrix))

    m,d,path = grid_path(matrix)
    print(np.array(m))
    print(np.array(d))

    print("路径：")
    for i in path:
        print(i)
    print("最小路径长度：",m[-1][-1])
    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))