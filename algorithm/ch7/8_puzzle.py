# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:00
# @Author  : xiang xi
# @Email   : 974624751kelsey@gmail.com
# @File    : 8_puzzle.py
import time
import numpy as np

class eight_puzzle:

    def __init__(self,puzzle,diff,last_dir):
        self.diff = diff
        self.des_puzzle = [1,2,3,8,9,4,7,6,5]
        self.puzzle = puzzle
        self.last_dir = last_dir

    path = []

    def direction(self,puzzle,last_direction=None):
        idx_9 = puzzle.index(9) + 1
        next_direction = []
        final_direction = []
        if idx_9 == 1:
            next_direction = ['right','down']
        elif idx_9 == 2:
            next_direction = ['left','right', 'down']
        elif idx_9 == 3:
            next_direction = ['left','down']
        elif idx_9 == 4:
            next_direction = ['right','up','down']
        elif idx_9 == 5:
            next_direction = ['left','right','up','down']
        elif idx_9 == 6:
            next_direction = ['left','up','down']
        elif idx_9 == 7:
            next_direction = ['right','up']
        elif idx_9 == 8:
            next_direction = ['left','right','up']
        elif idx_9 == 9:
            next_direction = ['left','up']

        if last_direction == None:
            final_direction = next_direction
        else:
            final_direction = next_direction.copy()
            if self.reverse_dir(dir=last_direction) in final_direction:
                final_direction.remove(self.reverse_dir(dir=last_direction))
        print(final_direction)
        return final_direction

    def diff_n(self,puzzle):
        count = 0
        if puzzle == self.des_puzzle:
            return count

        for i in range(len(puzzle)):
            if puzzle[i]!=9:
                if puzzle[i] == self.des_puzzle[i]:
                    count += 1
        return 8-count

    def dir_change_puzzle(self,move_puzzle,direction,idx_9):
        puzzle = move_puzzle.copy()
        if direction == 'left':
            puzzle[idx_9-1],puzzle[idx_9] = puzzle[idx_9],puzzle[idx_9-1]
        elif direction == 'right':
            puzzle[idx_9+1],puzzle[idx_9] = puzzle[idx_9],puzzle[idx_9+1]
        elif direction == 'up':
            puzzle[idx_9-3],puzzle[idx_9] = puzzle[idx_9],puzzle[idx_9-3]
        elif direction == 'down':
            puzzle[idx_9+3],puzzle[idx_9] = puzzle[idx_9],puzzle[idx_9+3]
        return puzzle

    def reverse_dir(self,dir):
        redir = ''
        if dir == 'left':
            redir = 'right'
        elif dir == 'right':
            redir = 'left'
        elif dir == 'up':
            redir = 'down'
        elif dir == 'down':
            redir = 'up'
        return redir

    def sort_stack(self,stack):
        if len(stack) <= 1:
            return stack

        for i in range(len(stack)):#采用冒泡排序
            for j in range(i):
                if stack[j].diff < stack[j+1].diff:
                    stack[j],stack[j+1] = stack[j+1],stack[j]
        return stack

    def Hill_Climbing(self,stack):
        while len(stack) != 0:
            if self.diff_n(stack[-1].puzzle) == 0:  # 找到目标魔方
                return self.path

            print("当前魔方为：",stack[-1].puzzle)
            curr_puzzle = stack[-1].puzzle
            next_dirction = self.direction(puzzle=stack[-1].puzzle,last_direction=stack[-1].last_dir)

            stack.pop()
            last_stack_end = len(stack)
            temp_stack = []
            idx_9 = curr_puzzle.index(9)
            for dir in next_dirction:
                move_puzzle = self.dir_change_puzzle(move_puzzle=curr_puzzle,direction=dir,idx_9=idx_9)
                diff = self.diff_n(move_puzzle)
                sub_puzzle = eight_puzzle(puzzle=move_puzzle,diff=diff,last_dir=dir)
                temp_stack.append(sub_puzzle)
                # last_stack_end += 1
            temp_stack = self.sort_stack(temp_stack)
            stack = stack + temp_stack
            self.path.append(stack[-1].last_dir)


if __name__ == '__main__':
    init_puzzle = [2,3,9,1,8,5,7,4,6] #空格用9表示
    p = eight_puzzle(puzzle=init_puzzle,diff=0,last_dir=None)
    # p.puzzle = init_puzzle
    stack = []
    stack.append(p)
    print("路径：",p.Hill_Climbing(stack=stack))






