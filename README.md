# Веб-скреппинг информации с сайта onebook.ru
Проект по веб-скреппингу информации с сайта onebook.ru. 
Это сайт типографии One Book, выпускающей книги на заказ. Стоимость заказа можно рассчитать на данном [онлайн-калькуляторе с сайта.](https://www.onebook.ru/help/calculators/)

Цель проекта - сбор данных о стоимости заказов на печать.
Собираемые данные (признаковое описание заказа):
1) Тип обложки
    * Твердый
    * Мягкий
2) Формат
    * А4
    * А5
3) Выборочный лак
    * Да
    * Нет
4) Скрепление блока
    * Клеевое
    * Сшитое
5) Цветность блока
    * Черно-белый
    * Цветной
6) Печать на экобумаге
    * Да
    * Нет
7) Количество книг
    * Принимает значения в диапазоне от 1 до 150 
8) Количество страниц в одной книге
    * Принимает значения в диапазоне от 20 до 1000
9) Цена за заказ (рублях)
    * Может быть целевой (зависимой) переменной при исследовании набора 

Количество комбинаций значений всех категориальных признаков - 64. Количество книг бралось в диапазоне от 1 до 150 с шагом 5. Количество страниц бралось в диапазоне от 20 до 1000 с шагом 5. 
Данные собраны в xlsx файл. Для скачивания набора данных можно воспользоваться ссылкой:  https://github.com/george101010/Prices-for-printing-orders-at-One-Book/blob/85d30ad31ed1b0ebc1d17af0035d558769af8934/Data/one_book_prices.xlsx

Сбор данных произведён с применением библиотеки Python Selenium. Сбор данных производился в несколько параллельных потоков.
