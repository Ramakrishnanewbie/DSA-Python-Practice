## T.C -> O(N)
## S.C -> O(1)


def check(nums):
  # Condition 1 : If array is sorted in ascending
  for i in range(len(nums)-1):
    if nums[i] <nums[i+1]:
      asc=True
    else:
      asc=False
      break
  
  
  # Condition 2 : If array is sorted in descending
  for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
      desc=True
    else:
      desc=False
      break
    
  return asc,desc
  
  
nums=[3,5,6,8,9,10,20]
asc,desc=check(nums)

print(asc,desc)

print("=====")

nums=[1,2,5,8,3,10,14,15]
asc,desc=check(nums)

print(asc,desc)