# Print "Rama" 5 times using recursion

def printr(n):
  if (n>0):
    print(f"Rama,{n}")
    printr(n-1)
  else:
    exit
    
if __name__ == "__main__" :
  printr(5)