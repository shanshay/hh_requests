import requests
import pprint

file = open("result_of_vacancies.txt", "w")

domain = 'https://api.hh.ru/'
url_vacancies = f'{domain}vacancies'
params_python_django = {
    'text': 'NAME:(Python AND developer) AND (Python AND Django AND Москва)'
}

result_python_django = requests.get(url_vacancies, params=params_python_django).json()
sum = 0
iter = 0
for items in range(len(result_python_django)):
    if result_python_django['items'][items]['salary'] == None:
        continue
    if result_python_django['items'][items]['salary']['from'] == None:
        sum = sum + result_python_django['items'][items]['salary']['to']
        iter = iter + 1
    else:
        sum = sum + result_python_django['items'][items]['salary']['from']
        iter = iter + 1
middle_salary_python_django = sum / iter

params_python_django_flask = {
    'text': 'NAME:(Python AND developer) AND (Python AND Django AND FLASK AND Москва)'
}

result_python_django_flask = requests.get(url_vacancies, params=params_python_django_flask).json()
sum = 0
iter = 0
for items in range(len(result_python_django_flask)):
    if result_python_django_flask['items'][items]['salary'] == None:
        continue
    if result_python_django_flask['items'][items]['salary']['from'] == None:
        sum = sum + result_python_django_flask['items'][items]['salary']['to']
        iter = iter + 1
    else:
        sum = sum + result_python_django_flask['items'][items]['salary']['from']
        iter = iter + 1
middle_salary_python_django_flask = sum / iter

params_python_sqlalchemy = {
    'text': 'NAME:(Python AND developer) AND (Python AND Sqlalchemy AND Москва)'
}

result_python_sqlalchemy = requests.get(url_vacancies, params=params_python_sqlalchemy).json()
sum = 0
iter = 0
for items in range(len(result_python_sqlalchemy)):
    if result_python_sqlalchemy['items'][items]['salary'] == None:
        continue
    if result_python_sqlalchemy['items'][items]['salary']['from'] == None:
        sum = sum + result_python_sqlalchemy['items'][items]['salary']['to']
        iter = iter + 1
    else:
        sum = sum + result_python_sqlalchemy['items'][items]['salary']['from']
        iter = iter + 1
middle_salary_python_sqlalchemy = sum / iter

full_percent = result_python_django['found'] + result_python_django_flask['found'] + result_python_sqlalchemy['found']
percent_python_django = round(((result_python_django['found'] / full_percent) * 100), 1)
percent_python_django_flask = round(((result_python_django_flask['found'] / full_percent) * 100), 1)
percent_python_sqlalchemy = round(((result_python_sqlalchemy['found'] / full_percent) * 100), 1)

file.write("Поиск': python developer, регион: Москва\n")
file.write("Поиск по требованиям: Python и Django\n")
file.write(f"Всего вакансий: {result_python_django['found']}, {percent_python_django}%\n")
file.write(f'Средняя заработная плата: {middle_salary_python_django}\n')
file.write("Поиск по требованиям: Python, Django и Flask\n")
file.write(f"Всего вакансий: {result_python_django_flask['found']}, {percent_python_django_flask}%\n")
file.write(f'Средняя заработная плата: {middle_salary_python_django_flask}\n')
file.write("Поиск по требованиям: Python и Sqlalchemy\n")
file.write(f"Всего вакансий: {result_python_sqlalchemy['found']}, {percent_python_sqlalchemy}%\n")
file.write(f'Средняя заработная плата: {middle_salary_python_sqlalchemy}\n')
file.close()
