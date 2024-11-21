#1
"""
x=[1,2,3,4,5,6,7,8,9,10]
even_doubles=[i*2 for i in x if i%2==0]
print(even_doubles)
"""
#2
"""
x=["Alison","Benson","Hafeed"]
intials=[i[0]for i in x]
print(intials)
"""
#3
"""
x=["apple","banana","cherry"]
with_a=[i for i in x if "a" in i]
print(with_a)
"""
#4
"""
x=[1,2,3,4,5]
sq_cu=[i**2 if i%2==0 else i**3 for i in x]
print(sq_cu)
"""
#5
"""
even_div3=[i for i in range(20) if i%2==0 and i%3==0]
print(even_div3)
"""
"""
print("stat")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
print(A/b)
print("End")
"""
"""
try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print(a/b)
except ValueError:
        print("please enter a integer number")
except ZeroDivisionError:
        print("division by zero not allowed")
finally:
        print("End")
"""
"""
def decorator(func):
    def wrap():
        print("***")
        func()
        print("***")
    return wrap

@decorator
def greet():
    print("Hello good morning")
greet()
"""
#                       PYTHON MODULES
 #                   ** _______________**
"""
import math
print(math.pi)
#help(math)

import math as m
print(m.pi)

from math import pi,floor,ceil
print(pi)
print(floor(3.9))#3
print(ceil(3.2))#4

from math import *
print(pi)
print(sqrt(25))#5
print(pow(2,3))
print(factorial(5))
"""
"""
from string import *
print(digits)
print(punctuation)
print(printable)
"""
"""
from datetime import *
x=datetime.now()
print(x.year)
print(x.month)
print(x.day)

"""
from random import *
help(random)
print(ramd:int(1000,9999)
















































































