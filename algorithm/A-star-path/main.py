# -*- coding: utf-8 -*-
# @Author: Xiang xi
# @Date:   2020-05-08 17:19:00
import pygame
from findpath import A_star
from background import Background
from background import width_blocks,height_blocks,BLOCK_SIZE
import numpy as np


screen_width = width_blocks * BLOCK_SIZE
screen_height = height_blocks * BLOCK_SIZE


WHITE=(255,255,255)
BLACK = (0,0,0)#背景
GREEN = (0, 128, 0)#起点 开启列表
RED = (255, 0, 0)#终点
BLUE = (0, 0, 255)#溪流
YELLOW = (255, 255, 0)#关闭列表
PURPLE = (128, 0, 128)
ORANGE = (255,140,0)#沙漠
GRAY = (119,136,153) #障碍

def game(maze, sol=None,start=None,end=None):
    pygame.font.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("A* pathfinding")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # screen.fill(((169,169,169)))#背景色
        screen.fill((WHITE))#背景色

        # 画路径
        for i in range(maze.shape[0]):
            for j in range(maze.shape[1]):
                # 画路径
                if (i, j) in sol:
                    draw_rect(screen, i, j, BLACK)

                else:
                    # #画背景
                    if (i,j) not in sol:
                        if (i,j) == start:   #起点
                            draw_rect(screen, i, j, GREEN)
                        elif (i,j) == end:  # 终点
                            draw_rect(screen, i, j, RED)
                        elif maze[i][j] == 5:   #障碍
                            draw_rect(screen, i, j, GRAY)
                        elif maze[i][j] == 2:   #沙漠
                            draw_rect(screen, i, j, ORANGE)
                        elif maze[i][j] == 3:   #溪流
                            draw_rect(screen, i, j, BLUE)
                        # elif (i,j) == end:  # 终点
                        #     draw_rect(screen, i, j, RED)
                        elif maze[i][j] == 0:  #背景
                            draw_rect(screen, i, j, WHITE)
        pygame.display.update()

def game2(maze, path_1=None,path_2=None,start=None,end=None):
    pygame.font.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("A* pathfinding")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # screen.fill(((169,169,169)))#背景色
        screen.fill((WHITE))#背景色

        # 画路径
        for i in range(maze.shape[0]):
            for j in range(maze.shape[1]):
                # 画路径
                if (i, j) in path_1:
                    draw_rect(screen, i, j, BLACK)
                elif (i, j) in path_2:
                    draw_rect(screen, i, j, YELLOW)

                else:
                    # #画背景
                    if (i,j) not in path_1:
                        if (i,j) == start:   #起点
                            draw_rect(screen, i, j, GREEN)
                        elif (i,j) == end:  # 终点
                            draw_rect(screen, i, j, RED)
                        elif maze[i][j] == 5:   #障碍
                            draw_rect(screen, i, j, GRAY)
                        elif maze[i][j] == 2:   #沙漠
                            draw_rect(screen, i, j, ORANGE)
                        elif maze[i][j] == 3:   #溪流
                            draw_rect(screen, i, j, BLUE)

                        elif maze[i][j] == 0:  #背景
                            draw_rect(screen, i, j, WHITE)
        pygame.display.update()


def draw_rect(screen, x, y, color):
    # pygame.draw.rect(screen, BLACK, [s_height / n * y + 10, s_width / m * x + 10, 20, 20])
    # font = pygame.font.SysFont('comicsans', 30)
    # label = font.render(str(text), 1, color)
    # screen.blit(label, (s_height / n * y + 15, s_width / m * x + 10))
    pygame.draw.rect(screen, color, [x*BLOCK_SIZE , y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE], 0)
    pygame.draw.rect(screen, PURPLE, [x*BLOCK_SIZE ,y*BLOCK_SIZE, BLOCK_SIZE,BLOCK_SIZE], 3)


