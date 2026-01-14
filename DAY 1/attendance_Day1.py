mark1=int(input("Enter the marks of SUBJECT1"))
mark2=int(input("Enter the marks of SUBJECT2"))
mark3=int(input("Enter the marks of SUBJECT3"))
mark4=int(input("Enter the marks of SUBJECT4"))
mark5=int(input("Enter the marks of SUBJECT5"))
attendence=int(input("ENTER YOUR ATTENDENCE"))

total=mark1+mark2+mark3+mark4+mark5
print("TOTAL OF ALL SUBJECT IS",total)
average=mark1+mark2+mark3+mark4+mark5/5
print("AVERAGR OF TOTAL IS:",average)
if attendence>=75:
    if average>=85:
        print("PASS WITH A GRADE ")
    elif average>=75:
        print("PASS WITH B GRADE")
    elif average>=65:
        print("PASS WITH C CLASS")
    elif average<40:
        print("SORRY GUY YOU ARE FAIL")
else:
    print("FAIL")

