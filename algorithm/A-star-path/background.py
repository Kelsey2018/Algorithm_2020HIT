import numpy as np

width_blocks = 40
height_blocks = 20
BLOCK_SIZE = 30  # size of block

class Background:
    def __init__(self):
        self.obstacles_list = []
        self.desert_list = []
        self.river_list = []
        self.start_block = None
        self.end_block = None
        self.blocks = []

    def set_start(self,start):
        self.start = start

    def set_end(self,end):
        self.end = end

    def set_obstacles(self,obstacles_list):
        self.obstacles_list = obstacles_list

    def set_desert(self,desrt_list):
        self.desert_list = desrt_list

    def set_river(self,river_list):
        self.river_list = river_list

    def genrate_maze(self):
        maze = np.zeros((width_blocks,height_blocks))
        maze[self.start[0]][self.start[1]] = 1   #1 起点
        maze[self.end[0]][self.end[1]] = 9  # 9 终点
        #5 障碍
        for item in self.obstacles_list:
            maze[item[0]][item[1]] = 5

        #2 沙漠
        if len(self.desert_list) > 0:
            for item in self.desert_list:
                maze[item[0]][item[1]] = 2

        #3 溪流
        if len(self.river_list) > 0:
            for item in self.river_list:
                maze[item[0]][item[1]] = 3

        maze = maze.astype(int)
        return maze
