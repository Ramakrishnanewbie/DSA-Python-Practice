## To check if a number is a pallindrome or not


## TC - O(logN)
## SC - O(1) 

def pal_check(n):
  org=n
  s=0
  while(n>0):
    r=n%10
    s=s*10+r  
    n= n//10
  
  if s ==org:
    print("pallindrome")
  else:
    print("not pallindrome")
    
    
if __name__ == "__main__" :
  pal_check(1232)
  