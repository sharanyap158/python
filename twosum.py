'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 #array should be in sorted order
 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

#BRUTE FORCE METHOD 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):# target=i+j then i=target-j
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
    #time complexity-O(N^2)
    #space compleity-O(1)
#it cannot be as efficient as possible so lets do it in hashing method
#METHOD-2-HASHING TECHNIQUE
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for a in range(0,n):
            b=target-nums[a] 
            if (b in d):#HERE IT TAKES INDEX, VALUE= target = a+b == b = target-a
                return (a,d[b]) #a,d is val,index which gives b
            else:
                d[nums[a]]=a
#time complexity - O(N)
#space complexity- O(N)
#after using hashing the space and time complexity got reduced and it reduces space complexity 
#here ans can be returned in any format 
#here we are again using space so we need optimal solution

#method 3 2 pointer technique-this technique is used to decrease space complexity
def twosums(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while(low<high):
        sum=nums[low]+nums[high]
        if(sum==target):
            return [low,high]#we can also use yes if indexes are there also can use YES and also it can be in dic()
        elif(sum>target):
            high -= 1
        elif(sum<target):
            low += 1
    return "No"
            
nums=list(map(int,input().split()))
target=int(input())
twosums(nums,target)
print(twosums(nums,target))
#TIME COMPLEXITY IS O(LOG n)
#SPACE COMPLEXITY IS O(1)
'''