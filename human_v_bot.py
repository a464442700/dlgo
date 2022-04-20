import time

from dlgo import agent
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move# point_from_coords
#from six.moves import input
from dlgo.pygui_draw_new import Draw
from multiprocessing import Process, Queue
from dlgo.agent import naive
def main():
 board_size = 9
 game = goboard.GameState.new_game(board_size)
 #bot = agent.RandomBot()
 bot=naive.RandomBot()
 bot_queue = Queue()
 human_queue=Queue()
 player_queue=Queue()
 display_go = Draw(40, board_size,bot_queue,human_queue,player_queue)
 display_go.start()
 print(game.next_player)
 print(game.next_player)
 while not game.is_over():
  print_board(game.board)
  player = game.next_player
  print("当前人",player)
  if player == gotypes.Player.black:
   #human_move = input('-- ')
   #point = point_from_coords(human_move.strip())
   #point=鼠标点击
   player_queue.put(player)
   while True :
    if not human_queue.empty():
     humanplayer, move = human_queue.get()
     print('humanplayer',humanplayer)
     point=move.point
     print(point)
     move = goboard.Move.play(point)
     print('move:',move.is_play)
     break

   #
  else:
    print('else')
    #time.sleep(100)
    move = bot.select_move(game)
    player_queue.put(player)
    bot_queue.put((player, move))
  print('movemove:',move.point)
  game = game.apply_move(move)
if __name__ == '__main__':
  main()