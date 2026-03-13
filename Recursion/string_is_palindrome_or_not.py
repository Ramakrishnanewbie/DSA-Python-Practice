## Check if string is pallindrome or not using recusrsion

## Intuition : What's the one that's changing ? we are basically checking the values of sttring from front and back and if theya re uneqqual return false, elese keep chacking until left == right and then  return true


def check_pal(s,left,right):
  if left >= right :
    return True
  else:
    if s[left] != s[right] :
      return False
    return check_pal(s,left+1,right-1)
    
    
    
st="abba"
l=0
r=len(st)-1    
res=check_pal(st,l,r)
print(res)