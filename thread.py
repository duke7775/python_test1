#功能：线程

import threading

def thread_func(args):
    thread_index = args[0]
    thread_id = threading.current_thread().ident

#打印0到9
    for i in range(10):
        print(f"Thread {thread_index} ID: {thread_id}, {i}   ")


#创建三个线程
def run_threads():
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_func, args=((i,),))
        threads.append(t)
    for t in threads:
        t.start()

run_threads()
