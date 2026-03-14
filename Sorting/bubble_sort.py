# Bubble Sort -> Side by side comparison


def bubble(nums):
  n=len(nums)
  i=n-1
  j=0
  while(j<i):
    #cehck nums[j] and nums[j+1]
    if(nums[j+1] <nums[j]):
      nums[j],nums[j+1]=nums[j+1],nums[j]
      j+=1

  # when j = i compare j and j+1 again and swap if necessary
  if(nums[j+1] <nums[j]):
    nums[j],nums[j+1]=nums[j+1],nums[j]
  j=0
  
    
nums=[5,6,2,3,9,0,1]
#     j         i