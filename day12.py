#1
"""
def greet():    #function_name #function definition
    print("hi")
    print("good morning")
greet()#functioncall
print(greet())#default function returns->none
"""
#2
"""
def greet():
    return"hi morning"
print(greet())
"""
#3
"""
def greet(name):
    return f"hi{name},Good morning"
greet("anand")#arguments [actuel value]

#4
def greet(name,place):
    return f"hi{name},are you from{place}?"
greet("Anand","Kochi")#positional Argument
greet(place="KOchi",name="sabin")#Keyword argument

#5
def greet(name,place="kochi"):
    return"{name}{place}"
greet("sabin")
greet("jithin","kozhikode")
"""
"""
def add(*args):
    #print(args)
    #print(type(args))
    sum=0
    for i in args:
        if type(i)== int or type(i)== float:
            sum+=1
    print(sum)
add(1,2,3,4,5,6,7,7,"12","hello",3.15)
"""
























































































































































































































































































