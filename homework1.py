#Задание к первой домашней работе находится в
#README_homework1
import datetime

class Task:
    def __init__(self,title:str,estimate:datetime.date,state="in_progress"):
        if type(title)!=str:
            raise TypeError("Invalid data for the attribute TITLE: must be str.")
        self.title=title
        if type(estimate)!=datetime.date:
            raise TypeError("Invalid data for the attribute ESTIME: must be datetime.date.")
        self.estimate=estimate
        if type(state)!=str:
            raise TypeError("Invalid data for the attribute STATE: must be str.")
        if state!="in_progress" and state!="ready":
            raise AttributeError
        self.state=state

    @property
    def remaining(self)->datetime.timedelta:
        if self.state=="in_progress":
            return self.estimate-datetime.today()
        else:
            return 0

    @property
    def is_failed(self):
        if self.state=="in_progress" and self.estimate<datetime.today():
            return True
        else:
            return False

    def ready(self):
        self.state="ready"


class Roadmap:
    def __init__(self,tasks=[]):
        if all(isinstance(x, Task) for x in tasks)==False:
            raise TypeError("tasks must have type=List[Task]")
        else:
            self.tasks = tasks



    @property
    def today(self):
        tasks_new=[]
        for t in self.tasks:
            if t.estimate==datetime.today():
                tasks_new.append(t)
        return tasks_new

    def filter(self,state:str):
        if type(state)!=str:
            raise TypeError("")
        tasks_new = []
        for t in self.tasks:
            if t.state==state:
                tasks_new.append(t)
        return tasks_new


"""
#testing
a=Task("1",datetime.date(2050,11,10))
b=Task("2",datetime.date(1996,11,10))
b.ready()
c=[a,b]
#by testing error:
#c=[a,b,"dlllssdsd"]
d=Roadmap(c)
print(d.tasks[1].state)
"""



