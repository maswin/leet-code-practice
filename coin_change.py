# https://leetcode.com/problems/coin-change/description/


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        DP = [amount + 1] * (amount + 1)
        DP[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    DP[i] = min(DP[i], DP[i-coin] + 1)
        return DP[amount] if DP[amount] != amount + 1 else -1


assert Solution().coinChange([1, 2, 5], 11) == 3
