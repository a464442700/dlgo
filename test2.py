from multiprocessing import Process
import os
from dlgo.pygui_draw import Draw

def myProcess(*name):
    print("传入的name有：",name)
    print("os.getpid():",os.getpid())
if __name__ == "__main__":
    p = Process(target=Draw,args=(40,))
    p.start()
    print("p.pid:",p.pid)
    Draw.draw_borad()