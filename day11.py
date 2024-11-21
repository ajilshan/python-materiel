"""
student_marks={"anand":"65",
               "abhinand":"75",
               "athul":"82",
               "benison":"42",
               "hafeed":"35",
               "jihin":"95",
    }
student_grade={}
for name in student_marks:
    #print("key",name)
    #print("value",student_marks[name])
    mark=int(student_marks[name])
    if mark>90:
        student_grade[name]="A+"
    elif mark>80:
        student_grade[name]="A"
    elif mark>70:
        student_grade[name]="B+"
    elif mark>60:
        student_grade[name]="B"
    elif mark>50:
        student_grade[name]="C"
    elif mark>40:
        student_grade[name]="D"
    else:
        student_grade[name]="F"
print(student_grade)
"""
#                       string
"""
x=input("enter a string:")
if x[::-1]==x:
    print("palindrome")
else:
    print("NOt palindrome")
"""
"""
a="venom"
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.count("n"))
print(a.count("n",0,3))#with range
print(a.find("n"))#index position
print(a.find("n",0,3))#with range
print(a.endswith("nom"))
print(a.startswith("ve"))

x="WelCome"
print(x.swapcase())
"""
#split
#y="python learning on progress"
#x=y.split()
#print(x)
#y="python learning on progress"
#x=y.split("n")#now 'n is the splitter'
#print(x)

#a=["python","learning"]
#b="".join(a)
#print(b)
#a=["python","learning"]
#b="@".join(a)
#print(b)

#                               strip()

#x="###hello###"
#print(x.strip("#"))#full strip
#print(x.lstrip("#"))#left side strip
#print(x.rstrip("#"))#right side strip


#                               replace()
"""
x="this is a string,string,string"
print(x.replace("string","text"))
print(x.replace("text","string"))
"""

x="""welcome to python,
python is a programming
language
"""
#y=list[x]
#y.split()        












































































        











































