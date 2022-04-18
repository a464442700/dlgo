#调用pygame库
import time

import pygame
import sys
import math
#调用常用关键字常量
from pygame.locals import QUIT,KEYDOWN

af=20#缩放因子
board_size=19#棋盘大小

#画点
def draw_point(screen,line_color,gride_size,point):
    (x,y)=point
    pieces_radio=math.ceil(af/5*2)
    pygame.draw.circle(screen, line_color, (x*af,y*af ), pieces_radio, 0)
def get_point(x,y):
    #x y 是坐标
    #如果坐标位于以math.ceil(af/5*2) 为半径的园内，返回其坐标
    #先获取大概的位置
    row,col=(0,0)
    srow=math.floor(x/af)
    erow=srow+1
    scol=math.floor(y/af)
    ecol=scol+1
    pieces_radio = math.ceil(af / 5 * 2)
    #依次求这四个点，判断位于哪个点上
    #print(srow,erow)
    for i in (srow,erow):
        for j in (scol,ecol):
            #print(i,j,x,y,pieces_radio)
            if is_in_circle(x,y,i,j,pieces_radio):
                (row,col)=(i,j)
                break
    if  (row >=1 and row <=19 and col <=19):
        return (row,col)
    else:
        return None



def draw_by_mouse(screen,line_color,gride_size):
    while True:  # 不断训练刷新画布

        for event in pygame.event.get():  # 获取事件，如果鼠标点击右上角关闭按钮，关闭
            if event.type in (QUIT, KEYDOWN):
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if get_point(x, y) is not None:
                    row, col = get_point(x, y)
                    print(row, col)
                    draw_point(screen, line_color, gride_size, (row, col))
                    pygame.display.update()

def is_in_circle(x,y,row,col,r):
    if (x-row*af)**2+(y-col*af)**2<= r**2:
        return True
    return False
def draw_board():
    long_size = board_size * af
    wide_size = board_size * af
    gride_size= af
    star_radiu=af/40*8
    screen_color = [238, 154, 73]  # 设置画布颜色,[238,154,73]对应为棕黄色
    line_color = [0, 0, 0]  # 设置线条颜色，[0,0,0]对应黑色

    pygame.init()

    # 获取对显示系统的访问，并创建一个窗口screen
    # 窗口大小为670x670
    screen = pygame.display.set_mode((long_size+2*board_size, wide_size+2*board_size))
    screen.fill(screen_color)  # 填充颜色
    pygame.display.update()
    while True:
        pass
    for i in range(gride_size, long_size + gride_size, gride_size):
        if (i == gride_size or i == long_size):
            pygame.draw.line(screen, line_color, (gride_size, i), (long_size, i), 4)
            pygame.draw.line(screen, line_color, (i, gride_size), (i, long_size), 4)
        pygame.draw.line(screen, line_color, (gride_size, i), (long_size, i), 2)
        pygame.draw.line(screen, line_color, (i, gride_size), (i, long_size), 2)
    # 画星位
    for i in range(3, 21, 6):
        for j in range(3, 21, 6):
            pygame.draw.circle(screen, line_color, ((i + 1) * gride_size, (j + 1) * gride_size), star_radiu, 0)
    pygame.display.update()

    draw_by_mouse(screen,line_color,gride_size)

        #画线


        #draw_point(screen, line_color,gride_size,(1,1))

        #keys_pressed = pygame.mouse.get_pressed()

        # if keys_pressed[0]:
        #     x, y = pygame.mouse.get_pos()
        #     print(x, y, get_point(x, y))
        #print(x,y)
          # 刷新显示

if __name__   =='__main__':
    draw_board()
