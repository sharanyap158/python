def getfloor(a,x,n):
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low + high)//2
        if(a[mid]<=x):
            ans=a[mid]
            low=mid+1
        else:
            high=mid-1
    return ans 
def getceil(a,x,n):
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]>=x):
            ans=a[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
a=list(map(int,input().split()))
x=int(input())
n=len(a)
print(getfloor(a,x,n))
print(getceil(a,x,n))