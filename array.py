def findMaximum(arr,low,high):
  max=arr[low]
  i=low
  for i in range(high+1):
    if arr[i]>max:
      max=arr[i]
  return max
arr=[1,30,40,50,60,70]
n=len(arr)
print("the maximum element is %d"% findMaximum(arr,0,n-1))
