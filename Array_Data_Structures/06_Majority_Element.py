##Question 
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always
exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

##Solution 1 (Brute Force ##High Time Complexity)
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = set(nums)
        d = {}
        for ele in nums_set:
            count = 0
            for num in nums:
                if ele == num:
                    count = count + 1
            d[ele] = count
        return max(zip(d.values(), d.keys()))[1]
        
    ##Solution 2  (Lesser Time complexity) 
    def majorityElement2(self, nums: List[int]) -> int:
        target = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                target = n
            elif n != ele:
                count = count - 1
            else:
                count = count + 1
        return ele
        
        
obj = Solution()
result = obj.majorityElement2([3,2,3])
print(result)
