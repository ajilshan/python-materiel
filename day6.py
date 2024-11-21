'''
password="pass@123"
while True:
    get_password = input("Enter your password:")
    if password == get_password:
        print("Successfully logged in")
        break
    else:
        print("try again")
'''
#                DATA STRUCTURE
#                   LIST
#changable
#ordered
#slicing
#[square brackets]
#duplicate elements allowed
'''
sample=[20,45,30,25,35,10]
#[45,25,10]
print(sample[1::2])
print(sample[-5:])
print(sample[-5:-2])
print(sample[-5::1])
print(sample[::-1])
'''
mark=[25,54,32,67,65,]
print(mark)
mark.append(76)
print(mark)
