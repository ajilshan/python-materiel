a=int(input("Enter the age of first person:"))
b=int(input("Enter the age of second person:"))
c=int(input("Enter the age of third person:"))
if a>b>c:
    print("First person is the oldest and third person is the youngest")
elif b>c>a:
    print("second person is the oldest first person is the youngest")
elif c>b>a:
    print("third person is the oldest and first person is the youngest")
elif a>c>b:
    print("first person is oldest and second person is youngest")
elif c>a>b:
    print("Third peron is the oldest and second person is the youngest")
elif b>a>c:
    print("second person is the youngest and third person is the youngest")
elif a==b==c:
    print("All are same age")
else:
    print("do not enter two same ages")
    



