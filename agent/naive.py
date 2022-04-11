# tag::randombotimports[]
import random
from agent.base import Agent# 从文件agent.base。py中导入类Agent（也可以是方法，变量）
#也可以写成 import agent.base ，区别是使用时必须 这样用 a=Agent()改成a= agent.base.Agent
from agent.helpers import is_point_an_eye
from goboard_slow import Move
from gotypes import Point
# end::randombotimports[]


__all__ = ['RandomBot']


# tag::random_bot[]
class RandomBot(Agent):
    def select_move(self, game_state):
        """Choose a random valid move that preserves our own eyes."""
        candidates = []
        for r in range(1, game_state.board.num_rows + 1):
            for c in range(1, game_state.board.num_cols + 1):
                candidate = Point(row=r, col=c)
                if game_state.is_valid_move(Move.play(candidate)) and \
                        not is_point_an_eye(game_state.board,
                                            candidate,
                                            game_state.next_player):
                    candidates.append(candidate)
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))
# end::random_bot[]