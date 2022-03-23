
import enum
from collections import namedtuple
# end::namedtuple[]
__all__ = [
    'Player',
    'Point',
]

class Player(enum.Enum):#Enum表示枚举类
    black = 1
    white = 2
    @property #property装饰器，如果没有@other.setter则只可读
    def other(self):
        return Player.black if self == Player.white else Player.white #return a if ture else return b


class Point(namedtuple('Point', 'row col')):#namedtuple表示一个命名元组，类在括号里面，表示类的继承
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]


    def __deepcopy__(self, memodict={}):
        # These are very immutable.
        return self