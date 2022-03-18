from jira_insight import *
from getpass import getpass


import jira_insight as ji
ji1 = ji.Insight('SERVER', ('login', 'pass'))


object_schema = ji.InsightObjectSchema(ji1, 1)

print(object_schema.get_object_types)
object_schemas = ji1.get_object_schemas()
print(object_schemas)

for i in object_schemas:
    print(object_schemas[i].name)
    # .replace("InsightObjectSchema: ",""))


print("-----------")
# d={{'1811', 'objectAttributeValues': [{'value': '2'}]},
#{'objectTypeAttributeId': '1814', 'objectAttributeValues': [{'value': 'Описание объекта'}]},
# {'objectTypeAttributeId': '1821', 'objectAttributeValues': [{'value': 'АБС Б2'}]}}
#d={[{'objectTypeAttributeId':'1814'}]:[{'value': '2'}],[{'objectTypeAttributeId': '1821'}]:[{'value': 'АБС Б2'}]}


d = {"objectTypeAttributeId": 1811,
     "objectAttributeValues": [{"value": "4"}]}


x = ji.InsightObjectType(ji1, 428).create_object(d)
print(x)
