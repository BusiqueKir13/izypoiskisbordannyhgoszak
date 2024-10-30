# # подключаем urlopen из модуля urllib
import os
import datetime  #импортируем возможность устанавливать дату
# # подключаем библиотеку BeautifulSoup и request
from urllib.request import urlopen
import urllib.request

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

headers = {
    "Accept": "*/*", "User-Agent": user_agent}





with open("searchprocure.html", encoding="utf-8") as file:
    rsinn=file.read()
#Задача 3 Получаем href ссылки на все закупки, их название, способ закупки, НМЦК, дату проведения закупки
soup = BeautifulSoup(rsinn,"lxml")
ikz_href = soup.find_all("div","registry-entry__header-mid__number")

for item in ikz_href:
    item_ikz = item.text
    item_href = item.get()

    print(f"{item_ikz}:{item_href}")

print(ikz_href)