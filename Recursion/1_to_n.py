def one_to_n(i,n):
  if i==n+1 :
    exit
  else:
    print(i)
    one_to_n(i+1,n)
    
    
def method2(n):
  if(n>0):
    method2(n-1)
    print(n)
  else:
    return  
    
one_to_n(1,5)

print("="*20)
method2(5)