## Print factors for a given number


def print_factors(n):
  lf=[]
  for i in range(1,n+1) :
    if n % i == 0 :
      lf.append(i)
      
  print(lf, "\n")
  

if __name__ == "__main__" :
  print_factors(7)
  print_factors(10)
  print_factors(13)
  print_factors(15)
  print_factors(25)
  print_factors(48)