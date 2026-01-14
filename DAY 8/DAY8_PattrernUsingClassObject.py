
# *
# **
# ***
# ****
# *****
# ******
class pattern:
    def __init__(self,pt):
       
        for i in range(pt+1):
            print("*"*i)
        
obj1=pattern(6)

# ******
# *****
# ****
# ***
# **
# *

class pattern:
    def __init__(self,i):
       
        while i>=1:
            print("*"*i)
            i-=1
        
obj1=pattern(6)
