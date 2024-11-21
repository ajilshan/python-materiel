"""
passi="ping"
while True:
    get_password=input("Enter your password")
    if passi==get_password:
        print("Successfully created password")
        break
    else:
        print("try again")
"""    
mark=[90,45,66,45,34,68]
print(mark[2])

mark.append(54)
print(mark)

mark.remove(68)
print(mark)

mark.insert(-1,68)
print(mark)

mark.pop()
print(mark)

print(mark[0:-1:2])
