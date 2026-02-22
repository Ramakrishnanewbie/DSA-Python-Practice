# Counting number of digits

## Generic one
def count_digits(n):
  c=0
  if(n==0):
    c=1
  while(n != 0):
    c+=1
    n=n//10
  print(c)
  
  
## Interesting way
## Calculate log base 10 of a number and add 1 and take real part (convert to integet)
from math import *
def count_digits_2(n):
  print(int(log10(n)+1))
    

if __name__ == "__main__":
  count_digits_2(1)