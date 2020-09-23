"""

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

"""

"""

Input: nums = [1, 0, -1, 0, -2, 2], target = 0

Output: [
            [-1,  0, 0, 1],
            [-2, -1, 1, 2],
            [-2,  0, 0, 2]
        ]

"""


class Solution(object):
    def fourSums(self, nums, target):
        nums_dict = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 in nums_dict:
                    nums_dict[sum2].append((i, j))
                else:
                    nums_dict[sum2] = ([i, j])

        result = set()
        for key in nums_dict():
            value = target - key
            list1 = nums_dict[key]
            list2 = nums_dict[value]
            for i, j in list1:
                for k, l in list2:
                    if i != k, i != l, j != k, j != l:
                        final_list = [nums[i], nums[j], nums[k], nums[l]]
                        final_list.sort()
                        result.add(final_list)

            return list(result)
