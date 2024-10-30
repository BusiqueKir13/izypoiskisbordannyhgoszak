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

from pandas import DataFrame

#Задача 2.1: после формирования ссылки, которая работает - скачиваем html страницу для дальнейшего его парсинга
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"]
# Выбор случайной строки user agent
user_agent = random.choice(user_agents)
# Указываем user agent в заголовках запроса перед выполнением запроса
headers = {
    "Accept": "*/*", "User-Agent": user_agent}
# dataikz = f"content/№ 0331100013520000001.html",


with open(f"content/0_№ 0331100013520000001.html", encoding="utf-8") as file:
    rsinn=file.read()

soup = BeautifulSoup(rsinn, "lxml")


#Берем информацию о способе закупки
typeprosurement = soup.find("span",{'class': "cardMainInfo__title distancedText ml-1"})
for prosurement in typeprosurement:
    tpprosurement = prosurement.text.strip(' \n\t')
#Берем информацию об объекте закупки
nameprosure= soup.find("span", {'class': "cardMainInfo__content"})
for namis in nameprosure:
    obj = namis.text.strip(' \n\t')
#Берем информацию о НМЦК закупки
maxprice= soup.find("span",{'class':"cardMainInfo__content cost"})
for prices in maxprice:
    nmc = prices.text.strip(' \n\t')
#Дата публикации
datestart= soup.find("div", {'class': "cardMainInfo__section col-6"})
date1=datestart.find("span", {"class": "cardMainInfo__content"})
for dating in date1:
    dt1=dating.text.strip(' \n\t')
#Дата окончания подачи заявок
datefinish = soup.find("div", {'class': "date"})
date2 = datefinish.find_all('span',{'class':"cardMainInfo__content"})[2]
dt2=date2.text.strip(' \n\t')


#Дата аукциона
    # datetender = soup.find("div", {'class': "col"})
    # dattend = datetender.find_all('section', {'class': "blockInfo__section"})
    # dat3 = dattend.find_all('span', {'class': "section__info"})[2]
    # dt3=dat3.text.strip(' \n\t')
#ОКПД2 закупки
okpd = soup.find_all("td", {'class':"tableBlock__col"})[1].text.strip(' \n\t')
# for typeval in typevalue:
#     okpd=typeval.text.strip(' \n\t')

#СМП да или нет


#Формирует таблицу для сбора данных из файла страницы

table: DataFrame = pd.DataFrame({
    "Способ закупки":[tpprosurement],
    "Предмет закупки": [obj],
    "НМЦК":[nmc.strip(' ')],
    "Дата публикации":[dt1],
    "Окончание подачи заявок":[dt2],
    "ОКПД2":[okpd]
                    })
pd.set_option('display.max_columns', None)
# print(f"{tpprosurement}: {obj}: {nmc}: {dt1}: {dt2}:{okpd}")
# print(okpd)
print(table)