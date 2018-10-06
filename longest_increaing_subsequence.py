#https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        DP = [0] * N
        DP[0] = 1
        max_val = 1
        for i in range(N):
            this_max = 1
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    this_max = max(this_max, DP[j] + 1)
            DP[i] = this_max
            max_val = max(this_max, max_val)
        # print(DP)
        return max_val


assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert Solution().lengthOfLIS([1, 2]) == 2
assert Solution().lengthOfLIS([-2, -1]) == 2
