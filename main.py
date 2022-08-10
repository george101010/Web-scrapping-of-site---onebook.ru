from methods_for_page import *
from datetime import datetime
from  concurrent.futures import  ThreadPoolExecutor

# инициализация 4 веб-драйверов, переходящих на нужный сайт

drivers = [create_driver() for _ in range(4)]

# задание для каждого веб драйвера. Числа преобразуются в битовую цепочку длиной 6
# каждая цепочка это - положение радио-баттонов на сайте
# для каждой комбинации производится скрепинг с разным числом книг и страниц
chunks = [  list(range(32, 40)),
            list(range(40 , 48)),
            list(range( 48 , 56)),
            list(range( 56,64))
           ]
# запуск процесса скрепинга в 4 потока
# функция scrap_inf содержится в модуле methods_for_page
with ThreadPoolExecutor(max_workers=4) as executor:

    executor.map(scrap_inf , chunks, drivers)

# закрытие всех драйверов
[ dr.quit() for dr in drivers]


