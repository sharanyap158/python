import math
def kokoEat(arr,k):
        # Code here
        low=1
        high=max(arr)
        while(low<=high):
            div=(low+high)//2
            sum=0
            for num in arr:
                sum+=math.ceil(num/div)
            if(sum<=k):
                high=div-1
            else:
                low=div+1
        return low
arr=list(map(int,input().split()))
k=int(input())
print( kokoEat(arr,k))