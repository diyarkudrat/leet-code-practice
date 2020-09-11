"""
Given an array nums of n integers, are there elements a,b,c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Solution set must not contian duplicate triplets.

0 <= nums.length <= 300

Example 1:

    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0 1]]

Example 2:

    Input: nums = []
    Output: []

Example 3:

    Input: nums = [0]
    Output: []
"""

"""
Initial Thoughts:
    - initialize empty set
    - Loop through list
    - at each iteration, add two numbers together, subtract from 0, and check if that value is in the list
"""

"""
Solution:
    
    - Sort list
    - loop through list
    - 2 pointers: left and right pointers
    - left = i + 1, right = last element in list
    - add those three elements together
    - if total sum < 0, add 1 to left pointer
    - if total sum > 0, subtract 1 from right pointer
    - if total sum = 0, add those three elements in a list, within a list

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
        return result


            
            
        

        