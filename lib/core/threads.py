import threading
import time


def run_threads(num_threads, function):
    threads = []
    # 启动多个线程
    for num_threads in range(num_threads):
        thread = threading.Thread(target=function, name=str(num_threads))
        thread.setDaemon(True)
        try:
            thread.start()
        except Exception as ex:
            err_msg = "error occurred while starting new thread ('{0}')".format(str(ex))
            print(err_msg)
            break
        threads.append(thread)

    # 等待所有线程完毕
    # 取代join来阻塞线程，避免ctrl+C无法退出
    alive = True
    while alive:
        alive = False
        for thread in threads:
            if thread.isAlive():
                alive = True
                time.sleep(0.1)