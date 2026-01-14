# def fibbonanci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return fibbonanci(n-1)+fibbonanci(n-2)
# n=23
# for i in range(n+1):
#     print(fibbonanci(i))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
   
# print(fact(5))

# def sum(n):
#     for i in range(1,n):
#         return n+sum(n-1)
# print(sum(5))


import random as rn
r=rn.random()
list1=[]
def generate_otp():
    otp=rn.sample(range(11111,999999),1)
    print("Your Generayed OTP is::",otp)
    list1.append(otp)
    print(list1)



while True:
    ch=input("Do you want to generate OTP")

    if ch=='stop':
        print("ok you stopped to generate OTP")
    if ch=='yes':
        generate_otp()


    
       
        
        