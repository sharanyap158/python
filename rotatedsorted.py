def search(arr,key):
        # Complete this function
        n=len(arr)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==key):
                return mid
                #left half is sorted
            elif(arr[low]<=arr[mid]):
                if(arr[low]<=key<=arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
                #right half is sorted 
            elif(arr[mid]<=arr[high]):
                if(arr[mid]<=key<=arr[high]):
                    low=mid+1
                else:
                    high=mid-1
        return -1
arr=list(map(int,input().split()))
key=int(input())
print(search(arr,key))  