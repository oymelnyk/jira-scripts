from getpass import getpass
from jira_insight import *

#print("Login: ")
# login = input() #LOGIN
#pwd = getpass()


insight = Insight('SERVER', (login, pwd))

object_schema = InsightObjectSchema(insight, 1)


i = [i for i in object_schema.search_iql(
    "objecttypeid = 146 AND \"№ договора\" = П2021")]

for n in i:
    print(n.attributes['№ договора'].value)
    print(n.attributes['Статус договора'].value['name'])
    print(n.attributes['Компания'].value[0].attributes['Наименование'].value)
    for i in n.attributes['ИТ система'].value:
        print(i.attributes['Название'].value)

    print(n.attributes['Тип договора'].value[0])
    print(n.attributes['Суть договора'].value[0])
    print(n.attributes['Краткое описание деталей договора'].value)
    print(n.attributes['Подразделение ДИТ'].value[0])
    print(n.attributes['Ответственный за договор'].value[0])
    print(n.attributes['сумма договора'].value)
    print(n.attributes['дата заключения'].value)
    print(n.attributes['дата окончания'].value)
    # print( n.attributes['******'].value) you can add more attributes
