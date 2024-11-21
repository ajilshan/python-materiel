"""
                        problem 1
                        ~~~~~~~~~
y=int(input("Enter a year"))
if (y%4==0) or (y%400==0):
          print("it is a leap year")
else:
        print("it is not a leap year")
"""
#                       problem 2
'''
num=int(input("enter a number"))
if num%5==0 and num%7==0:
    print(f"{num} is factor of 5 and 7")
else:
    print(f"{num} is not a factor of 5 and 7")
'''
#                       problem 3
"""
a=int(input("enter the 1st length of a triangle"))
b=int(input("enter the 2nd length of a triangle"))
c=int(input("enter the 3rd length of a triangle"))
if a+b>c:
    print("valid")
elif c+a>b:
    print("valid")
elif b+c>a:
    print("valid")
else:
    print("not valid")
"""
#                       problem 4
"""
a=int(input("enter a number"))
b=int(input("enter a number"))
c=(input("enter an operator"))
if c=="*":
    print(a*b)
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="/":
    print(a/b)
else:
    print("invalid")
"""
#                       problem 5
"""
x=int(input("enter a number"))
y=int(input("enter a number"))
if x>0 and y>0:
    print("first quadrent")
elif x<0 and y>0:
    print("Second quadrant")
elif x<0 and y<0:
    print("Third quadrant")
elif x>0 and y<0:
    print("Fourth quadrant")
elif x==0 and y==0:
    print("Origin")
else:
    print("invalid")

"""
#                       problem 6
"""
weight=float(input("enter your weight "))
height=float(input("enter your height "))
bmi=weight/height**2
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<24.9:
    print("normal weight")
elif 25<=bmi<29.9:
    print("overweight")
elif bmi>30:
    print("obesity")
else:
    print("not found")
"""
#                       problem 7
"""
age=int(input("Enter your age"))
if age>0 and age<12:
    print("Child")
elif age>12 and age<19:
    print("Teenager")
elif age>19 and age<64:
    print("Adult")
elif age>64:
    print("Senior")
else:
    print("not found")
"""

#                       problem 8
day=int(input("Enter a number"))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("invalid")


































    












    
