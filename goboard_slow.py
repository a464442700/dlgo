

class GoString():
    def __init__(self, color, stones, liberties):
        self.color = color#当前棋链的颜色
        self.stones = set(stones)#棋链的棋子坐标集合
        self.liberties = set(liberties)#气也是坐标，棋链的气的坐标集合

    def remove_liberty(self, point):
        self.liberties.remove(point)#移除一个气？

    def add_liberty(self, point):
        self.liberties.add(point)#增加一个气坐标？

    def merged_with(self, go_string):  # <2>
        assert go_string.color == self.color#assert表示断言，false直接raise例外
        combined_stones = self.stones | go_string.stones#合并棋链，棋链中的棋子求并集
        return GoString(
            self.color,
            combined_stones,
            (self.liberties | go_string.liberties) - combined_stones)#气求并集再求差集

    @property
    def num_liberties(self):
        return len(self.liberties)

    def __eq__(self, other):
        return isinstance(other, GoString) and \
               self.color == other.color and \
               self.stones == other.stones and \
               self.liberties == other.liberties