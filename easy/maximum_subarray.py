"""

Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

Example 1:

    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: [4, -1, 2, 1] has the largest sum = 6.

Example 2:

    Input: nums = [1]
    Output: 1

"""

"""

Initial Thoughts:
    - initialize variable that keeps track of the largest sum value
    - initialize empty list
    - loop through array
        - for each value, add it to the empty list
        - add all values in empty list together and check if it's greater than the variable from the first bullet point
    
    - return variable from first bullet point

Solution: Brute Force

    - Check every possible subarray and check which one is the max sum
    - takes O(n)^2 time

Solution: Kadane's Algorithm

    - compare the maximum subarray at the end of each index
        - you're comparing the subarray at the current index with the maximum subarray before/including the current index



"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_curr = 0
        max_global = 0

        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            if max_curr > max_global:
                max_global = max_curr

        return max_global


