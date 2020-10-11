# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : least_element.py
import time
import numpy as np

class HamiltonPath:

    def __init__(self, filename, s):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None

        with open(filename) as f:
            line_num = 0  # 第一行是顶点数和边数
            for line in f:
                if line_num == 0:
                    v, e = line.strip().split()
                    self.V = int(v)
                    self.E = int(e)
                    self.adj = [[] for i in range(self.V)] # 创建二维数组即邻接表
                else:
                    # 读取边 写入邻接表
                    v1, v2 = line.strip().split()
                    # 转化为整数
                    v1 = int(v1)
                    v2 = int(v2)
                    self.adj[v1].append(v2)
                    self.adj[v2].append(v1)
                line_num += 1
        self.__s = s
        self.__visited = [False for i in range(self.V)]
        self.__pre = [-1 for i in range(self.V)]
        self.__end = -1
        self.graphDFS(s, s, self.V)
        self.graphBFS(s, s, self.V)

    def get_graph_information(self):
        """
        打印图的邻接表
        :return:
        """
        print("V={}, E={}".format(self.V, self.E))
        for i, v in enumerate(self.adj):
            print("{} : {}".format(i, v))

    def validateVertex(self, v):
        """
        验证顶点取值
        :param v:
        :return:
        """
        if v<0 or v>=self.V:
            raise ValueError("v值超出范围")

    def hasEdge(self, v, w):
        """
        判断两个顶点是否存在
        :param v: 第一个顶点
        :param w: 第二个顶点
        :return: true or false
        """
        self.validateVertex(v)
        self.validateVertex(w)
        return w in self.adj[v]

    def degree(self, v):
        """
        求某个顶点的度
        :param v:
        :return:
        """
        self.validateVertex(v)
        return len(self.adj[v])


    def graphDFS(self, v, parent, left):

        # 标记v顶点已经遍历过了
        self.__visited[v] = True
        # 记录父亲结点
        self.__pre[v] = parent
        # 访问了v，剩下顶点数减一
        left -= 1
        if left == 0:
            self.__end = v
            return True

        for w in self.adj[v]:
            if self.__visited[w] == False:
                if self.graphDFS(w, v, left):
                    return True

        # 找不到HamiltonLoop，开始回溯到上一个结点
        self.__visited[v] = False
        return False

    def graphBFS(self, v, parent, left):

        # 标记v顶点已经遍历过了
        self.__visited[v] = True
        # 记录父亲结点
        self.__pre[v] = parent

        routes = [[v]]
        for i in range(left-1):
            update_routes = []
            for route in routes:
                top = route[len(route) - 1]
                single_route = []
                for w in self.adj[top]:
                    if w not in route:
                        single_route.append(route+[w])
                update_routes += single_route
            routes = update_routes

        for route in routes:
            route.append(v)
        print("==========BFS=============")
        print(routes)
        return routes

    def getHamiltonPath(self):
        res = []
        if self.__end == -1:
            return res

        cur = self.__end
        while cur != 0:
            res.append(cur)
            cur = self.__pre[cur]
        res.append(self.__s)#把开始结点加入进去
        res.reverse()
        res.append(self.__s)
        if len(res)< 8:
            print("所求哈密尔顿环失败")
            return 0
        print("所求哈密顿路径为：", res)

if __name__ == '__main__':
    hl = HamiltonPath("graph1.txt", 0)
    hl.get_graph_information()
    hl.getHamiltonPath()