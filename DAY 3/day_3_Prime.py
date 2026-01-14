#NUMBER IS PRIME OR NOT



num=int(input("Enter Number"))

if num<=1:
    print("not prime")

else:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
    else:
            print("prime")

