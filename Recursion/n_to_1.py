# Head

def head(n):
  if(n > 0):
    print(n)
    head(n-1)
  else:
    exit


# Tail

def tail(i,n):
  if(i < n+1):
    tail(i+1,n)
    print(i)
  else:
    exit 
    
    
tail(1,5) 
print("="*20)
head(5)
    