if __name__ == '__main__':

    model = "graph2-2"
    if model.startswith("graph1"):
        background = Background()
        background.set_start((3, 8))
        background.set_end((13, 9))
        background.set_obstacles([(6, 5), (6, 6), (7, 7), (7, 8), (7, 9), (8, 9), (8, 10), (8, 11)])

        path = A_star(background.genrate_maze(), background.start, background.end, background)
        #======================test1============================
        if model == "graph1-1":
            #单向
            grid_sol_single = path.a_star_single_direction()
            print(grid_sol_single)
            game(background.genrate_maze(), grid_sol_single,background.start,background.end)
        elif model == "graph1-2":
            #双向
            path_1,path_2 = path.a_star_double_direction()
            print(path_1)
            print(path_2)
            game2(background.genrate_maze(),path_1,path_2,background.start,background.end)

        # ======================test1============================
    elif model.startswith("graph2"):
        background = Background()
        # background.set_start((4,10))
        background.set_start((4, 10))
        background.set_end((35, 0))
        background.set_obstacles([(3, 0), (7, 0), (12, 0), (7, 1), (12, 1),
                                  (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (7, 2), (8, 2), (9, 2), (10, 2),
                                  (12, 2),
                                  (8, 3), (12, 3), (12, 4), (7, 5), (8, 5), (12, 5), (2, 6), (3, 6), (4, 6), (5, 6),
                                  (6, 6), (7, 6), (12, 6),
                                  (2, 7), (5, 7), (7, 7), (12, 7), (36, 7), (5, 8), (5, 9), (7, 9), (36, 9),
                                  (2, 10), (5, 10), (7, 10), (8, 10), (19, 10), (20, 10), (21, 10), (28, 10),
                                  (2, 11), (3, 11), (4, 11), (5, 11), (8, 11), (19, 11), (20, 11), (21, 11), (31, 11),
                                  (3, 12), (8, 12), (12, 12), (19, 12), (20, 12), (21, 12), (3, 13), (8, 13), (9, 13),
                                  (11, 13), (12, 13), (31, 13),
                                  (3, 14), (8, 14), (12, 14), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15),
                                  (12, 15), (24, 15), (25, 15),
                                  (3, 16), (12, 16), (24, 16), (25, 16), (7, 17), (12, 17), (3, 18), (7, 18), (12, 18),
                                  (3, 19), (7, 19), (12, 19)
                                  ])

        background.set_desert([(24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0), (30, 0), (31, 0),
                               (32, 0), (33, 0), (34, 0), (35, 0), (36, 0), (37, 0), (38, 0), (39, 0), (25, 1), (26, 1),
                               (27, 1), (28, 1), (29, 1),
                               (30, 1), (31, 1), (32, 1), (33, 1), (35, 1), (36, 1), (37, 1), (38, 1), (39, 1), (26, 2),
                               (27, 2), (28, 2), (29, 2),
                               (30, 2), (31, 2), (32, 2), (34, 2), (35, 2), (36, 2),(37, 2), (38, 2), (39, 2),
                               (26, 3), (27, 3), (28, 3), (29, 3),
                               (30, 3), (31, 3), (33, 3),
                               (34, 3), (35, 3),(36, 3), (26, 4), (27, 4), (28, 4), (29, 4), (30, 4), (31, 4), (32, 4), (34, 4),
                               (35, 4), (27, 5), (28, 5),
                               (29, 5), (30, 5), (31, 5), (32, 5), (27, 6), (28, 6), (29, 6), (30, 6), (31, 6), (32, 6),
                               (29, 7), (30, 7), (31, 7), (32, 7)
                               ])

        background.set_river(
            [(34, 1), (33, 2), (32, 3), (33, 4), (33, 5), (34, 5), (33, 6), (34, 6), (33, 7), (34, 7), (35, 7),
             (32, 8), (33, 8), (34, 8), (35, 8), (32, 9), (33, 9), (34, 9), (32, 10), (33, 10), (35, 10), (36, 10),
             (32, 11), (34, 11),
             (35, 11), (33, 12), (34, 12), (32, 13), (33, 13), (34, 13), (32, 14), (33, 14), (34, 14), (31, 15),
             (32, 15),
             (33, 15), (31, 16), (32, 16), (33, 16), (30, 17), (31, 17), (32, 17), (29, 18), (30, 18), (31, 18),
             (28, 19), (29, 19), (30, 19)
             ])
        path = A_star(background.genrate_maze(), background.start, background.end, background)
        # game(background.genrate_maze())
        if model == "graph2-1":
            # ======================test2============================
            # 单向
            print(background.genrate_maze())
            grid_sol_single = path.a_star_single_direction()
            print(grid_sol_single)
            game(background.genrate_maze(),grid_sol_single,background.start,background.end)

        elif model == "graph2-2":
            #双向
            path_1,path_2 = path.a_star_double_direction()
            print(path_1)
            print(path_2)
            game2(background.genrate_maze(),path_1,path_2,background.start,background.end)
            # ======================test2============================


