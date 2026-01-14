
import random as rn

r=rn.random()#for generate random values from 0 to 1
print(r)

r=rn.randint(10,50) #for int
print(r)

r=rn.uniform(10.12,90.09)#for float
print(r)

r=rn.sample(range(1,150),5)
print(r)
