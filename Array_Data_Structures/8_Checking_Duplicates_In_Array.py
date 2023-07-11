##Question: Contains Duplicates 

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

'''

##Brute force approach
def duplicates_brute(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1,2,3,1]
result_brute = duplicates_brute(nums)
print(result_brute)



##Sorting Approach
def duplicates(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


nums = [1,2,3,1]
result = duplicates(nums)
print(result)


##Set Approach

def duplicates1(nums):
    if len(nums) != len(set(nums)):
        return True
    return False

nums = [1,2,3,1]
result1 = duplicates1(nums)
print(result1)

