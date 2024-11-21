#file operations
"""
file=open("sample.txt","r")
#print(file.read())
#print(file.read())
data=file.readlines()
print(data)
"""

#read "r"
#write "w"
#append "a"
#create "x"
"""
file=open("sample2.txt","w")
file.write("HEloo world")
file.write("sample data")
file.close()
"""
"""
with open("sample3.txt","w")as file:
    print(file.write("sample"))
    file.writelines(["seeyou"," \n soon"])
"""
"""
file=open("sample2.txt","a")
file.write("KK")
file.close()
"""
#OOPS: Object Oriented Programming Language

class Watch():#constructor method
    def __init__(self,brand,strap,waterproof,type):
        self.brand=brand
        self.strap=strap
        self.waterproof=waterproof
        self.type=type
        self.time="12:00"
    def display(self):
        print(f"current time:{self.time}")
    def adjust_time(self,newtime):
        self.time=newtime
        print(f"adjusttime:{self.time}")
    def is_waterproof(self):
        #if self.waterproof==True:
        #    print("Water Proof")
        #else:
        #    print("Not")

        print(f"waterproof: {self.waterproof}")
        
#object creation
obj1=Watch("Rolex","metal",False,"analog")
obj2=Watch("paantz","rubber",True,"Digital")
#object function accessing
obj1.display()
obj2.display()
obj1.adjust_time("11:00")
obj1.is_waterproof()

    

























    
    



























