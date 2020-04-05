from threading import Thread
import time

t = Thread(target=time.sleep, args=(30, ), daemon=True)
t.start()
