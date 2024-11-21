#to remove duplicate item from list
"""
x=[5,2,1,2,3,4,2]
y=[]
for i in x:
    if i not in y:#already printed items will not be taken
        y.append(i)
print(y)
"""
#with set
"""
x=[5,2,1,2,3,4,2]
y=set(x)
print(y)
"""
#                       dictionary
"""
phone_numbers={"athul":"1234",
             "hafeed":"4567",
             "Rahul":"2459",}
print(phone_numbers)
print(phone_numbers["athul"])#accessing
phone_numbers["athul"]="4321"#updation/adding
print(phone_numbers)
"""
#Alternative method
"""
phone_numbers={"athul":"1234",
             "hafeed":"4567",
             "Rahul":"2459",}
print(phone_numbers.get("athul"))#get value
phone_numbers.update({"benison":"1234"})#Add item
print(phone_numbers)
phone_numbers.update({"athul":"9999"})#update item
print(phone_numbers)
"""
"""
roll_numbers={1:"anand",
              2:"abhinand",
              3:"benison",
              4:"hafeed",
              4:"sai",}
print(roll_numbers)
roll_number.pop(2)#pop(key)
print(roll_numbers)
roll_numbers.popitem()#to remove last item
print(roll_numbers)
roll_numbers.clear()
print_numbers.clear()
"""

#print(roll_numbers.keys())
#print(roll_numbers.values())
#print(roll_numbers.items())
"""
roll_numbers={1:"anand",
              2:"abhinand",
              3:"benison",
              4:"hafeed",
              4:"sai",}
for i in roll_numbers:
    print(i)

for i in roll_numbers.keys():
    print(i)
    
for i in roll_numbers:
    print(roll_numbers[i])
    
for i in roll_numbers.values():
    print(i)

for i in roll_numbers.items():
    print(i)
for i,j in roll_numbers.items():
    print(i,j)
"""
#zip()

x=["physics","chemestry","maths"]
y=[40,35,48]
sample=list(zip(x,y))
sample_dic=dict(zip(x,y))
print(sample)
print(sample_dic)

sum=0
num=int(input("Enter a positive number"))
for i in range(len(str(num))):
    rem=num%10
    sum+=rem
    num//=10
print(sum)





        










































