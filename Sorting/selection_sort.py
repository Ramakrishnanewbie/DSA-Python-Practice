# Selection Sort

""" 
Intuition : 

nums= [5,7,8,4,1,6,9,2]

Assuming this array is given, we have to sort it using Selection sort. 

So, what happens in selection sort.

start i=0, assume that nums[i] is minimum. 
We se min_index as 0

We iterate from position 1 using j variable and check if there is something smaller. 
So, we 


Basically we start at i=0 and set it as minimum index (by assumption). We will check for the least element after this and put it as j. We check the first occurence and then 
"""


def select_sort(arr):
  n=len(arr)
  for i in range(0,n):
    min_index=i
    for j in range(i+1,n):
      if(arr[j] < arr[min_index]):
        min_index=j
    arr[min_index],arr[i] =arr[i],arr[min_index]
  
  return arr
  
  
def select_sort_desc(arr):
  n=len(arr)
  n=len(arr)
  for i in range(0,n):
    max_index=i
    for j in range(i+1,n):
      if(arr[j] > arr[max_index]):
        max_index=j
      arr[i],arr[max_index]=arr[max_index],arr[i]
    
  return arr
    
nums=[1,3,2,4,6,3,1,9,0]
i=0
j=1
min_index=0
res=select_sort(nums)
    
print(res)

res2=select_sort_desc(nums)
print(res2)
    
  