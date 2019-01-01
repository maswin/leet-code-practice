# https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/

import sys


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        cities = [[] for _ in range(n)]
        for s, d, c in flights:
            cities[s].append((d, c))

        distances_from_src = [sys.maxsize for _ in range(n)]
        distances_from_src[src] = 0
        for stop in range(K + 1):
            new_distances_from_src = distances_from_src[:]
            change = False
            for city in range(n):
                for a_city, a_city_cost in cities[city]:
                    new_cost = a_city_cost + distances_from_src[city]
                    if new_cost < new_distances_from_src[a_city]:
                        new_distances_from_src[a_city] = new_cost
                        change = True
            distances_from_src = new_distances_from_src
            if not change:
                break

        cost = distances_from_src[dst]
        return cost if cost != sys.maxsize else -1


assert Solution().findCheapestPrice(
    3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200

assert Solution().findCheapestPrice(
    3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500
