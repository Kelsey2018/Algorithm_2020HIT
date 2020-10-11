import time
import numpy as np
import math

# 辅助表 m 保存代价 m[i]
def maxsun_substr(num: np.ndarray):
    m = [0 for i in range(len(num))]
    sum = 0
    if len(num) == 0:
        return 0

    m[0] = num[0]
    for i in range(1,len(num)):
        m[i] = max(num[i],m[i-1]+num[i])
        sum = max(m[i], sum)

    return sum

if __name__ == '__main__':
    start = time.time()

    p = [-2,1,-3,4,-1,2,1,-5,4]
    sub,maxsum = maxsun_substr(p)
    print(maxsum)

    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))