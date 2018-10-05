# https://leetcode.com/problems/interleaving-string/description/


class Solution:

    def isInterleaveUtil(self, s1, s2, s3, interleave_str, s1_pos, s2_pos, memo):
        if s1_pos < len(s1) and s2_pos < len(s2):
            if memo[s1_pos][s2_pos]:
                return False
            memo[s1_pos][s2_pos] = True

        if s1_pos == len(s1) and s2_pos == len(s2) and interleave_str == s3:
            return True

        ans = False
        if s1_pos < len(s1) and s3[s1_pos + s2_pos] == s1[s1_pos]:
            ans |= self.isInterleaveUtil(
                s1, s2, s3, interleave_str + s1[s1_pos], s1_pos + 1, s2_pos, memo)

        if not ans and s2_pos < len(s2) and s3[s1_pos + s2_pos] == s2[s2_pos]:
            ans |= self.isInterleaveUtil(
                s1, s2, s3, interleave_str + s2[s2_pos], s1_pos, s2_pos + 1, memo)

        return ans

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo = [[False] * (len(s2)) for i in range(0, len(s1))]
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveUtil(s1, s2, s3, "", 0, 0, memo)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
assert not Solution().isInterleave(s1, s2, s3)
