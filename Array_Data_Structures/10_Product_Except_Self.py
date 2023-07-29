##Function calling 
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


def productExceptSelf(nums):
  zeroes = 0
  full_product = 1

  for idx, i in enumerate(nums):
    if i == 0:
      zeroes += 1
      if zeroes > 1:
        print([0]*len(nums))
        if zeroes > 1:
          print([0]*len(nums))
        position = idx
        else:
            full_product *= i

      if zeroes:
          result = [0] * len(nums)
          result[position] = full_product

      else:
          result = [full_product//i for i in nums]
    
    return result 
