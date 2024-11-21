#Tuple
"""
numbers=(1,2,3,4,5)
print(numbers)
print(type(numbers))
print(number[0])
print(number[-1])
print(numbers[::-1])
x=(1,2,3)
y=(4,5,6)
print(x+y)
"""

#x=(1,2,3,4)
#y=list(x)
#y.append(5)
#x=tuple(y)
#print(x)

#x=(1,True,3.14,"hello",[1,2,3,4])
#y=list(x)
"""
x=[1,2,3,[4,5,6,[7,8,9,[10,11],12],13],14,15,[16,17],18]
print(x[3][1])
print(x[3][3][2])
print(x[3][3][3][0])
print(x[3][4])
print(x[6][1])
"""
setA={1,2,3,4,5}
setB={4,5,6,7,8}
#print(setA.union(setB))#union
#setA.update(setB)#update
#print(setA)
#print(setA.intersection(setB))#intersection
#setA.intersection_update(setB)#intersection update
#print(setA)
#print(setA.difference(setB))#differance
#print(setB.difference(setA))
#setA.difference_update(setB)#diffrence update
#print(setA)
#setB.difference_update(setA)#diffrence update setB
#print(setB)
#print(setA.symmetric_difference(setB))#symmetric diffrence
#setA.symmetric_difference_update(setB)#symmetric diffrence update
#print(setA)

#superset
#subset
#disjoint

A={1,2,3,4}
B={3,4}
C={9,10}

print(A.issuperset(B))
print(A.issubset(C))
print(A.issubset(B))
print(B.issubset(A))
print(B.issubset(C))
print(C.isdisjoint(A))
print()


















































