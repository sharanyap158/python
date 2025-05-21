def numsub(nums,target):
    MOD=10**9+7
    nums.sort()
    n=len(nums)
    power=[1]*n
    for i in range(1,n):
        power[i]=(power[i-1]*2)%MOD
    left=0
    right=n-1
    count=0
    while left <= right:
        if nums[left]+nums[right]<= target:
            count=(count+power[right-left])%MOD
            left += 1
        else:
            right -= 1
    return count
nums=list(map(int,input().split()))
target=int(input())
print(numsub(nums,target))