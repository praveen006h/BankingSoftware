import pyautogui as pg 
import time


from multiprocessing import Pool
from multiprocessing import cpu_count

def clickr(a):
    while True:
        pg.click()


if __name__ == '__main__':
    processes = cpu_count()
    pool = Pool(processes)
    pool.map(clickr,range(processes) )