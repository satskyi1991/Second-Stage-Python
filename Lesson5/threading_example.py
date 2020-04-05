import time
from threading import Thread
from multiprocessing import Process

def sleeping(time_to_sleep):
    time.sleep(time_to_sleep)
    print('I`v wake up')

# start = time.time()
# sleeping(2)
# sleeping(3)

# print(time.time() - start)
#
# t = Thread(target=sleeping, args=(4,))
# t2 = Thread(target=sleeping, args=(5, ))
#
# start = time.time()
# t.start()
# t2.start()
# t.join()
# t2.join()
# print(f' {time.time() - start}')
#


def calculate(n):
    a = []
    for i in range(n):
        a.append(i)



start = time.time()
calculate(1000000)
calculate(1000000)
print(f'{time.time() - start}')

t = Process(target=calculate, args=(1000000,))
t2 = Process(target=calculate, args=(1000000,))

start = time.time()
t.start()
t2.start()
t.join()
t2.join()
print(f'{time.time() - start}')

threads = []

# for i in range(100):
#
#     t = Thread(target=time.sleep, args=(i,), daemon=T)
#     threads.append(t)


list_of_threads = [Thread(target=time.sleep, args=(i, )) for i in range(100)]

for thread in list_of_threads:
    thread.start()

#time.sleep(5)
# for thread in list_of_threads:
#     print(thread.is_alive())


a = []
def calculate(i):
    global a
    a.append(i)


list_of_threads = [Thread(target=calculate, args=(i, )) for i in range(10000)]
for thread in list_of_threads:
    thread.start()
time.sleep(1)

print(a)


class MyThread(Thread):

    def __init__(self, is_daemon):
        super().__init__(daemon=is_daemon)
        self.result = None

    def run(self):
        time.sleep(3)
        self.result = 3




a = MyThread(False)
a.start()
a.join()
print(a.result)
