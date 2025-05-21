'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
'''
#Program:
#Method- using 3 for loops
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplet_sum=set()
        n=len(nums)
        for i in range(0,n-2):#5-2=3
            for j in range(i+1,n-1):#5-1=4
                for k in range(j+1,n):#5 index is 4
                    if(nums[i]+nums[j]+nums[k]==0):
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()#as the set need to be sorted and to eliminate duplicates 
                        triplet_sum.add(tuple(temp))#changing list to tuple
        ans=[]
        for triplet in triplet_sum:
            ans.append(list(triplet))
        return ans
        #time complexity=t(n)-O(N^3)
        #Space complexity=S(N)-O(N)
        '''
'''
#HASHING METHOD - USING 2 FOR LOOPS       
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplet_sum=set()
        n=len(nums)
        for i in range(0,n-2):#5-2=3
            hashmap=[]
            for j in range(i+1,n-1):#5-1=4
                k  =- (nums[i]+nums[j])
                if(k in hashmap)):
                    temp=[nums[i],nums[j],k]
                    temp.sort()#as the set need to be sorted and to eliminate duplicates 
                    triplet_sum.add(tuple(temp))#changing list to tuple
        ans=[]
        for triplet in triplet_sum:
            ans.append(list(triplet))
        return ans # using 2 for loops time limit exceeded
        '''
'''
#METHOD-3- 3 POINTERS 
#PROGRAM:
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans=[]
        for i in range(0,n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if (sum<0):
                    j += 1
                elif(sum>0):
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while(j<k and nums[j+1]==nums[j]):
                        j+=1
                    while(j<k and nums[k-1]==nums[k]):
                        k-=1
        return ans
        #TIME COMPLEXITY - O(LOG N)
        #SPACE COMPLEXITY- O(1)
    '''
