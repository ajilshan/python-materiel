#                   problem 1
"""
num=1
for i in range(101):
    
    if i%5==0:
        continue
    if i%2==0:
    print(i)
"""
#                            problem 2
"""
x=int(input("Enter a number"))
tot=0
i=1

while i<=x:
    if i%2==0:
        tot+=i
    i+=1
print(tot)
"""
#                               problem 3
for i in range(5):
    for j in range(i+1):
        print(5-j,end="")
    print()
    
#                               problem 4
"""
num=int(input("Enter a number"))
i=1
while i<=num:
    x=num/i
    i+=1
    if x>=2:
        print("p")
    else:
        print("n")
"""
#                               problem 5
"""

word1=input("Enter a word")
word2=input("Enter a word")
x=[word1]
y=[word2]
if x==y:
    print("a")
"""
#                               problem 6
"""
dict1={"p":8,"q":12,"r":5}
dict2={"q":7,"s":10,"p":4}
x=(list(dict1))
y=(list(dict2))
a=list(x+y)
"""
#                               problem 7
"""
word=input("Enter a word")
for i in range(len(word)):
    print(word.count("i"))

"""
#                               problem 8
"""
dic1={'x':10,'y':20,'z':30}
for i,j in dic1.items():
    print(j,i)
"""
#                               problem 9
"""
dict1={'data1':5,'data2':3,'data3':2}
product=1
for i in dict1.values():
    product*=i
print(product)
"""

#                       problem 10
'''
sample_list=['hello','world','python']
a="".join(sample_list)
print(a)
'''
#                       problem 11
"""
original_list=[7,2,9,4,1]
original_list.sort()
print(original_list)
print("second smallest element="original_list[1])

"""

#                       probelm 14
"""
x=input("enter a number")
if x[::-1]==x:
    print("palindrome")
else:
    print("not palindrome")
"""
#                   problem 15
"""

list1=[1,2,3]
list2=[2,3,4]
a=set(list1)
b=set(list2)
print(a.difference(b))
print(a.symmetric_difference(b))
"""





















    

























































