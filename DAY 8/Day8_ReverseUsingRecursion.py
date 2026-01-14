#Print Reverse USING RECURSION 
def fun(n):
    if n==0:
        return 
    print(n)
    fun(n-1)
    
fun(5)

#Another Logic

# def fun(n):
#     if n==0:
#         return 1
#     else:
#         print(n)
#         fun(n-1)
    
# fun(5)