import datetime

year = 2017
first_day_of_year = datetime.date.min.replace(year = year).strftime('%d.%m.%Y')
last_day_of_year = datetime.date.max.replace(year = year).strftime('%d.%m.%Y')

print(first_day_of_year,last_day_of_year)
# print(first_day_of_year.strftime('%d.%m.%Y'),last_day_of_year.strftime('%d.%m.%Y'))

