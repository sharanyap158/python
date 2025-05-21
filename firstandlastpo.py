def getLowerBound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def getUpperBound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>target):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
def find(nums,target):
    lb=getLowerBound(nums,target)
    if(lb==-1 and nums[lb] != target):
        return [-1,-1]
    ub=getUpperBound(nums,target)
    return [lb,ub-1]
nums=list(map(int,input().split()))
target=int(input())
print(find(nums,target))