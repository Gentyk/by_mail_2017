#Задание к первой домашней работе находится в
#README_homework1
import datetime

class Task:
    def __init__(self,title:str,estimate:datetime.date,state="in_progress"):
        self.title=title
        self.estimate=estimate
        self.state=state
    def remaining(self):
        if self.state=="in_progress":
            return self.estimate-datetime.today()
        else:
            return 0
    def is_failed(self):
        if self.state=="in_progress" and self.estimate<datetime.today():
            return True
        else:
            return False
    def ready(self):
        self.state="ready"

from typing import List
class Roadmap:
    t_tasks=List[Task]

    def __init__(self,tasks=[]):
        self.tasks=tasks
    def today(self):
        tasks_new=List[Task]
        for t in self.tasks:
            if t.estimate==datetime.today():
                tasks_new.append(t)
        return tasks_new
    def filter(self,state:str):
        tasks_new = List[Task]
        for t in self.tasks:
            if t.state==state:
                tasks_new.append(t)
        return tasks_new


"""a=Task("1",datetime.datetime(2050,11,10))
b=Task("2",datetime.datetime(1996,11,10))
b.ready()
c=[a,b]
print(str(c[0].estimate))
d=Roadmap(c)
print(d.tasks[0].state)#"""



