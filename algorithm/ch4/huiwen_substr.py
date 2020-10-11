import time

# 辅助表 m 保存代价 m[i][j]
def huiwen(s):
    n = len(s)
    m = [[0 for i in range(n)] for i in range(n)]
    lensub = 0
    substr = []

    for j in range(0,n):
        for i in range(0,j+1):
            if j-i <= 1:
                if s[i]==s[j]:
                    m[i][j] = 1
                    if lensub < j - i + 1:
                        lensub = j - i + 1
                        substr = s[i:j + 1]
            else:
                if s[i] == s[j] and m[i+1][j-1]==1:
                    m[i][j] = 1
                    if lensub < j-i+1:
                        lensub = j-i+1
                        substr = s[i:j+1]
    return substr,lensub

def huiwen_substr(s):
    k = len(s)  # 计算字符串的长度
    matrix = [[0 for i in range(k)] for i in range(k)]  # 初始化n*n的列表
    logestSubStr = ""  # 存储最长回文子串
    logestLen = 0  # 最长回文子串的长度

    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    matrix[i][j] = 1  # 此时f(i,j)置为true
                    if logestLen < j - i + 1:  # 将s[i:j]的长度与当前的回文子串的最长长度相比
                        logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                        logestLen = j - i + 1  # 当前最长回文子串的长度
            else:
                if s[i] == s[j] and matrix[i + 1][j - 1]:  # 判断
                    matrix[i][j] = 1
                    if logestLen < j - i + 1:
                        logestSubStr = s[i:j + 1]
                        logestLen = j - i + 1
    return logestSubStr


if __name__ == '__main__':
    start = time.time()
    s = "abcddddddd"
    # huiwen_substr(s)
    substr,len = huiwen(s)
    print("最长回文子串：",substr)
    print("最长回文子串长度：",len)
    end = time.time()
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))