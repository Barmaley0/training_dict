"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

print("Отделы:")
for item in departments:
    print(item["title"])
print(" ")

names_list = []
for item in departments:
    for name in item["employers"]:
        names_list.append(name["first_name"] + " " + name["last_name"])
print("Все сотрудники компании:\n", "\n".join(names_list), sep="")
print(" ")

for item in departments:
    print("Отдел:", item["title"])
    print("-" * 10)
    print("Сотрудники:")
    for name in item["employers"]:
        print(f"{name['first_name']} {name['last_name']}")
        
    print(" ")

names_list = []
for item in departments:
    for name in item["employers"]:
        if name["salary_rub"] > 100000:
            names_list.append(name["first_name"] + " " + name["last_name"])
        else:
            pass
print("Все сотрудники компании которые получают больше 100 000руб:\n", "\n".join(names_list), sep="")
print(" ")

names_list = []
for item in departments:
    for name in item["employers"]:
        if name["salary_rub"] < 80000:
            names_list.append(name["first_name"] + " " + name["last_name"])
        else:
            pass
print("Все сотрудники компании которые получают меньше 80 000руб:\n", "\n".join(names_list), sep="")
print(" ")

salary_list_hr_dep = []
salary_list_it_dep = []
for item in departments:
    if item["title"] is "HR department":
        for salary in item["employers"]:
            salary_list_hr_dep.append(salary["salary_rub"])
    else:
        for salary in item["employers"]:
            salary_list_it_dep.append(salary["salary_rub"])
print(f"Зарплата сотрудников отдела {departments[0]['title']} составила {sum(salary_list_hr_dep):,.0f}руб в месяц. ")
print(f"Зарплата сотрудников отдела {departments[1]['title']} составила {sum(salary_list_it_dep):,.0f}руб в месяц. ")
print(" ")

print(f"Минимальная зарплата сотрудника отдела {departments[0]['title']} составила {min(salary_list_hr_dep):,.0f}руб в месяц. ")
print(f"Минимальная зарплата сотрудника отдела {departments[1]['title']} составила {min(salary_list_it_dep):,.0f}руб в месяц. ")
print(" ")

print(f"Минимальная зарплата сотрудника отдела {departments[0]['title']} составила {min(salary_list_hr_dep):,.0f}руб в месяц. ")
print(f"Средняя зарплата сотрудника отдела {departments[0]['title']} составила {sum(salary_list_hr_dep) / len(salary_list_hr_dep):,.0f}руб в месяц. ")
print(f"Максимальная зарплата сотрудника отдела {departments[0]['title']} составила {max(salary_list_hr_dep):,.0f}руб в месяц. ")
print(f"Минимальная зарплата сотрудника отдела {departments[1]['title']} составила {min(salary_list_it_dep):,.0f}руб в месяц. ")
print(f"Средняя зарплата сотрудника отдела {departments[1]['title']} составила {sum(salary_list_it_dep) / len(salary_list_it_dep):,.0f}руб в месяц. ")
print(f"Максимальная зарплата сотрудника отдела {departments[1]['title']} составила {max(salary_list_it_dep):,.0f}руб в месяц. ")
print(" ")
print(" ")
print(" ")




