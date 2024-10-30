# # подключаем urlopen из модуля urllib
import os
import datetime  #импортируем возможность устанавливать дату
# # подключаем библиотеку BeautifulSoup и request
from urllib.request import urlopen
import urllib.request
import json
import re
import pandas as pd
import requests
# подключаем библиотеку BeautifulSoup
from bs4 import BeautifulSoup
import random


# Задача - создать таблицу, куда будут добавлять данные

table = pd.DataFrame({
                    'Заказчик': [1,2,3],
                    'Способ закупки':[1,2,3],
                    'Заказчик':[1,2,3],
                    'Тип закупки':[1,2,3],
                    'Предмет закупки':[1,2,3],
                    'НМЦК':[1,2,3],
                    'Цена контракта':[1,2,3],
                    'Количество заявок':[1,2,3],
                    'Экономия':[1,2,3],
                    'Дата публикации':[1,2,3],
                    'Дата окончания подачи заявок':[1,2,3],
                    'Дата аукциона':[1,2,3],
                    'Дата итогового протокола':[1,2,3],
                    'Дата заключения контракта':[1,2,3]
                      })

procedure_number = []
customer = []
method_of_conducting = []
date_of_placement = []
end_date = []
nmc = []
electronic_platform = []
data_samples = []
data_analogs = []
data_delivery_time = []
data_payment_time = []
data_divisibility = []
data_address = []
data_support = []
data_url = []


data_dict = {'Номер процедуры': procedure_number,
             'Заказчик': customer,
             'Способ проведения': method_of_conducting,
             'Дата размещения': date_of_placement,
             'Дата окончания подачи заявок': end_date,
             'НМЦ': nmc,
             'Электронная площадка': electronic_platform,
             'Образцы': data_samples,
             'Аналоги': data_analogs,
             'Срок поставки': data_delivery_time,
             'Срок оплаты': data_payment_time,
             'Делимость': data_divisibility,
             'Адрес': data_address,
             'Обеспечение': data_support,
             'Ссылка': data_url}





print(table)
print(data_dict)