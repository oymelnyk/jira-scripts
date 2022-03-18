from os import name
from jira import JIRA
from getpass import getpass
import re
from jira_insight import *

print("Login: ")
login = input()
pwd = getpass()



insight = Insight('SERVER', (login, pwd))

#object_schema = InsightObjectSchema(insight, 1)

#objects = [object_schema.search_iql("Key = SBA-599")]
#insight_object = objects[0]
#print(insight_object)

test = InsightObject(insight, 'SBA-599')



name = test.attributes['Название'].value
print(name)
#f_a = insight_objects.object_type_attributes("Сопровождение").value


#print(objects)
#print("  ")
#print(name)#+" "+f_a)
