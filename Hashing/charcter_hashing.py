# Character hashing 

# Question: Given a string s and a list of characters q, return a dictionary with the count of each character in q that appears in s.

def charhash(s,q):
  s_dict=dict()
  res_dict=dict()
  for i in s:
    s_dict[i]=s_dict.get(i,0)+1
    
  for character in q:
    res_dict[character]=s_dict.get(character,0)
    
    
  return res_dict


if __name__ == "__main__" :
  s="azyxyyzaaaa+A"
  q=["d","a","y","x","z","A","X","+"]
  
  res=charhash(s,q)
  
  print(res)
