
import random as rn



def allote_id(lst):
    id=rn.sample(range(100000,999999),5)
    i=0
    while i<=4:
        print(f"Employee name is {list[i]} and id is {id[i]}")
        i+=1
allote_id(["A","B","C","D","E"])
