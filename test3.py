
from multiprocessing import Process, Queue
class ReadProcess(Process):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while not self.queue.empty():
            result = self.queue.get()
            print("读入的数据是：", result)
            if result==10:
                pass
                #exit()

class WriteProcess(Process):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()
    def run(self):
        i = 0
        while not self.queue.full():
            i = i + 1
            self.queue.put(i)
            print("写入的数据是：", i)
            if i== 10:
                exit()


if __name__ == "__main__":
    queue = Queue()
    w = ReadProcess(queue)
    r = WriteProcess(queue)
    r.start()
    w.run()
    print("继续执行")

