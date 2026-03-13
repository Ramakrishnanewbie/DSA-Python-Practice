## Factorial

# given is n , we have to find n x n-1 x n-2 .....1

# Notice that when n=1, the value to multiply is 1, otherwise n*fnc(n-1)


def facto(n):
  if n==1 or n==0: 
    return 1
  else:
    return n*facto(n-1)

    
res=facto(5)
print(res)