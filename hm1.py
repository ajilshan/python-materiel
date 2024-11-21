#
"""
i=1
sum=0
while i<=100:
    if i%2==0:
        sum+=i
    i+=1
print(sum)
"""
#2
"""
x=int(input("Enter a number"))
multi=[]
for i in range(10):
    multi.append(x)
    x=x+multi[0]
print(multi)
"""
#3
"""
x=[5,4,2,6,3,7,1]#maximum number
x.sort()
print(x[-1])
"""
#4
"""
a,b=0,1
result=[]
for i in range(20):
    result.append(a)
    a,b=b,a+b
print(result)
"""
#5
x=int(input("Enter a number:"))
fact=1
a=1
for i in range(1,x):
    fact*=a
print(fact)


    
















    
