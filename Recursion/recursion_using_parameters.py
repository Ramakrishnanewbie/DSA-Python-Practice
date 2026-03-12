# Recusrsion using Parameters [Print x, N times]


def print_x_n_times(x,n):
  if(n>0):
    print(x)
    print_x_n_times(x,n-1)
  else:
    return
    

if __name__ == "__main__" :
  print_x_n_times(15,3)
  
  


