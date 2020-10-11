# -*-coding:utf-8 -*-

class Node:
    """节点类"""
    def __init__(self, elem, lchild=None, rchild=None,lweight=None,rweight=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
        # self.lweight = lweight
        # self.rweight = rweight
        if self.lchild != None:
            self.lweight = lweight
        if self.rchild != None:
            self.rweight = rweight

class Tree:
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if not self._root:
            self._root = node
            return
        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            if not cur.lchild:
                cur.lchild = node
                return
            elif not cur.rchild:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)
                queue.append(cur.lchild)

############构建一棵树
tree = Tree()
root = Node(elem='a',lweight=1)
node_1 = Node(elem='b',lweight=2,rweight=2)
node_2 = Node(elem='c',lweight=3)
node_3 = Node(elem='d')
node_4 = Node(elem='e',lweight=4,rweight=5)
node_5 = Node(elem='f')
node_6 = Node(elem='g')
root.lchild = node_1
node_1.lchild = node_2
node_1.rchild = node_3
node_2.lchild = node_4
node_4.lchild = node_5
node_4.rchild = node_6

def divide_and_conquer(root,n=None,):
    if root.lchild == None and root.rchild != None:
        if root.lweight <= n :
            return 1

    if root.lchild != None and root.rchild == None:
        if root.rweight <= n :
            return 1
    # divide
    TL = tree.root.lchid
    TR = tree.root.rchid

    #conquer
    L_nodes = divide_and_conquer(TL, n=(n - TL.lweight))
    R_nodes = divide_and_conquer(TR, n=(n - TL.rweight))