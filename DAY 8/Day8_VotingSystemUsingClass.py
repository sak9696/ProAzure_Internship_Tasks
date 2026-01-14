
class voting:
    age=[12,45,76,90,34,2,34,12,21,32]
    name=["A","B","C","D","E","F","G","H","I","J"]
    list3=[]

    def __init__(self):
        for i in range(len(self.age)):
            if self.age[i]>=21:
                print("Eligible For Voting",self.name[i],"-",self.age[i])
                self.list3.append(self.name[i])
        print(self.list3)
        for i in range(len(self.age)):    
            if self.age[i]<=21:
                print("Not Eligible For Voting",self.age[i])

v1=voting()



        