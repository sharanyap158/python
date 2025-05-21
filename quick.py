def quickSort(arr,low,high):
        # code here
        if(low<high):
            pindex=partition(arr,low,high)
            quickSort(arr,low,pindex-1)
            quickSort(arr,pindex+1,high)
    
def partition(arr,low,high):
        # code here
    i=low
    j=high
    pivot=arr[low]
    while(i<j):
        while(arr[i]<=pivot and i<high):
            i+=1
        while(arr[j]>=pivot and j>low):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
arr=list(map(int,input().split()))
n=len(arr)
low=0
high=n-1
quickSort(arr,low,high)
print(arr)
    