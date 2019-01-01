# https://leetcode.com/problems/redundant-connection


class DisjointSet:
    def __init__(self, number_of_nodes):
        self.parent = [x for x in range(number_of_nodes + 1)]
        self.rank = [1] * (number_of_nodes + 1)

    def find(self, element):
        if (self.parent[element] != element):
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, x, y):
        xp = self.parent[self.find(x)]
        yp = self.parent[self.find(y)]
        if self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            if self.rank[xp] == self.rank[yp]:
                self.rank[yp] += 1


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        number_of_nodes = max([node for edge in edges for node in edge])
        disjoin_set = DisjointSet(number_of_nodes)
        for edge in edges:
            if disjoin_set.find(edge[0]) == disjoin_set.find(edge[1]):
                return edge
            disjoin_set.union(edge[0], edge[1])
        return None
