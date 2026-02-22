## Armstrong Number : if sum of each digit raised to the number of digits gives the same number, then we can call it armstrong number. 
from math import *

def armstrong_num(n):
  
  ## Find number of digits
  num_digits=int(log10(n)+1)
  org=n
  s=0
  while(n > 0):
    r=n%10
    s=s + (r**num_digits)
    n=n//10
  
  if(s == org):
    print("Armstraong Number")
  else:
    print("Not Armstrong Number")
    
    
if __name__ == "__main__" :
  armstrong_num(153)
  armstrong_num(1634)
  armstrong_num(10)