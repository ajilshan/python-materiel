#1-C
#2-C
#3-A
#4-B
#5-C
#6-D
#7-A
#8-C
#9-C
#10-B

#11
"""
x=[1,2,3,4,5]
sqr=[i*2 for i in x]
print(sqr)
"""
#12
"""
x=[1,2,5,3,9]
def sec_lar():
    x.sort(reverse=True)
    print(x[1])
sec_lar()
"""
#13
"""
x=[1,6,5,6,3,7,1]
def rem_dup():
    a=set(x)
    b=list(a)
    print(b)
rem_dup()
"""
#14
"""
num=(1,2,3,4,5,6)
#print(type(num))
def rev_ord():
    a=list(num)
    a.sort(reverse=True)
    b=tuple(a)
    print(b)
rev_ord()
"""
#15




#16
"""
a={1,2,3,4}
b={9,10}
def is_disjoint():
    print(b.isdisjoint(a))
is_disjoint()
"""
#17
"""
dict1={"1":"A","2":"B","3":"C"}
dict2={}
def swap():
    dict2=dict(zip(dict1.values(),dict1.keys()))
    print(dict2)
swap()
"""
#18
"""
a={"A":1,"B":2,"C":3}
b={"A":3,"B":4,"X":5}
def merge():
    a.update(b)
    print(a)
merge()
"""
#19
"""
def fact():
    x=int(input("Enter a number"))
    i=1
    fact=1
    while(i<=x):
        fact*=i
        i+=1
    print(fact)
fact()
"""
#20
"""
number=[1,2,3,4,5,6,7]
even=map(lambda x:x%2==0,number)
print(list(even))
"""
#21
"""
number=[1,2,4,5,6]
square=map(lambda x:x**2,number)
print(list(square))
"""
#22

#23 Not completed
"""
a="agio"
def vowel():
    print(a.find("a"))
    
vowel()
"""
#24
"""
a="venom"
def title():
    print(a.title())
title()
"""
#25
"""
x="hello"
def common():
    for i in range(len(str(x))):
"""
#26
"""
class Bank():
    def __init__(self,acc,cname,balance):
        self.acc=acc
        self.cname=cname
        self.balance=balance
    def deposit(self):
        deposit=int(input("Enter deposit amount:"))
        afterdeposit=self.balance+deposit
        print(f"Balance:{afterdeposit}")
    def withdrawel(self):
        withdraw=int(input("Enter withdrawel amount"))
        if withdraw<self.balance:
            after_withdrawel=self.balance-withdraw
            print(f"Balance:{after_withdrawel}")
        else:
            print("Insufficiant balance")
    def show_balance(self):
        print(self.balance)
    
            
obj1=Bank("123","Aj",1000)
#obj1.deposit()
obj1.withdrawel()
obj1.show_balance()
"""
#27
"""
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def personal_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class Student_id(Person):
    def __init__(self,name,age,student_idn):
        super().__init__(student_idn)
        self.studentidn=student_idn
        
        
obj1=Person("aj",20)
#obj1.personal_details()
obj2=Student_id("aj",20,"554")
print(obj2.student_idn)
"""
#28
"""
x=input("enter a string:")
def palindrome():
    if x[::-1]==x:
        print("palindrome")
    else:
        print("NOt palindrome")
palindrome()
"""
#29






















































































    
















































    



























    
    

