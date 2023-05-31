

import time
import threading
def gf(n):
    for i in range(n):
        print("I am talking with gf")
        time.sleep(2)

def exgf(n):
    for i in range(n):
        print("Exgf is talking")
        time.sleep(2)

t1=time.time()
gf=threading.Thread(target=gf,args=(5,),name="samantha")
exgf=threading.Thread(target=exgf,args=(5,),name="rashmika")
gf.start()
exgf.start()
print('no of active threads are',threading.active_count())
print(threading.enumerate())
gf.join()
exgf.join()
print('gf is active or not',gf.is_alive())
t2=time.time()
print("Time Taken: ",t2-t1)