# Find the largest element in the array 


def find_largest(nums):
  largest=nums[0]
  for i in nums:
    if i>largest:
      largest=i
  return largest


def method2(nums):
  largest=float("-inf")
  for i in nums:
    if i >largest:
      largest=i
  
  return largest


nums=[1,2,6,99,5,3,101,3995,4,5,2,1,67]
res=find_largest(nums)
print(res)

print("======")
res=method2(nums)
print(res)



