#student fing avg with grade
def avgMarks(subject1,subject2,subject3):
    
    total=subject1+subject2+subject3
    avg=total/3
    return avg

def result(avg):
    if(avg>=85):
        print("Pass with grade A")
    elif(avg>75):
        print("pass with grade B")
    else:
        print("fail")

average=avgMarks(90,89,98)
result(average)

#
def avgMarks():
    n=int(input("HOW MANY STUDENT YOU WANT::"))
    for i in range(n):
        name=input("Enter Name::")
        rollno=int(input("Enter Roll NO::"))
        subject1=int(input("Enter subject 1 marks::"))
        subject2=int(input("Enter subject 2 marks::"))
        subject3=int(input("Enter subject 1 marks::"))
        total=subject1+subject2+subject3
        print("TOTAL IS::",total)
        avg=total/3
        print("AVERAGE IS::",avg)
        if(avg>=85):
            print("Pass with grade A")
        elif(avg>75):
            print("pass with grade B")
        else:
            print("fail")

average=avgMarks()





           
