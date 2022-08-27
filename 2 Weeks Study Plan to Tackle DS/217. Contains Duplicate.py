"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        for i in range(len(nums)):
            a = count(nums[i])
            if (a >= 2):
                return True
        return False
        
        import numpy as np
        new_arr = np.unique(nums)
        
        return len(new_arr) != len(nums)
        
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False
        
        for i in nums:
            if nums.count(i) >= 2:
                return True
        return False
        """
        
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False
               
