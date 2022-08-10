
# в данном модуле содержатся функции для скрепинга

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xpaths_ import x_paths_
from table_vals import *
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from tqdm import tqdm

# модуль xpaths_ содержит х-пути для радио-баттонов
# модуль table_vals  содержит значения для заполнения таблицы после крепинга

# функция получения цены
def get_price(driver):
    price = driver.find_element(By.CLASS_NAME, "js-order-price").get_attribute('innerHTML').replace('&nbsp;', '')
    return int(price)

# функция ввода количества страниц
def enter_number_pages(driver, Number ):
    wait = W(driver, 1)


    try:
        Element = wait.until(E.presence_of_element_located( (By.NAME, "CALC_PAGE") ))
        Element.send_keys(Keys.CONTROL + "a")
        Element.send_keys( Number )
    except:
        time.sleep(7)
        Element = wait.until(E.presence_of_element_located( (By.NAME, "CALC_PAGE") ))
        Element.send_keys(Keys.CONTROL + "a")
        Element.send_keys( Number )
    return None

# функция ввода количества книг
def enter_number_books( driver, Number ):
    wait = W(driver, 5)
    try:

        Element = wait.until(E.presence_of_element_located( (By.NAME, "CALC_BOOK") ))
        Element.send_keys(Keys.CONTROL + "a")
        Element.send_keys( Number )
    except:
        time.sleep(7)
        Element = wait.until(E.presence_of_element_located( (By.NAME, "CALC_BOOK") ))
        Element.send_keys(Keys.CONTROL + "a")
        Element.send_keys( Number )
    return None

# функция выбора заданных параметров (radio_buttons)
# задана комбинация 6 параметров (битовая строка), функция выбирает нужные радио-баттоны
def set_combination( driver, bit_string_ ):
    wait = W(driver , 3)
    for Num , i in enumerate( bit_string_ ) :
        #time.sleep(0.7)
        try:
            time.sleep(3)
            radio_button = wait.until(E.element_to_be_clickable( (By.XPATH, x_paths_[Num ][ i ] ) ) )


            radio_button.click()
        except:
            time.sleep(6)
            radio_button = wait.until(E.element_to_be_clickable( (By.XPATH, x_paths_[Num ][ i ] ) ) )


            radio_button.click()
    return None

# функция инициализации веб-драйвера и перехода на нужный сайт
def create_driver( ):
    URL = "https://www.onebook.ru/help/calculators/"

    driver = webdriver.Chrome( service = Service( ChromeDriverManager().install() ) )
    driver.maximize_window()
    driver.get( URL )
    driver.execute_script("""
   var l = document.getElementsByClassName("header")[0];
   l.parentNode.removeChild(l);
    """)
    time.sleep(3)
    return driver

# функция скрепинга информации с сайта
# на вход подается драйвер driver с открытым сайтом и массив чисел Numbers_,
# которые конвертируются в битовую строку -
# положение радиобаттонов на сайте
def scrap_inf( Numbers_ , driver):

    pages = [ i for i in range(20 , 1001,20 ) ]
    books = [1]+[ i for i in range(5 , 151,5 ) ]

    for Nb in tqdm(Numbers_):
        chs = bin(Nb)[2:]
        bit_string =   [0]* (6 - len(chs)) + list(map( int, list(chs)   ) )

        TABLE = []

        set_combination(driver, bit_string )
        TABLE_ITEM1 = [ column_vals_[P][ bit_string[P] ] for P in  range(6) ]

        for J in books:


            TABLE_ITEM2 = TABLE_ITEM1 + [J]
            enter_number_books(driver,  J )
            for K in  pages :

                time.sleep(0.1)
                enter_number_pages(driver, K )
                time.sleep(0.1)
                pr = get_price(driver)

                TABLE_ITEM3 = TABLE_ITEM2 + [K , pr]
                TABLE.append(TABLE_ITEM3)

        DATA = pd.DataFrame(TABLE, columns=columns_categ)
        DATA.to_csv('scraped_data\data'+str(Nb)+'.csv', sep=';', index=False)

    return None