import time

from dlgo import agent
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move  # point_from_coords
# from six.moves import input
from dlgo.pygui_draw_new_2 import Draw
from multiprocessing import Process, Queue
from dlgo.agent import naive
from dlgo.gotypes import Player, Point


def main():
    board_size = 4
    game = goboard.GameState.new_game(board_size)
    # bot = agent.RandomBot()
    bot = naive.RandomBot()
    bot_queue = Queue()
    human_queue = Queue()
    player_queue = Queue()
    grid_queue = Queue()
    display_go = Draw(40, board_size, bot_queue, human_queue, player_queue, grid_queue)
    display_go.start()
    # print(game.next_player)
    # print(game.next_player)
    while not game.is_over():
        print_board(game.board)
        # print(game.board)
        # if game.board._grid != None:
        #     for key,value in game.board._grid.items():
        #         print(key,value)
        #         print(value.color)
        player = game.next_player
        # print("当前人", player)
        if player == gotypes.Player.black:
            # human_move = input('-- ')
            # point = point_from_coords(human_move.strip())
            # point=鼠标点击
            player_queue.put(player)
            while True:

                if not human_queue.empty():
                    humanplayer, move = human_queue.get()
                    # print('humanplayer', humanplayer)
                    point = move.point
                    # point=Point(move.point.col,move.point.row)
                    # point.row=move.point.col
                    # point.col=move.point.row
                    # print(point)
                    #   if game.board.is_on_grid(point) and game.board._grid.get(point):
                    #    continue
                    if move.is_pass:
                        break
                    if move.is_resign:
                        return
                    if move.point:
                        move = goboard.Move.play(point)
                        # 这个可以验证该位置未落子，自吃，重复下
                        if game.is_valid_move(move):  # 未添加is_point_an_eye，表示人类选手可以填补眼
                            break

                    # print('move:', move.is_play)

            #
        else:
            # print('else')
            # time.sleep(100)
            move = bot.select_move(game)
            player_queue.put(player)
            bot_queue.put((player, move))
        # print('movemove:', move.point)

        game = game.apply_move(move)
        grid_queue.put(game.board._grid)
        #print(game.board._grid)  # 打印棋子
        #数目法求子
        for key, value in game.board._grid.items():



            # print('------start-----')
            # print(key, value)
            # print(value.color)
            # print('value.liberties:',len(value.liberties))
            # print('value.stones:',value.stones)
            # print('-------end----')
        # print('game.is_over():',game.is_over())


if __name__ == '__main__':
    main()
