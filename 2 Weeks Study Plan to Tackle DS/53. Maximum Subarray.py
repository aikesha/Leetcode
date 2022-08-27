"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxV, tot = nums[0], 0
                
        for i in nums:
            if tot < 0:
                tot = 0
            tot += i
            maxV = max(maxV, tot)
                    
        return maxV
    

                
        
               
