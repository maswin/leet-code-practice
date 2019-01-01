# https://leetcode.com/problems/maximum-subarray/submissions/

import sys


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = nums[0]
        N = len(nums)
        this_sum = nums[0]
        for i in range(1, N):
            this_sum = max(this_sum + nums[i], nums[i])
            if this_sum > max_sum:
                max_sum = this_sum
        return max_sum
