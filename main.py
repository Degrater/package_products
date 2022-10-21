import sys
from config import *
from multiprocessing import connection
import pymysql


print("Менеджер товаров\nДля добавления товара введите-1,\nДля поиска товара введите-2\nДля просмотра всего каталога введите-3\nДля остановки введите 0. Удачи")
number=int(input("> "))

while number != 0:
    if number == 1:     
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
            try:
                tovar_name = input("Введите название товара:\n> ")
                tovar_price = int(input("Введите стоимость:\n> "))
                tovar_code = int(input("Введите код товара:\n> "))
                print(f" Вы отправили товар -> Название: {tovar_name}  \nЦена:{tovar_price}$ \nКод товара: {tovar_code}")
                with connection.cursor() as cursor:
                    inf_answer = f"INSERT INTO buy_type VALUES ('{tovar_name}', {tovar_price} , {tovar_code} );"
                    cursor.execute(inf_answer)
                    print("Товар добавлен")
                number = int(input("Для продолжения введите-1\nДля остановки введите 0.\n> "))
            finally:
                connection.close()
        except:
            print("Что-то пошло не так(((")
            sys.exit()
    if number == 2:
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
                )
            try:
                search_name = input("Введите название товара:\n> ")
                with connection.cursor() as cursor:
                    inf_answer0 = f"SELECT * from buy_type WHERE buy_name='{search_name}';"
                    cursor.execute(inf_answer0)
                    print(cursor.fetchone())
                    number = int(input("Для продолжения введите-1\nДля остановки введите 0.\n> "))
            finally:
                connection.close()
        except:
            print("Что-то пошло не так(((")
            sys.exit()
