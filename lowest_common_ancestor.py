# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def find_common_ancestor(root):
            # Base case
            if not root:
                return (False, False, None)

            # Left subtree
            (lpFound, lqFound, lca) = find_common_ancestor(root.left)
            if lca:
                return (True, True, lca)

            # Right subtree
            (rpFound, rqFound, rca) = find_common_ancestor(root.right)
            if rca:
                return (True, True, rca)

            # Root
            pFound = lpFound or rpFound or root.val == p.val
            qFound = lqFound or rqFound or root.val == q.val

            if pFound and qFound:
                return (True, True, root)
            else:
                return (pFound, qFound, None)

        (_, _, lca) = find_common_ancestor(root)
        return lca
