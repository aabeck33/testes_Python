'''
    https://www.youtube.com/watch?v=qRFPGuBc-KE
'''

import time
from tqdm import tqdm

for i in tqdm(range (20)):
    time.sleep(1)

with tqdm(total=20) as my_bar:
    for i in tqdm(range (20)):
        time.sleep(1)
        my_bar.update(5)