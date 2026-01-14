



#Take two inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Operations
add = a + b
sub = a - b
mul = a * b

print("Addition Is:",add)
print("Subtraction Is:",sub)
print("Multiplication Is:",mul)

# Division (avoid divide by zero)
if b != 0:
    div = a / b
    print("Division Is:",div)
else:
    div = None