# # подключаем urlopen из модуля urllib
import os
import datetime  #импортируем возможность устанавливать дату
# # подключаем библиотеку BeautifulSoup и request
from urllib.request import urlopen
import urllib.request
import json
import re
import pandas as pd
from pandas import DataFrame
import requests
# подключаем библиотеку BeautifulSoup
from bs4 import BeautifulSoup

import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"]
# Выбор случайной строки user agent
user_agent = random.choice(user_agents)
# Указываем user agent в заголовках запроса перед выполнением запроса
headers = {"Accept": "*/*", "User-Agent": user_agent}

url = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=0331100013522000004'
req=requests.get(url, headers=headers)
souping =req.text
soup = BeautifulSoup(souping, "lxml")
#собираем все данные с результатов, которые необходимы

amountprocure = soup.find_all('tr', {'class': 'tableBlock__row'})
customeramount = soup.find('td', {'class': 'tableBlock__col'})
for cosa in customeramount:
     ca = cosa.text.strip('\n\t')

pricecontract = soup.find_all('td',{'class':"tableBlock__col"})[3]
for pc in pricecontract:
    pc1 = pc.text.strip('\n\t')

winnerprocure = soup.find_all('td', {'class': 'tableBlock__col'})[9]
for win in winnerprocure:
    wp1 = win.text.strip('\n\t')
table: DataFrame = pd.DataFrame({
    "Заказчик":[ca],
    "Предмет закупки": [''],
    "Цена контракта":[pc1],
    "Количество участников":[''],
    "Победитель":[wp1],
    "Сслыка на контракт":['']
                    })
pd.set_option('display.max_columns', None)

print('Вот что у нас получается...')
# print(amountprocure)
print(ca)
print(table)
# print(winnerprocure)


