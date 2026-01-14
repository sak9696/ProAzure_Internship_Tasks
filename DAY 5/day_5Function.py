#define FUNCTION

def myFunction():
    print("welcome miss sakshi jadhav")
myFunction()

#FUNCTION WITH ARGUMENTS
def myFunction2(a,b):
    print(a+b)
myFunction2(2,3)


#FUNCTION WITH ARGUMENTS WITH STRING FORMATING

def myFunction3(name,city):
    print(f"heyy  i am {name} i currently live in{city}")
myFunction2("sakshi","baramati")

#FIND OUT THE SQUARE OF DIFFERENT WAYS
def myFunction4(i):
    print(i**2)
    print("square is",i*i)
myFunction4(6)

#PARAMETER PASSING WITH DIFFERENT ARGUMENTS 
# POSITIONAL ARGUMENTS

def myFunction5(rollno,name,marks):
    print("rollNo=",rollno,"name=",name,"marks=",marks)

myFunction5(rollno=10,name="sakshi",marks=9.32)

#KEYWORDS ARGUMENTS

def myFunction5(rollno,name,marks):
    print("rollNo=",rollno,"name=",name,"marks=",marks)

myFunction5(name="sakshi",marks=9.32,rollno=10)


# #DEFAULT PARAMETER
# def myFunction6(rollno=10,name="SWATI"):

#     rollno=int(input("Enter Roll no:"))
#     name=input("Enter Name:")
#     print("rollNo=",rollno,"name=",name)

# myFunction6()


def AverageOfMarks():
    marks1=int(input("enter a marks of 1:"))
    marks2=int(input("Enter marks 2:"))
    marks3=int(input("Enter marks 3:"))

    total=marks1+marks2+marks3
    avg=total/3
    print("average of marks",avg)
AverageOfMarks()


#LAMBADA FUNCTION
square=lambda x:x*x
print(square(5))