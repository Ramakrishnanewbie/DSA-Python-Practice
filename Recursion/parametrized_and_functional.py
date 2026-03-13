# Parametrized and fucntional Recursion :

# sum 1 to n
sum=0

def func(n,sum=0,i=1):
  if i>n :
    print(sum)
    return
  else:
    func(n,sum+i, i+1)
    
    

func(5)



## Functional recusrion -> No printing, only returning

# 1 to N 

def func_recursion(n,sum=0):
  if n == 1:
    return 1
  else:
    return n+func_recursion(n-1)
  
res=func_recursion(10)
print(res)