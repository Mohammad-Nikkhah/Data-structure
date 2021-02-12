def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j = i-1
        while j >=0 and arr[j]>key:
            arr[j+1] =arr[j]
            j -= 1
        arr[j+1] =key


# instance of function
arr = [20,21,22,10,9,-1]
insertionSort(arr)
lst=[]
for i in range(len(arr)):
    lst.append(arr[i])
print(lst)