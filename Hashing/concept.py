# n and m are two list, check how many times m[i] is in n and return

def count_re(n,m):
  # create a dict for n
  n_dict=dict()
  res_dict=dict()
  for i in n:
    n_dict[i]=n_dict.get(i,0)+1

  
  for i in m :
    res_dict[i] = n_dict.get(i,0)
    
  return res_dict


if __name__ == "__main__" :
  n=[5,3,2,2,1,5,5,7,5,10]
  m=[10,111,1,9,5,67,2]
  
  res=count_re(n,m)
  print(res)