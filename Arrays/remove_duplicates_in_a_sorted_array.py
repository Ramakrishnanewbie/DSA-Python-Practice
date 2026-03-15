def remove_sorted_duplicates(nums):
  
  dictio=dict()
  
  for i in nums:
    dictio[i]=dictio.get(i,0)
    
  for j, key in enumerate(dictio.keys()):
    nums[j]=key
    
  return j+1,nums
  

  


def method2(nums): # T.C -> O(N), S.C -> O(1)
    i = 0  # write pointer (last unique)
    j = 1  # scan pointer

    while j < len(nums):
        if nums[j] == nums[i]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]  # no need to swap, just overwrite
            j += 1

    return i + 1, nums


nums=[1,1,1,2,3,4,4,7,9,9,9,10]

res,x=method2(nums)
    
print(res)

print("=====")

print(x)