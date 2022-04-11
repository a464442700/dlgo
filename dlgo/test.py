from collections import namedtuple

class Point(namedtuple('Point', 'row col')):#namedtuple表示一个命名元组，类在括号里面，表示类的继承
    def __init__(self):
        assert False
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]
#p=Point(1,1)
#print(p.neighbors()[0].row)
#assert 1
#print(1^1^0)
a=1
a1=set()
a1.add(1)
a2=set([2])
a3=a1|a2
print(a3-a1)