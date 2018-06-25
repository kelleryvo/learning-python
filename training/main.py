# -*- coding: utf-8 -*-

#IMPORTS
import person
import platform
import datetime
#IMPORTS PARTIAL
from person import data
print(data["1"])

#INITIALIZE OBJECT
p1 = person.Person("John", 36)
p1.myfunc()

p1.age = 40

p1.myfunc()

del p1.age

#p1.myfunc()

del p1

#PRINT DATETIME
x = datetime.datetime.now()
print(x)

#SYSTEM MODULE
x = platform.system()
print(x)
