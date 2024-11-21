                            #problem 1
"""
num=int(input("Enter a number"))
i=1
fact=1
while(i<=num):
    fact*=i
    i+=1
print(f"factoriel of {num} is {fact}")
"""
#                           problem 2
"""
a=1
while(a<=10):
    print(a)
    a+=1
"""
#                           problem 3
"""
a=1
while(a<=10):
    a+=1
    if a%2!=0:
        continue
    print(a)
"""
#                           problem 4
"""
passo="pass@123"
while True:
    get_pass=input("Enter a password")
    if get_pass==passo:
        print("successfully created password")
        break
    elif get_pass=="quit":
        print("terminated")
        break
    else:
        print("try again")
"""
#                           problem 5
"""
num=int(input("Enter digits"))
sum=0
if num>0:
    for i in range(len(str(num))):
        rem=num%10
        sum+=rem
        num//=10
    print(sum)
else:
    print("try again")
"""
#                           problem 6






































    
    


















