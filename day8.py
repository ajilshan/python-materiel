"""
colors=["red","blue","black","green","white","yellow"]
traffic=["red","yellow","green"]
for i in colors:
    if i in traffic:
        print(f"{i} in traffic")
    else:
        print(f"{i} not in traffic")

"""
"""
numbers=[1,2,3,4,5]
squares=[]
for i in numbers:
    squares.append(i**2)
print(squares)
"""
"""
colors=["red","yellow","orange","white","green"]
for i in colors:
    if i=="red":
        print("stop")
    elif i=="green":
        print("go")
"""
"""
colors=["red","blue","green"]
numbers=[1,2,3,4,5]
for i in colors:
    for j in numbers:
        print(j,i)
"""

#                       patterns
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
"""
#for i in range(5):
#    for j in range(5-i):
#        print("*",end=" ")
#    print()





















