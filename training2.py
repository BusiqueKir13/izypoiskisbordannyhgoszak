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

from urllib3.filepost import writer

#
# from requests_html import AsyncHTMLSession
# from requests_html import HTMLSession
# from requests_html import HTMLResponse
# #старт программы

# Задача 1: Составление URL ссылок на основную страницу поиска

#старт программы
innedit = input("Введите ИНН:") # вводим инн организации
year_edit = input("Введите год:") # вводим дату за который должны выводится закупки организации
year = int(year_edit) #указываем год в будущем выбор из комбобокса
first_day_of_year = datetime.date.min.replace(year = year).strftime('%d.%m.%Y') #установка первой даты диапазона с которой будет уточняться закупки
last_day_of_year = datetime.date.max.replace(year = year).strftime('%d.%m.%Y') #установка последней даты диапазона с которой будет уточняться закупки + перевод в понимаемый сайтом формат оформления даты

#Составление УРЛ
#Составляем URL адрес на который будет заходить программа.
urlmain = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString="
urlprocure ="https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber=" # url-конструкция для того, чтобы посмотреть данные о закупке
urlamount ="https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=" # url- конструкция для того, чтобы посмотреть результаты торгов

search_inn = str(innedit) #указываем ИНН - в дальнейшем из строки ввода информации
morph_filter = "&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&" #установка фильтра для поиска
numberpage = "pageNumber=1&sortDirection=false&"
recordperpage = "recordsPerPage=_500" #установка максимального количества позиций отображаемых на странице
otherfilter = "&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz94=on&pc=on&currencyIdGeneral=-1&"
datefilter = "publishDateFrom="
daty = first_day_of_year
datefilter2 = "&publishDateTo="
dateto = last_day_of_year
yearfilter = datefilter+daty+datefilter2+dateto
filterset = morph_filter+numberpage+recordperpage+otherfilter
resultsearch = urlmain+search_inn+filterset+yearfilter
print(resultsearch) #отображаем результат - валидную url ссылку которая ведет на результат поиска
print('Создаем себе путь на все закупки за год от организации') # чтобы не было скучно

#Задача 2: Скачивание хтмл документа и формирования ссылок на процедуры - создание эксель файла и удаление файла хтмл после записи в эксель ссылок

my_file=open("valid_url.txt", "w+")
my_file.write(resultsearch)
my_file.close()
my_file = open("valid_url.txt")
file_contents = my_file.read()
my_file.close()
print('Вот что у нас получается...')
print(file_contents)

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
url=file_contents.strip()

req=requests.get(url, headers=headers)
rsinn=req.text
# print(rsinn)

with open("searchprocure.html", "w+", encoding="utf-8") as file:
    file.write(rsinn)

with open("searchprocure.html", encoding="utf-8") as file:
    rsinn=file.read()
#Задача 3 Получаем href ссылки на все закупки, их название, способ закупки, НМЦК, дату проведения закупки
soup = BeautifulSoup(rsinn,"lxml")
ikz_href = soup.find_all(class_="registry-entry__header-mid__number")
# ikz_href1 = soup.find_all(class_="registry-entry__header-mid__number")
allprocurement ={}
allamount ={}

for item in ikz_href:
    item_num = item.text.strip(' \n\t')
    item_num1 = item_num.replace("№ ","") #Эта операция позволяет скорректировать и подставить икз в ссылку
    item_ref1 = "https://zakupki.gov.ru"+item.find('a').get('href')
    item_ref2 = urlamount+item_num1
    allprocurement[item_num] = item_ref1
    allamount[item_num1] = item_ref2
    with open("allprocurement.json", "w") as file:
       json.dump(allprocurement, file, indent=4, ensure_ascii=False)
    with open("allamount.json", "w") as file:
       json.dump(allamount, file, indent=4, ensure_ascii=False)
    # with open("allamount.json") as file:
    #     json.load(file)
    # with open("allprocurement.json") as file:
    #     json.load(file)

#Задача 3.2  - формирование и поиск остальных данных
with open("allamount.json") as file:
    all_procures = json.load(file)

iteration_count = int(len(all_procures)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")

if count == 0:
            req = requests.get(url=item_ref1, headers=headers)
            src = req.text

            with open(f"content/{count}_{item_num}.html","w",encoding="utf-8") as file:
                file.write(src)

            with open(f"content/{count}_{item_num}.html","r", encoding="utf-8") as file:
                src=file.read()
                count += 1

count = 0
if count == 0:
    req = requests.get(url=item_ref2, headers=headers)
    src = req.text
    with open(f"content/{count}_{item_num1}.html", "w", encoding="utf-8") as file:
        file.write(src)
    with open(f"content/{count}_{item_num1}.html", "r", encoding="utf-8") as file:
        src = file.read()
        count =+1
    with open(f"data/{count}_{item_num}.json", "a", encoding="utf-8") as file:
        json.dump(item_num, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Итерация {count}. {item_num} записан...")
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Работа завершена")

#Задача 4 формирование таблицы в exel для сбора данных с ссылок
# table = pd.DataFrame({'Заказчик':[custname],
#                       'ИКЗ':[item_num],
#                       'УРЛ':[item_ref],
#                       'Объект закупки':[prsrmnt],
#                       'НМЦК':[price],
#                       'Дата публикации':[datepublic],
#                       'Дата окончания':[ending1],
#                       'Способ закупки':[mthd],
#                       })

dataprocure=urlprocure+item_num1

dataamount=urlamount+item_num1
print(item_num1)

print("ссылка на закупку")
print(dataprocure)

print("ссылка на результаты торгов")
print(dataamount)



#Задача 5 перенос необходимых данных с сайта в таблицу


# Задача 6 Расширение таблицы - расчет экономии средств, построение графиков, статистика

os.remove("valid_url.txt")








