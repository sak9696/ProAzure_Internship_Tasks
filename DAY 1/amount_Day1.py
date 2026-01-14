amount=int(input("Enter the amount="))
withdraw=int(input("how much amount you want to WITHDRAW"))

if amount>=withdraw:
    result=amount-withdraw
    print("Withdraw  is SucceessFull. \n Remaining aount is:",result)
elif amount<withdraw:
    print("not Sufficient amount:")
else:
    print("Something Issue")
    
    
