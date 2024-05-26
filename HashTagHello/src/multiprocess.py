'''
    Multiprocessos
    https://data-flair.training/blogs/python-multiprocessing/
    https://pymotw.com/2/multiprocessing/basics.html
    https://www.digitalocean.com/community/tutorials/python-multiprocessing-example
    --
    https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/
    https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
    https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/
    --
    joblib: https://www.youtube.com/watch?v=maj47xd_R7g
'''

import multiprocessing
import time
from joblib import Parallel, delayed

from tqdm import tqdm

def spawn(num):
    # print(num+1)
    time.sleep((num + 1) * 1)
    # print(num)
    return num

if __name__ == '__main__':
    '''
    for i in range(25):
        ## right here
        p = multiprocessing.Process(target=spawn, args=(i,), daemon=False)
        p.start()
        ## p.join()
    print(f'Processadores na máquina: {multiprocessing.cpu_count()}')
'''
    resultado = Parallel(n_jobs=8)(delayed(spawn)(i) for i in tqdm(range(25)))
    print(resultado)