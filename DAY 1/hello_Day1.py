#STRING1 OPERATION INDEXING
str="PYTHON"
print("FORWARD INDEXING Y ACCESS ",str[1])
print("REVERSE INDEXING Y ACCESS ",str[-5])
print("FORWARD INDEXING H Access ",str[3])
print("REVERSE INDEXING H ACCESS ",str[-3])

#STRING 2 OPERATION INDEXING
str1="MY PROGRAMMING"
print(str1[-3])
print(str1[4])

#STRING 3 OPERATION CONCAT

str2="sakshi"
str3="jadhav"
print(str2+str3)

#STRING REPETATION
str4="sakshi"
oper=str4*3
print(oper)

# MEMBERSHIP OPERATOR(IN)
str5="PYTHON"
print("PY" in str5)
#SLICING OPERATION
print(str5[2:4:1])
print(str5[2:5:2])


str6="MY PROGRAMMING LANGAUGE"
s1=str6[3:14:1]
s2=str6[3:10:1]
s3=str6[15:19:1]
print(s1)
print(s2)
print(s3)

s4=str6[-8:-4:1]
s5=str6[-20:-13:1]
s6=str6[-20:-9:1]
print(s4)
print(s5)
print(s6)


#STRING FORMATTING
#1] F STRING

name=input("ENTER YOUR NAME:")
city=input("ENTER YOUR CITY:")
age=input("ENTER YOUR AGE:")
grade=input("ENTER YOUR GRADE")

print(f"My Name IS {name} and last year Grade Is {grade}.\n I live in {city} and My age is {age} ")


#2] . FORMAT
print("MY NAME IS {} AND I AM LIVE IN {}.\n MY LAST YEAR GRADE IS {} AND AGE IS{}".format(name,city,grade,age))

#STRING METHODS AND FUNCTIONS
#1 LENGTH FUNCTION

stri="PYTHON"
print(len(stri))
#2.UPPER

print(str4.upper())
#3. LOWER
print(stri.lower())
#4.TITLE
name1="sakshi mansing jadhav"
print(name1.title())

#BOOL OUTPUT METHOD
st1="python"
st2="1234"
st3="prime123"
print(st1.isalpha())#CHECK ONLY STRICTLY STRING

print(st2.isdigit())#CHECK ONLY STRICTLY DIGITS

print(st3.isalnum())#CHECK ONLY STRICTLY BOTH


# FIND FUNCTION
value="MY PROGRAMMING PROGRAM LANGAUGE"
print(value.find("PROGRAM"))

#COUNT FUNCTION
print(value.count("M"))

#REPLACE FUNCTION
print(value.replace("PROGRAMMING","BEST"))

#STRIP FUNCTION
value2="   hello     sakshi     "
print(value2.strip())

#SLICING OPERATIONS
print(str[::])

print(value[-1:-9:-1][::-1])

rev=str[::-1]
print(rev)
word=rev[0:8][::-1]
print(word)



#CONTROL STATEMENT
#1. IF STATEMENT
num=10
if num>5:
    print("number is greater")
else:
    print("number is smaller")

age=80
if age>21:
    print("Eligible for voting")

else:
    print("Not Eligible for Voting")


#EVAL FUNCTION - ACCEPT INT,FLOAT . BUT NOT ACCEPT STRING

print("1.TEA \n 2.COFFIE \n 3. milk \n 4. biscuit")

choice=eval(input("Enter Your Choice:"))
if choice==1:
    print("Tea Is Ordered")

elif choice==2:
    print("Coffie is Ordered")

elif choice==3:
    print("milk is Ordered")

elif choice==4:
    print("biscuit is ordered")

else:
    print("invalid choice")

username=input("ENTER USERNAME")
password=int(input("ENTER PASSWORD"))

if username=="Admin":
    if password==1234:
        print("LOGIN SUCCESSFUL")
    else:
        print("INCORRECT PASSWORD")

else:
    print("INVALID USER")
