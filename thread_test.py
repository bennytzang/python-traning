import threading
import time

'''
#定義子執行緒工作函數
def job(num):
    print("Thread", num)
    time.sleep(1)

'''
# 子執行緒類別
class MyThread(threading.Thread):
  def __init__(self, num):
    threading.Thread.__init__(self)
    self.num = num

  def run(self):
    print("Thread", self.num)
    time.sleep(1)


#建立執行緒
threads = []
for i in range(5):
    #threads.append(threading.Thread(target = job, args = (i,)))
    threads.append(MyThread(i))
    threads[i].start()

#主執行緒繼續執行自己的工作
#...
for i in range(3):
    print("Main thread:", i)
    time.sleep(1)

#等待所有子執行緒結束
for i in range(5):
    threads[i].join()

print("Done.")