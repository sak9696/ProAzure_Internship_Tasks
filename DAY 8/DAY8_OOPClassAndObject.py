

#OOP CONCEPTS IN PYTHON

#Classes and Object

class student:
    def __init__(self):
        print("heyy i am sakshi jadhav")

s1=student()

#Student Information using class and object

class stud:
    collage_name="SVPM"
    def __init__(self,name,roll):
        self.nm=name
        self.rl=roll
        print("name=",self.nm,"Roll_no=",self.rl,"Collagr name=",self.collage_name)
        

s1=stud("sakshi",10)

s2=stud("isha",11)


#CAR Information using class and object

class car:
    model="tata"
    def __init__(self,Brand_name,model,color):
        self.brd=Brand_name
        self.md=model
        self.cl=color
        print(" Car brand Name is=",self.brd,"Model is=",self.md,"and color is=",self.cl,"     ",model)


c1=car("Toyato","fortunar","White")
c2=car("Tata","S cross","black")


