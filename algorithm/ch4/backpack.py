import time
import numpy as np


# 辅助表 m 保存代价 m[i,j]
def backpack(w,v,c,n):
    m = [[0 for i in range(c+1)]for j in range(n)]

    # print(min(w[n-1],c))
    for j in range(min(w[n-1],c)): # 初始化最后一行
        m[n-1][j] = 0
    for j in range(w[n-1],c+1):
        m[n-1][j] = v[n-1]

    for i in range(n-2,0,-1):
        for j in range(min(w[i]-1,c)):
            # print(i,j)
            m[i][j] = m[i+1][j]
        for j in range(w[i],c+1):
            m[i][j] = max(m[i+1][j], m[i+1][j-w[i]]+v[i])

    if c<w[0]:
        m[0][c] = m[1][c]
    else:
        m[0][c] = max(m[1][c] , m[1][c-w[0]]+v[0])
    return m

def print_bag(m,w,c):
    p = [0 for i in range(n)]

    h = 0
    l = c
    while l >= 0 and h < n-1:
        if m[h][l] == m[h + 1][l]:
            print("c=",c)
            print(h,l)
            p[h] = 0
            h = h + 1

        else:
            p[h] = 1
            l = l - w[h]
            h = h + 1

    if m[h][l] != 0:
        p[h] = 1
    return p
if __name__ == '__main__':
    start = time.time()

    w = [2,2,6,5,4]
    v = [6,3,5,4,6]
    c = 10
    n = 5
    m = backpack(w,v,c,n)
    print(np.array(m))

    p = print_bag(m,w,c)
    print(np.array(p))

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))