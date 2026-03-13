# Fibinoci

# What's fibinoci ? -> a number is sum of previous 2 numbers

# So, what's changing ? n as we are supposed ot calculate n-1 and n-2 , basically shrinking addition

def fib(n):
  if n==0: 
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-1)+fib(n-2)
  
res=fib(8)
print(res)