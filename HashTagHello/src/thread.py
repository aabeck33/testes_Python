'''
    Threads in Python
    https://realpython.com/intro-to-python-threading/
    https://www.pythontutorial.net/python-concurrency/python-threading/
'''
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep((name + 1) * 20)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    start_time = time.perf_counter()
    logging.info("Main    : before creating thread")
    threads_list = list() # list() ou []
    for i in range(1,4):
        logging.info("Main    : creating and starting thread %d.", i)
        x = threading.Thread(target=thread_function, args=(i,), daemon=False)
        # logging.info(f"Main    : before running thread {i}")
        threads_list.append(x)
        x.start()
    logging.info("Main    : wait for the thread(s) to finish")
### If you want to wait for the thread to complete in the main thread, you can call the join() method.
    # x.join()
    '''
    for index, thread in enumerate(threads_list):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    '''
    print(threads_list)
    end_time = time.perf_counter()
    logging.info("Main    : all done")