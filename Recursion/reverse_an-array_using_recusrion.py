# Reversee an aray using recursion

# Intuition : what's changing -> position of elements in the array, meaning we need a way to track the elements and then pass them into the recusrsive function

# if left>right : we gotta stop
# else : swap left and right value in the array and then increment left and decrement right by 1 and pass it to the recusrivce call

def reverse_array(arr,left=0,right=None):
  if right == None:
    right=len(arr)-1
  if left > right :
    return arr
  else:
    arr[left],arr[right] = arr[right],arr[left]
    return reverse_array(arr,left+1,right-1)



arr=[5,7,3,2,6,1,5,9,7]
left=0
right=len(arr)-1
res=reverse_array(arr,left,right)

print(res)