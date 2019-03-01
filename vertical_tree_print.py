# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = defaultdict(list)

        def dfs(root, level, height):
            if not root:
                return
            result[level].append((height, root.val))
            dfs(root.left, level - 1, height + 1)
            dfs(root.right, level + 1, height + 1)
        dfs(root, 0, 0)
        answer = []
        levels = sorted(result.keys())
        for level in levels:
            answer.append(list(map(lambda y: y[1], sorted(result[level]))))
        return answer
