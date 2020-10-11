# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 19:08
# @Author  : xiang xi
# @Email   : 19S103133@stu.hit.edu.cn
# @File    : Finding_Convex_hull.py

import matplotlib.pyplot as plt
import numpy as np
import random
import time
import math


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size() - 1]

    def top_2(self):
        return self.items[self.size() - 2]


def rand_point_set(n, range_min=0, range_max=101):
    """
    随机生成具有 n 个点的点集
    :param range_max: 生成随机点最小值，默认 0
    :param range_min: 生成随机点最大值，默认 100
    :param n: int
    :return: list [(x1,y1)...(xn,yn)]
    """
    try:
        return list(zip([random.uniform(range_min, range_max) for _ in range(n)],
                        [random.uniform(range_min, range_max) for _ in range(n)]))
    except IndexError as e:
        print("\033[31m" + ''.join(e.args) + "\n输入范围有误！" + '\033[0m')


def is_one_side(a, b, c):
    """
    判断一个点在一条直线的左边还是右边
    判断点 C(x3,y3) 在直线 AB 的左边还是右边
                     [ 其中 A(x1,y1), B(x2,y2) ]
    计算此三阶行列式：
    | x1 y1 1 |
    | x2 y2 1 | = x1y2 + x3y1 + x2y3 - x3y2 - x2y1 - x1y3
    | x3 y3 1 |
    当上式结果为正时, C 在 AB 左侧
             为负时, C 在 AB 右侧
    :return: 如果点 C 在直线 AB 左侧，返回 True
             否则  返回 False
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    number = x1 * y2 + x3 * y1 + x2 * y3 - x3 * y2 - x2 * y1 - x1 * y3
    if x1 == x2 == x3 or y1 == y2 == y3 or a == c or b == c:
        number = 0
    return number


def BruteForCH(lists):
    """
    蛮力法输出边界边集
    :param lists:
    :return: list [( , )...( , )]
    """
    lists.sort()
    list_border_line = []  # 边集
    for i in lists:
        for j in lists[lists.index(i) + 1:]:
            count_left = 0
            count_right = 0
            for k in lists:
                if k == i or k == j:
                    continue
                else:
                    if is_one_side(i, j, k) > 0:
                        count_left += 1
                    if is_one_side(i, j, k) < 0:
                        count_right += 1
                    if is_one_side(i, j, k) == 0:
                        pass
            if count_right != 0 and count_left != 0:
                pass
            else:
                list_border_line.append((i, j))
    return list_border_line


#############################################Graham-Scan##########################
def swap(a: np.ndarray, li: int, ri: int):
    """Swap elements of numpy array.
    Args:
        a: numpy array.
        li: left index.
        ri: right index.
    """
    tmp = np.copy(a[li])
    a[li] = a[ri]
    a[ri] = tmp


def ccw(p1: np.ndarray, p2: np.ndarray, p3: np.ndarray) -> int:
    """Determine if points turn counter-clockwise.
    Args:
        p1: first point.
        p2: second point.
        p3: third point.
    Returns:
        -1 => 逆时针方向
        1 => 顺时针方向
        0 => 在线上
    """
    dx1 = p2[0] - p1[0]
    dy1 = p2[1] - p1[1]
    dx2 = p3[0] - p1[0]
    dy2 = p3[1] - p1[1]

    dx1dy2 = dx1 * dy2
    dy1dx2 = dy1 * dx2

    if dx1dy2 > dy1dx2:
        return 1
    if dx1dy2 < dy1dx2:
        return -1
    if dx1 * dx2 < 0 or dy1 * dy2 < 0:
        return -1
    if dx1 * dx1 + dy1 * dy1 < dx2 * dx2 + dy2 * dy2:
        return 1

    return 0

def extract_primary(points: np.ndarray) -> tuple:
    """Kind of self-explanatory.
    Args:
        points:
    Returns:
        primary (start) point, remaining points.
    """
    points_y = np.array([v[1] for v in points])
    min_point_idx = np.argmin(points_y)  # 找出纵坐标最小的点索引
    # min_point_idx = np.argmin(points)
    primary = np.copy(points[min_point_idx])
    points = np.array(points)
    remaining_points = np.concatenate(
        (points[:min_point_idx], points[min_point_idx + 1:])
    )
    return primary, remaining_points

def calculate_corner(A, B):
    """
    :param A: the base point
    :param B: the calculated point
    :return: the corner of A and B
    """
    x = B[0] - A[0]
    y = B[1] - A[1]
    if x == 0 and y > 0: return 90.0
    elif x == 0 and y < 0: return -90.0
    elif x==0 and y==0: return 0.0

    corner = math.atan(y/x)
    if corner>0 and y>0: return corner * 180 / math.pi
    elif corner<0 and y>0: return corner * 180 / math.pi + 180.0
    elif corner<0 and y<0: return corner * 180 / math.pi
    elif corner>0 and y<0: return corner * 180 / math.pi - 180.0
    elif corner==0 and x<0: return 180.0
    elif corner==0 and x>=0: return 0.0

def sort_for_graham_scan(points: np.ndarray, primary: np.ndarray) -> np.ndarray:
    """Sort points for graham scan.
    Args:
        points: points to sort .
        primary: primary (start) point (not in array).
    Returns:
        sorted points.
    """
    #计算极角
    # print('points.shape[0]',points.shape[0])
    corners = []
    for index in range(points.shape[0]):
        corner = calculate_corner(primary, points[index])
        corners.append(corner)

    #排序，采用的argsort内置函数quicksort
    corners = np.array(corners)
    corners_index = corners.argsort()
    sorted_points = np.array(points)[corners_index]
    hull = np.concatenate(
        (sorted_points[-1:], [primary], sorted_points)
    )
    return hull


def find_hull_vertices(points: np.ndarray) -> np.ndarray:
    """Finds points that don't require clockwise turns to connect.
    Args:
        points: sorted points. Will be modified by this process.
    Returns:
        hull vertices.
    """
    M = 3
    N = points.shape[0]
    for i in range(4, N):
        while ccw(points[M], points[M - 1], points[i]) >= 0:
            M -= 1
        M += 1
        swap(points, M, i)
    return points[1:M + 1]

def graham_scan(points: np.ndarray) -> np.ndarray:
    """Find vertices of convex hull around points.
    Args:
        points: (x, y) coordinates of points.
    Returns:
        hull: points that are vertices on convex hull.
    """
    primary, remaining_points = extract_primary(points)
    sorted_points = sort_for_graham_scan(remaining_points, primary)
    hull = find_hull_vertices(sorted_points)
    return hull


def clockwise_turn(list):
    return list
def sort_clockwise(points,primary):
    return points
def clock_turn(list):
    return list
def mergeSort(list_QL,list_QR_1,list_QR_2):
    # print("list_QL = ",list_QL)
    merge_list = list(list_QL) + list(list_QR_1) + list(list_QR_2)
    return merge_list

def get_medium(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[~mid]) / 2

def mergesort(list_QL,list_QR_1,list_QR_2,L_inner_point):
    # 三路归并排序
    border_list = []
    head_1,head_2,head_3 = 0,0,0
    while list_QR_1[head_1] and list_QR_1[head_2] and list_QR_2[head_3] >0:
        c1 = calculate_corner(list_QL[head_1],L_inner_point)
        c2 = calculate_corner(list_QR_1[head_2],L_inner_point)
        c3 = calculate_corner(list_QR_2[head_3],L_inner_point)
        if c1>c2 and c1>c3:
            border_list.append(list_QL[head_1])
            head_1 = head_1 + 1
        elif c2>c1 and c2>c3:
            border_list.append(list_QR_1[head_2])
            head_2 = head_2 + 1
        elif c3>c1 and c3>c2:
            border_list.append(list_QR_2[head_3])
            head_3 = head_3 + 1
    while list_QL[head_1] and list_QR_1[head_2]:
        c1 = calculate_corner(list_QL[head_1], L_inner_point)
        c2 = calculate_corner(list_QR_1[head_2], L_inner_point)
        if c1 > c2:
            border_list.append(list_QL[head_1])
            head_1 = head_1 + 1
        else:
            border_list.append(list_QR_1[head_2])
            head_2 = head_2 + 1
    while list_QL[head_1] and list_QR_2[head_3]:
        c1 = calculate_corner(list_QL[head_1],L_inner_point)
        c3 = calculate_corner(list_QR_2[head_3], L_inner_point)
        if c1 > c3:
            border_list.append(list_QL[head_1])
            head_1 = head_1 + 1
        else:
            border_list.append(list_QR_2[head_3])
            head_3 = head_3 + 1
    while list_QR_1[head_2]  and list_QR_2[head_3] :
        c2 = calculate_corner(list_QR_1[head_2], L_inner_point)
        c3 = calculate_corner(list_QR_2[head_3], L_inner_point)
        if c2 > c3:
            border_list.append(list_QR_1[head_2])
            head_2 = head_2 + 1
        else:
            border_list.append(list_QR_2[head_3])
            head_3 = head_3 + 1
    while list_QL[head_1]:
        border_list.append(list_QL[head_1])
        head_1 = head_1 + 1
    while list_QR_1[head_2]:
        border_list.append(list_QR_1[head_2])
        head_2 = head_2 + 1
    while list_QR_2[head_3]:
        border_list.append(list_QR_2[head_3])
        head_3 = head_3 + 1
    return border_list


def clockTurn(list):
    list = np.array(list)
    points_y = np.array([v[1] for v in list])
    points_index = points_y.argsort()
    sorted_points = np.array(list)[points_index]
    return sorted_points

def clockwiseTurn(list):
    list = np.array(list)
    points_y = np.array([v[1] for v in list])
    points_index = points_y.argsort()
    sorted_points = np.array(list)[points_index]
    return sorted_points[::-1]

def graham_scan_divided(temp_Q,primary):
    result = graham_scan(temp_Q)
    return result


def sortClockwise(points:np.ndarray,primary:np.ndarray) -> np.ndarray:
    corners = []
    points = np.array(points)

    for index in range(points.shape[0]):
        corner = calculate_corner(primary, points[index])
        corners.append(corner)

    # 排序，采用的argsort内置函数quicksort
    corners = np.array(corners)
    corners_index = corners.argsort()
    sorted_points = np.array(points)[corners_index]
    return sorted_points


def graham_scan_divide(temp_Q,primary):
    sorted_points =  np.concatenate(
        (temp_Q[-1:], [primary], temp_Q)
    )
    # hull = find_hull_vertices(sorted_points)
    M = 3
    N = sorted_points.shape[0]
    for i in range(4, N):
        while ccw(sorted_points[M], sorted_points[M - 1], sorted_points[i]) >= 0:
            M -= 1
        M += 1
        swap(sorted_points, M, i)
    return sorted_points[1:M + 1]
    # return hull


def Divide_and_Conquer(points):
    # preprocess
    if len(points) <= 3: 
      return points
    array_points = np.array(points)

    points_x = array_points[:, 0]
    mid = get_medium(points_x)

    # divide
    QL = []
    QR = []
    for i in range(len(points)):
        px = points[i][0]
        py = points[i][1]
        if px <= mid:
            QL.append((px, py))
        else:
            QR.append((px, py))

    # 防止出现QL或QL一侧为空的情况，否则将无限循环
    if QL == []:
        return QR
    elif QR == []:
        return QL

    # print("QL",QL)
    # print("QR",QR)

    # conquer
    sub_QL = Divide_and_Conquer(QL)
    sub_QR = Divide_and_Conquer(QR)

    # merge
    # Q = list(sub_QL) + list(sub_QR)
    # print("Q = ",Q)

    #找左边点集的一个内点
    sum_x = 0
    sum_y = 0
    num = 1
    for item in sub_QL:
        x,y = item[0],item[1]
        sum_x = sum_x + x
        sum_y = sum_y + y
        num = num + 1

    L_inner_point = np.array((float(sum_x/num),float(sum_y/num)))
    # print(L_inner_point)

    #找右边点集的最高、最低点
    print("右边点集",sub_QR)
    print("左边点集",sub_QL)
    points_y = np.array([v[1] for v in sub_QR])
    min_point_idx = np.argmin(points_y)  # 找出纵坐标最小的点索引
    max_point_idx = np.argmax(points_y)  # 找出纵坐标最大的点索引
    min_y_point = np.array(np.copy(sub_QR[min_point_idx]))
    max_y_point = np.array(np.copy(sub_QR[max_point_idx]))

    #三个序列的三路归并
    list_QL = sub_QL
    list_QL = sort_clockwise(list_QL,L_inner_point)#逆时针
    list_QR_1 = []
    list_QR_2 = []
    for item in sub_QR:
        if ccw(min_y_point,max_y_point,item) == -1:
            list_QR_1.append(item)
            list_QR_1 = clock_turn(list_QR_1)#顺时针
        elif ccw(min_y_point,max_y_point,item) == 1:
            list_QR_2.append(item)
        else:
            pass
    list_QR_2.append((min_y_point[0],min_y_point[1]))
    list_QR_2.append((max_y_point[0],max_y_point[1]))
    list_QR_2 = clockwise_turn(list_QR_2)#逆时针
    print(list_QR_1)
    print(list_QR_2)

    temp_Q = mergeSort(list_QL,list_QR_1,list_QR_2)
    print("temp_Q = ",temp_Q)
    result = graham_scan_divided(temp_Q,L_inner_point)
    return result


def draw(list_all, list_border):
    """
    画图
    :param list_all: 所有点集
    :param list_border: 所有边集
    :return: picture
    """
    list_all_x = []
    list_all_y = []
    for item in list_all:
        a, b = item
        list_all_x.append(a)
        list_all_y.append(b)
    for item in list_border:
        item_1, item_2 = item
        #  横坐标,纵坐标
        one_, oneI = item_1
        two_, twoI = item_2
        plt.plot([one_, two_], [oneI, twoI])
    plt.scatter(list_all_x, list_all_y,c='b')
    plt.show()


def draw_1(list_all, list_border):
    """
    画图
    :param list_all: 所有点集
    :param list_border: 所有边集
    :return: picture
    """
    list_all_x = []
    list_all_y = []
    border_x = []
    border_y = []
    for item in list_all:
        a, b = item
        list_all_x.append(a)
        list_all_y.append(b)
    for item in list_border:
        print("item ", item)
        item_1, item_2 = item  # 横坐标,纵坐标
        border_x.append(item_1)
        border_y.append(item_2)
    x_0, y_0 = list_border[0]
    border_x.append(x_0)
    border_y.append(y_0)
    plt.plot(border_x, border_y)
    plt.scatter(list_all_x, list_all_y)
    plt.show()


if __name__ == '__main__':
    start = time.time()  # 程序运行开始时间

    print("""请输入Q点集的个数:\t""")
    list_points = rand_point_set(int(input()))

    model = '3'
    if model == '1':
        #########蛮力法##########
        hull = BruteForCH(list_points)
        draw(list_points,hull)
    elif model == '2':
        ########Graham-Scan法##########
        hull = graham_scan(list_points)
        draw_1(list_points,hull)
    elif model == '3':
        ###########分治法##############
        # Divide_and_Conquer(list_points)
        hull = Divide_and_Conquer(list_points)
        draw_1(list_points, hull)

    end = time.time()  # 程序运行结束时间
    print("Running Time(ms):{:.4f}".format((end - start) * 1000))