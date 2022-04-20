from __future__ import print_function
# tag::bot_vs_bot[]
from dlgo.agent import naive
from dlgo import goboard_slow
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time
from dlgo.pygui_draw_new import Draw
from multiprocessing import Process, Queue

def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
         gotypes.Player.black: naive.RandomBot(),
         gotypes.Player.white: naive.RandomBot(),
    }
    #新开进程程输出画面
    queue = Queue()
    display_go = Draw(40, board_size,queue)
    display_go.start()

    while not game.is_over():
        #time.sleep(0.3)  # <1>


        print_board(game.board)

        bot_move = bots[game.next_player].select_move(game)
        player=game.next_player
        print_move(player, bot_move)
        #将信息输入队列
        if not queue.full():
            queue.put((player, bot_move))



        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()