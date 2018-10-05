# https://leetcode.com/problems/base-7/description/


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        ans = ""
        is_negative = num < 0
        if is_negative:
            num = num * -1
        while num != 0:
            ans = str(num % 7) + ans
            num = num // 7
        return "-" + ans if is_negative else ans


assert Solution().convertToBase7(100) == "202"
assert Solution().convertToBase7(-7) == "-10"
assert Solution().convertToBase7(0) == "0"
