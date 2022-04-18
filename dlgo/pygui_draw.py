import pygame
import math
from dlgo.gotypes import  Player
class Draw():

    def __init__(self,af):
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
        pygame.init()
        self.screen = pygame.display.set_mode((self.long_size + 2 * self.board_size, self.wide_size + 2 * self.board_size))
        self.screen.fill(self.screen_color)
        pygame.display.update()
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