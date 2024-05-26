import _thread               # baixo nível
from threading import Thread # alto ńível
import time


# Implementação de fibonaci ineficiente usando função recusrsiva
def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    return fib(n - 1) + fib(n - 2)


def test_fib(n):
    return print('Fib %d: %d' %(n, fib(n)))


def run_fibs():
    test_fib(35)
    test_fib(10)
    test_fib(30)


#run_fibs()
#run_fibs_with_threads()


# Usando _thread
def run_fibs_with_threads():
    _thread.start_new_thread(test_fib, (35, ))
    _thread.start_new_thread(test_fib, (10, ))
    _thread.start_new_thread(test_fib, (30, ))
    time.sleep(15)

"""
for i in range(0, 36, 5):
    t = Thread(target=test_fib, args=(i, ))
    t.start()
"""
for i in (35, 10, 30):
    t = Thread(target=test_fib, args=(i, ))
    t.start()