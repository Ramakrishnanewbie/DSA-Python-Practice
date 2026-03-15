def second_largest(nums):
  #using nums.sort()
  
  nums.sort()
  return nums[-2]  # TC-> O(nlogn), S.C->O(1)


"""======================================================
======================================================="""

def second_largest_method2(nums) :
  ## We will iterate through array once and find the largest. 
  ## In the secodn loop, we will check for values where value is greater than second_largest but less than largest
  
  
  # T.C -> O(N+N) ~ O(N)
  # S.c -> O(1)
  
  largest=nums[0] 
  second_largest=float("-inf")
  
  for i in nums:
    if i > largest:
      largest=i 
      
  for i in nums:
    if i>second_largest and i<largest:
      second_largest=i
      
  return second_largest



def optimal_solution(nums):
  ## Basically in one pass, we will do teh same, find largest value, and when largest value updated, it means that the previous alrgest values was the second_largest values. 
  
  ## Example, say teh largest value currenly is 3, as we iterate, we find that there is an element 8, so what we do is assign s_largest value as the current_largest value and update largest_value to be 8.
  
  ## T.C -> O(N)
  ## S.C -> O(1)
  
  largest=float("-inf")
  
  for i in nums:
    if i > largest:
      second_largest=largest
      largest=i

  return second_largest

nums=[55,32,97,-55,45,32,88,21,93]
res=second_largest(nums)
print(res)

print("======")

res=second_largest_method2(nums)
print(res)


print("=======")
res=optimal_solution(nums)
print(res)