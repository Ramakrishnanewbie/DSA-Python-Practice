# nums = [1,2,3,4,5,6,7,8,1,1]


def store_frequencies(nums):
  dictionary={}
  for i in nums :   # For T.C for takes O(N) and if and else takes O(1) , so overall time takes O(N) and SC is O(N) 
    if i not in dictionary:
      dictionary[i]=1
    else:
      dictionary[i]+=1
      
  return dictionary


def method2(nums): # T.C and S.C is same, O(N)
  dictionary=dict()
  for i in nums:
    dictionary[i] = dictionary.get(i,0)+1
    
  return dictionary


if __name__== "__main__" :
  nums=[1,1,1,2,3,2,3,4,5,5,4,6,7,8,7,7,6,6,8]
  result=store_frequencies(nums)
  
  print(result)
  
  
  result2= method2(nums)
  print(result2)
