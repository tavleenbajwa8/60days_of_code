##Question 
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""

##Solution

def twoSum(nums,target):
    d = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in d:
            return d[rem], i
        else:
            d[nums[i]] = i   

#Test case-1
nums_1 = [3,2,4]
target_1 = 6

#Test case-2
nums_2 = [2,7,11,15]
target_2 = 9

#Result
result_1 = twoSum(nums_1, target_1)
result_2 = twoSum(nums_2, target_2)

print(list(result_1))
print(list(result_2))
