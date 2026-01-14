import random as rn

list1 = ["A", "B", "C", "D", "E"]
list2 = rn.sample(range(111111, 1509999), 6)

print(list1)
print(list2)

for i in range(len(list1)):
    print("Name",list1[i], "=RollNo", list2[i])
