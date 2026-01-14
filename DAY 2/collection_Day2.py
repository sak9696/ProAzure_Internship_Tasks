#non primitive data type/collective DT / collection
#list
my_List=["apple","chikoo",4,6.7]

print(my_List)
print(my_List[0])
print(my_List[1])
print(my_List[2])
print(my_List[3])


#1.append(ele) 2.insert(index,ele), 3. extend(list)
#append(ele)
my_List.append("sak")
print(my_List)
#insert

my_List.insert(3,12.09)
print(my_List)

my_List.insert(-2,1)
print(my_List)

#3. extend(list)
list2=[7,8,9]
my_List.extend(list2)
print(my_List)


list1=[1,2,3,4,[10,20,30],90,100,[2,4,6,8],100,200]
print(list1[-3])
print(list1[4])

list1[4].append("cricket")
print(list1)


list1[-3].insert(2,"hockey")
print(list1)
list=[6,7,5,6]
list1[-3].extend(list)
print(list1)

#1.remove 2.pop 3.clear

lst=[1, 2, 3, 4, [10, 20, 30, 'cricket'], 90, 100, [2, 4, "hockey", 6, 8], 100, 200]
lst.remove(2)
print(lst)

lst.pop()
print(lst)




lst[-3].remove("hockey")

















