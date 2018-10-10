# https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        N = len(s)
        DP = [[False] * N for i in range(N)]
        for i in range(N):
            DP[i][i] = True
            ans += 1
        for i in range(N-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans += 1
        for size in range(3, N + 1):
            for start in range(N-size+1):
                end = start + size - 1
                if s[start] == s[end] and DP[start+1][end-1]:
                    DP[start][end] = True
                    ans += 1
        return ans


assert Solution().countSubstrings("aaa") == 6
