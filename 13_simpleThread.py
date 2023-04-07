##Older way or manual way compare to concurrent.futures
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

""" 
t1 = threading.Thread(target=do_something, args=[1])
t2 = threading.Thread(target=do_something, args=[1])

t1.start()
t2.start()

t1.join()
t2.join()

#OR below in loop
"""
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()    #this join we use to wait next code execution until it finished the process started otherwise it will execute whole code before finishing started process

finish = time.perf_counter()

print(f'Finished in {finish-start} seconds')