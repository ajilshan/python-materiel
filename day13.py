#fininocci series
"""
a=0
b=1
print(a,end=",")
print(b,end=",")
for i in range(8):
    c=a+b
    print(c,end=",")
    a,b=b,c
"""
#with function
"""
def fininocci(num):
    a=0
    b=1
    print(a,end=",")
    print(b,end=",")
    for i in range(num-2):
        c=a+b
        print(c,end=",")
        a,b=b,c
num=int(input("Enter the limit"))
fininocci(num)
"""
"""
def palindrom(stri):
    if stri[-1]==stri:
        return "palindrome"
    else:
        return "Not palindrome"
stri=input("Enter a word:")
palindrom(stri)
"""
#lambda anonymous functions
#sample=lambda :"hello"
#print(sample())

#sample=lambda x :f"hi {x}"
#print(sample("benison"))

#add=lambda x,y : x+y
#print(add(5,3))

#  1                         map_function
"""
number=[1,2,3,4,5]
squares=map(lambda x:x**2,number)
print(squares)#map object
print(list(squares))#[1,4,9,16,25]
#1.1
number=[1,2,3,4,5]
squares=map(lambda x:x%2==0,number)
print(squares)#map object
print(list(squares))#[1,4,9,16,25]
"""

# 2                         filter
"""
numbers=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x:x%2==0,numbers)
print(list(even))#[2,4,6,8,10]  
"""
#   3                        reduce
"""
from functools import reduce
numbers=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)#15
"""
#                       List comperhension
"""
numbers=[1,2,3,4,5]
sqrs=[]
for i in numbers:
    sqrs.append(i**2)
print(sqrs)
"""
          #to
"""
numbers=[2,4,6,8,10]
squares=[i**2 for i in numbers]
print(squares)
"""
#_____________________________________________________________________________
#1
"""
x=[1,2,3,4,5,6,7,8,9,10]
even_doubles=[]
for i in x:
    if i%2==0:
        even_doubles.append(i*2)
print(even_doubles)#[4,8,12,16,20]
"""
#2
"""
names=["Alice","Benison","Hafeed","Sabin"]
intials=[]
for i in names:
    intials.append(i[0])
print(intials)
"""
#3
"""
words=["apple","banana","kiwi","Cherry"]
words_with_a=[]
for i in words:
    if "a" in i:
        words_with_a.append(i)
print(words_with_a)
"""
#4
"""
numbers=[1,2,3,4,5]
sqrs_cube=[]    #even-sqaures,odd-cube
for i in numbers:
    if i%2==0:
        sqrs_cube.append(i**2)
    else:
        sqrs_cube.append(i**3)
print(sqrs_cube)
"""
#5
"""
x=[]#even and divisible by 3
for i in range(20):
    if i%2==0 and i%3==0:
        x.append(i)
print(x)
"""
















































































































































