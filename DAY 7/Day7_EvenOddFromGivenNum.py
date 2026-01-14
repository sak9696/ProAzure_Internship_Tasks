

start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))


for i in range(start, end + 1):
    if i % 2 == 0:
        print("Even numbers:",i)
        
    else:
        print("\nOdd numbers:",i)

print("\nOdd numbers:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i)
