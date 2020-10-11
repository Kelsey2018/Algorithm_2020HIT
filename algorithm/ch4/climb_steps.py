import time
import numpy as np
import math

# 辅助表 m 保存代价 m[i]
def climb_steps(n):
    k = 0
    if n == 1:
        return 1
    if n ==2:
        return 2



    return k

if __name__ == '__main__':
    start = time.time()
    n = 3
    print(climb_steps(n))
    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))