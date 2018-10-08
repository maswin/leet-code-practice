# https://leetcode.com/problems/palindrome-pairs/description/

from collections import defaultdict


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = set()
        word_map = defaultdict(lambda: None)
        for i, w in enumerate(words):
            word_map[w] = i
        # print(word_map)
        for i in range(len(words)):
            l = 0
            r = 0
            word = words[i]
            # print("Word : " + word)
            while(l <= r):
                x = word[l:r]
                # print("small word : " + x)
                rev_x = x[::-1]
                x_id = word_map[rev_x]
                # print("rev id : " + str(x_id))
                if x_id != None and x_id != i:
                    # print("Existing rev word : " + rev_x)
                    new_word = word + rev_x
                    if new_word == new_word[::-1]:
                        # print("Palindrome " + new_word)
                        ans.add((i, x_id))
                    new_word = rev_x + word
                    if new_word == new_word[::-1]:
                        # print("Palindrome " + new_word)
                        ans.add((x_id, i))
                if r < len(word):
                    r += 1
                else:
                    l += 1
        return list(ans)


print(Solution().palindromePairs(["a", "b", "c", "ab", "ac", "aa"]))
