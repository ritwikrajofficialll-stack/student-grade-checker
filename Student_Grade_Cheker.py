name = input("Enter your name : ")
sub1 = int(input("Enter your physics marks : "))
sub2 = int(input("Enter your chemistry marks : "))
sub3 = int(input("Enter your maths/bio marks : "))

print("Name : " , name)

#CODE FOR PHYSICS
if(sub1>=90):
    print("Grade A in physics")
elif(sub1>=80):
    print("Grade B in physics")
elif(sub1>=70):
    print("Grade C in physics")
elif(sub1>=60):
    print("Grade D in physics")
else:
    print("Grade F in physics") 

#CODE FOR CHEMISRY
if(sub2>=90):
    print("Grade A in chemistry")
elif(sub2>=80):
    print("Grade B in chemistry")
elif(sub2>=70):
    print("Grade C in chemistry")
elif(sub2>=60):
    print("Grade D in chemistry")
else:
    print("Grade F in chemistry")

#CODE FOR MATH/BIO
if(sub3>=90):
    print("Grade A in maths/bio")
elif(sub3>=80):
    print("Grade B in maths/bio")
elif(sub3>=70):
    print("Grade C in mathys/bio")
elif(sub3>=60):
    print("Grade D in maths/bio")
else:
    print("Grade F in maths/bio")      

total = (sub1+sub2+sub3)
percentage = ((total)/300) * 100

print("Total marks : " , total)
print("Percentage : " , percentage)

if(percentage>=90):  
    print("Overall Grade is A ")
elif(percentage>=80):
    print("Overall Grade is B ")
elif(percentage>=70):
    print("Overall Grade is C ")
elif(percentage>=60):
    print("Overall Grade is D ")
else:
    print("Overall Grade is F ") 
print("************************CODE ENDS********************************BY RITWIK RAJ :)*******")
#CODE IS WRITTEN BY RITWIK RAJ.....:):)