def printArray(arr, n):
    for i in range(0,n):
        print ("%d"%( arr[i]),end=" ")
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
pancakeSort(arr, n);
print ("Sorted Array ")
printArray(arr,n)
 
