from methods_for_page import *
from datetime import datetime
from  concurrent.futures import  ThreadPoolExecutor

# переход на сайт

drivers = [create_driver() for _ in range(4)]


chunks = [  list(range(32, 40)),
            list(range(40 , 48)),
            list(range( 48 , 56)),
            list(range( 56,64))
           ]

with ThreadPoolExecutor(max_workers=4) as executor:

    executor.map(scrap_inf , chunks, drivers)


[ dr.quit() for dr in drivers]
# закрытие сайта

