# -*- coding: utf-8 -*-
# @Author: Xiang xi
# @Date:   2020-05-08 17:19:00

import numpy as np
import random
import math

# cost_1 = 10
# cost_2 = 14
# cost_desert = 40
# cost_river = 20

cost_1 = 1
cost_2 = 1.414
cost_desert = 4
cost_river = 2


class Node(object):
    def __init__(self, parent, position, direction=None):
        self.position = position
        self.parent = parent
        self.direction = direction
        self.g = self.f = self.h = 0

    def __eq__(self, other):
        return self.position == other.position


class A_star:
    def __init__(self, maze, start, end, background):
        self.start = start
        self.end = end
        self.backgound = background
        self.maze = maze
        self.desert_list = background.desert_list
        self.river_list = background.river_list
        self.obstacles_list = background.obstacles_list

    def cal_direction(self, x_plus, y_plus):
        if y_plus == -1:
            return x_plus + 1
        elif y_plus == 0:
            return 3 if x_plus == -1 else 4
        elif y_plus == 1:
            return x_plus + 6

    def cal_m(self, position):
        if position in self.desert_list:
            return cost_desert
        elif position in self.river_list:
            return cost_river
        else:
            return 0

    def cal_g(self, position, direction):
        # m = self.cal_m(position)
        m = 0
        if self.maze[position[0]][position[1]] == 2:
            m = cost_desert
        elif self.maze[position[0]][position[1]] == 3:
            m = cost_river

        if direction in [1, 3, 4, 6]:
            return cost_1 + m
        elif direction in [0, 2, 5, 7]:
            return cost_2 + m

    def distance(self, x1, y1, x2, y2):  # 这里定义为为曼哈顿距离
        return math.sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2) * cost_1
        # return (abs(x2 - x1) + abs(y2 - y1)) * cost_1
        
        # h_diagonal = min(abs(x1-x2), abs(y1-y2))
        # h_straight = (abs(x1-x2) + abs(y1-y2))
        # return cost_2 * h_diagonal + cost_1 * (h_straight - 2 * h_diagonal)


    def cal_h(self, position,end_node):
        end_x = end_node.position[0]
        end_y = end_node.position[1]

        curr_x = position[0]
        curr_y = position[1]

        manhatten = self.distance(curr_x, curr_y, end_x, end_y)
        return manhatten

    def a_star_single_direction(self):
        open_list = []
        closed_list = []
        start_node = Node(None, self.start)
        end_node = Node(None, self.end)
        start_node.g = start_node.h = start_node.f = 0
        end_node.g = end_node.h = end_node.f = 0

        open_list.append(start_node)

        while len(open_list) > 0:
            current_node = open_list[0]
            ind = 0
            # best-first
            for index, item in enumerate(open_list):
                if current_node.f > item.f:
                    current_node = item
                    ind = index

            open_list.pop(ind)
            print("当前访问结点，",current_node.position)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                curr = current_node
                while curr.parent is not None:
                    path.append(curr.position)
                    curr = curr.parent
                path.append(self.start)
                print("最终代价为", current_node.f)
                return (path[::-1])[1:-1]

            children = []

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    temp_pos = (current_node.position[0] + i, current_node.position[1] + j)

                    a = temp_pos[0]
                    b = temp_pos[1]

                    if a < 0 or a >= len(self.maze) or b < 0 or b >= len(self.maze[0]):
                        continue
                    if self.maze[a][b] == 5:
                        continue

                    direction = self.cal_direction(i, j)
                    # print("当前孩子相对于父结点的方向为：",direction)
                    temp_node = Node(current_node, temp_pos, direction)
                    children.append(temp_node)


            for child in children:
                def node2position(open_list):
                    position_list = []
                    for item in open_list:
                        position_list.append(item.position)
                    return position_list
                if child.position in node2position(closed_list):
                    continue

                child.g = current_node.g + self.cal_g(child.position, child.direction)
                child.h = self.cal_h(child.position,end_node)
                child.f = child.g + child.h

                if child.position in node2position(open_list):
                    for index,open_node in enumerate(open_list):
                        if child.position == open_node.position:
                            if child.g >= open_node.g:
                                continue
                            else:
                                open_list[index] = child
                                # print("更新后：",open_list[index].g)
                                # print("child：",child.g)
                else:
                    open_list.append(child)



    def find_child_list(self, open_list, closed_list, end_node):
        if len(open_list) > 0:
            current_node = open_list[0]
            ind = 0
            # best-first
            for index, item in enumerate(open_list):
                if current_node.f > item.f:
                    current_node = item
                    ind = index

            open_list.pop(ind)
            closed_list.append(current_node)

            new_start = current_node

            children = []

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    temp_pos = (current_node.position[0] + i, current_node.position[1] + j)

                    a = temp_pos[0]
                    b = temp_pos[1]

                    if a < 0 or a >= len(self.maze) or b < 0 or b >= len(self.maze[0]):
                        continue
                    if self.maze[a][b] == 5:
                        continue

                    direction = self.cal_direction(i, j)
                    # print("当前孩子相对于父结点的方向为：",direction)
                    temp_node = Node(current_node, temp_pos, direction)
                    children.append(temp_node)

            for child in children:
                def node2position(open_list):
                    position_list = []
                    for item in open_list:
                        position_list.append(item.position)
                    return position_list

                if child.position in node2position(closed_list):
                    continue

                child.g = current_node.g + self.cal_g(child.position, child.direction)
                child.h = self.cal_h(child.position, end_node)
                child.f = child.g + child.h

                # for open_node in open_list:
                #     if child == open_node and child.g > open_node.g:
                #         continue
                #
                # open_list.append(child)
                if child.position in node2position(open_list):
                    for index,open_node in enumerate(open_list):
                        if child.position == open_node.position:
                            if child.g >= open_node.g:
                                continue
                            else:
                                open_list[index] = child
                else:
                    open_list.append(child)

            return open_list, closed_list

    def find_new_curr(self, open_list):
        if len(open_list) > 0:
            current_node = open_list[0]
            ind = 0
            # best-first
            for index, item in enumerate(open_list):
                if current_node.f > item.f:
                    current_node = item
                    ind = index

            return current_node

    def a_star_double_direction(self):
        open_list_1 = []
        open_list_2 = []
        closed_list_1 = []
        closed_list_2 = []

        start_node = Node(None, self.start)
        end_node = Node(None, self.end)
        start_node.g = start_node.h = start_node.f = 0
        end_node.g = end_node.h = end_node.f = 0

        open_list_1.append(start_node)
        open_list_2.append(end_node)

        new_start = start_node
        new_end = end_node
        position_list = []

        while new_start.position not in position_list:
            open_list_1, closed_list_1 = self.find_child_list(open_list_1, closed_list_1, end_node)
            open_list_2, closed_list_2 = self.find_child_list(open_list_2, closed_list_2, start_node)
            new_start = self.find_new_curr(open_list_1)
            new_end = self.find_new_curr(open_list_2)
            # print("新的起点",new_start.position)
            # print("新的终点",new_end.position)

            def node2position(open_list):
                position_list = []
                for item in open_list:
                    position_list.append(item.position)
                return position_list

            position_list = node2position(open_list_2)

        print("相遇点", new_start.position)
        meet = new_start

        # 打印路径
        path_1 = []
        path_2 = []

        while new_start is not None:
            path_1.append(new_start.position)
            new_start = new_start.parent

        for item in open_list_2:
            if meet.position == item.position:
                # print(item.position)
                new_end = item
                break

        # 代价
        final_cost = meet.f + new_end.f
        print("最终的代价：",final_cost)

        while new_end is not None:
            path_2.append(new_end.position)
            new_end = new_end.parent

        return (path_1[::-1])[1:], ((path_2[::-1])[:-1])[1:]





