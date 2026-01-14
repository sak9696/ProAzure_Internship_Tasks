a=int(input("Enter the First Side of Tringle"))
b=int(input("Enter the Second Side of Tringle"))
c=int(input("Enter the Third Side of Tringle"))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tringle is VALID and equavalence")
    elif a!=b and a==c  or c==b and a!=c:
        print("Two Side Same")
    else:
        print("Three Sides are Different")
else:
    print("tringle is invalid")


