'''
a=70
b=70
if(a is not b):
    print("result : a and b have the same value")
else:
    print("result : a and b do not have the same value")

a=20
b=20
if(id(a) is id(b)):
  print("result : a and b have the same value")
else:
    print("result : a and b do not have the same value")

z=10
c=12
print(z is c)
'''
#identity operators are used to compare the memory location of two objects to
#check if they are same object
#is,is not
#id() to obtain the memory location of an object

a=10
b=15
c=10
print(id(a))
print(id(b))
print(id(c))
print(a is b) #false
print(a is c) #true

print(a is not c) #false

#class - properties,behaviour

#membership operator( in,not in)
"""
x="HELLO WORLD"

print("WO"in x)#true
print("WORLD" in x)#true
print("DL" in x)#false

#round()

print(round(3.15))#3
print(round(3.1539,2))#3.15

l=3.1596
print(round(l,2))#2 means decimal value that want to be rounded
"""
x="hello world"
print(len(x))#11

#input
"""
name=input("enter your name:")
age=input("enter your age:")
print(name)
print(age)
print(type(name))
print(type(age))

x=int(input("enter your number:"))
y=int(input("enter a number:"))
print(x*y)

x=input("enter your number:")
y=input("enter a number:")
print(x*y) #error - str*str(error)
"""

#string method
#{}place hoders
'''
name=input("enter your name:")
age=int(input("enter your age:"))
print("my name is {} and i'm {} years old".format(name,age))
print(age>18)#true
'''
#f string method
'''
name=input("enter your name:")
age=int(input("enter your age:"))
print(f"my name is {name} and i'm {age} years old")
print(age>20)
'''

#conditional statments
'''
x=int(input("enter number:"))
if x>10:
       print(f"{x} is greater than 10")
print("end program")
'''

#num=int(input("enter a number:"))
#if num%2==0:
#    print(f"{num} is even")
#else:
#    print("f{num} is not even")

num=int(input("enter a number:"))

if num%5==0 and num%7==0:
    print(f"{num} is factor of both 5 and 7")



 





























































