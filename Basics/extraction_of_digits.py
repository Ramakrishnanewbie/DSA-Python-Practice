# Extracttion of digits from a number

def extract_digits(n):
    if(n>0):
      print(n%10)
      extract_digits(n // 10)
    else:
      exit
    
    

if __name__=="__main__":
  extract_digits(543)