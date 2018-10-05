# https://leetcode.com/problems/word-break/description/


class Solution:
    def __init__(self):
        self.soln = []

    def wordBreakUtil(self, s, wordDict, cache, start_index, soln):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if start_index >= len(s):
            self.soln.append(soln)
        if not cache[start_index] is None:
            return cache[start_index]
        ans = False
        for index in range(start_index+1, len(s) + 1):
            word = s[start_index:index]
            if word in wordDict:
                soln.append(word)
                self.wordBreakUtil(s, wordDict, cache, index, soln)
                soln.pop()
        cache[start_index] = ans

    def wordBreak(self, s, wordDict):
        cache = [None] * len(s)
        return self.wordBreakUtil(s, wordDict, cache, 0, [])


s = "leetcode"
wordDict = ["leet", "code"]
assert Solution().wordBreak(s, wordDict)

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
assert not Solution().wordBreak(s, wordDict)

s = "applepenapple"
wordDict = ["apple", "pen"]
assert Solution().wordBreak(s, wordDict)
