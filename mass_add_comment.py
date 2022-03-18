import re
from jira import JIRA
from getpass import getpass
from jira_insight import *


jira_server = 'SERVER'
#JQL_WU = 'project = ITSD AND status = "Open 2 line" AND "Information System" = SBA-599 AND assignee in (EMPTY) and summary ~ "Сброс пароля WU" and "Bank Branch" is not EMPTY AND "Логин пользователя WU" is not EMPTY AND "Assigned group" = Jira_IT_XXX and summary !~ "Сброс пароля оператора WU"'
login = ''  # ADD your login
pwd = getpass()
jira = JIRA(server=jira_server, basic_auth=(login, pwd))

issues = []  # add issues

sub_task = []  # add subtask numbers for comment


i = 0
for issue in issues:
    txt = str("Создана подзадача на 1 линию - ["+str(sub_task[i])+str(
        "|SERVER/browse/"+str(sub_task[i])+"]"))  # comment text
    print(txt)
    comment = jira.add_comment(issue, txt, is_internal=True)
    i = i+1
