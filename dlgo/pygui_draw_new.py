import pygame
import math
from dlgo.gotypes import  Player,Point
import time
from multiprocessing import Process, Queue
from pygame.locals import QUIT
import sys
class Draw(Process):

    def __init__(self,af,queue):
        self.af=af#缩放因子
        self.board_size=19
        self.long_size = self.board_size * af
        self.wide_size = self.board_size * af
        self.gride_size = af
        self.star_radiu = af / 40 * 8
        self.screen_color = [238, 154, 73]  # 设置画布颜色,[238,154,73]对应为棕黄色
        self.line_color = [0, 0, 0]  # 设置线条颜色，[0,0,0]对应黑色
        self.black=[0,0,0]
        self.white=[255,255,255]


        # while True:  # 不断训练刷新画布
        #     for event in pygame.event.get():  # 获取事件，如果鼠标点击右上角关闭按钮，关闭
        #         if event.type== QUIT:
        #             sys.exit()
    def draw_borad(self):
        for i in range(self.gride_size, self.long_size + self.gride_size, self.gride_size):
            if (i == self.gride_size or i == self.long_size):
                pygame.draw.line(self.screen, self.line_color, (self.gride_size, i), (self.long_size, i), 4)
                pygame.draw.line(self.screen, self.line_color, (i, self.gride_size), (i, self.long_size), 4)
            pygame.draw.line(self.screen, self.line_color, (self.gride_size, i), (self.long_size, i), 2)
            pygame.draw.line(self.screen, self.line_color, (i, self.gride_size), (i, self.long_size), 2)
        # 画星位
        for i in range(3, 21, 6):
            for j in range(3, 21, 6):
                pygame.draw.circle(self.screen, self.line_color, ((i + 1) * self.gride_size, (j + 1) * self.gride_size), self.star_radiu, 0)
        pygame.display.update()

    def draw_point(self, player,point):
        if player==Player.black:
            color= self.black
        elif player==Player.white:
            color = self.black

        (x, y) = (point.row,point.col)
        pieces_radio = math.ceil(self.af / 5 * 2)
        pygame.draw.circle(self.screen, color, (x * self.af, y * self.af), pieces_radio, 0)


    def is_in_circle(self,x, y, row, col, r):
        if (x - row * self.af) ** 2 + (y - col * self.af) ** 2 <= r ** 2:
            return True
        return False

    def get_point(self,x, y):
        # x y 是坐标
        # 如果坐标位于以math.ceil(af/5*2) 为半径的园内，返回其坐标
        # 先获取大概的位置
        row, col = (0, 0)
        srow = math.floor(x / self.af)
        erow = srow + 1
        scol = math.floor(y /  self.af)
        ecol = scol + 1
        pieces_radio = math.ceil( self.af / 5 * 2)
        # 依次求这四个点，判断位于哪个点上
        # print(srow,erow)
        for i in (srow, erow):
            for j in (scol, ecol):
                # print(i,j,x,y,pieces_radio)
                if self.is_in_circle(x, y, i, j, pieces_radio):
                    (row, col) = (i, j)
                    break
        if (row >= 1 and row <= 19 and col <= 19):
            return (row, col)
        else:
            return None
    def run(self):
        #画棋盘
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.long_size + 2 * self.board_size, self.wide_size + 2 * self.board_size))
        self.screen.fill(self.screen_color)
        self.draw_borad()
        pygame.display.update()
        #test start


        #test end

        while True:  # 不断训练刷新画布

            for event in pygame.event.get():  # 获取事件，如果鼠标点击右上角关闭按钮，关闭
                if event.type in (QUIT,):
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if self.get_point(x, y) is not None:
                        row, col = self.get_point(x, y)
                        print(row, col)
                        point = Point(row=row, col=col)
                        self.draw_point( Player.black, point)
                        pygame.display.update()

if __name__ == "__main__":
    queue = Queue()
    display_go=Draw(40,queue)
    display_go.run()