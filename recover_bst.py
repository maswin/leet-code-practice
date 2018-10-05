# https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None
        self.first = None
        self.second = None

    def recoverTreeUtil(self, root):
        if not root:
            return None
        self.recoverTreeUtil(root.left)

        if self.prev and self.prev.val > root.val:
            self.first = self.first if self.first else self.prev
            self.second = root

        self.prev = root
        self.recoverTreeUtil(root.right)

    def swap(self, a, b):
        if not a or not b:
            return
        tmp = a.val
        a.val = b.val
        b.val = tmp

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recoverTreeUtil(root)
        self.swap(self.first, self.second)


def inorder(root):
    if not root:
        return

    print(root.val)
    inorder(root.left)
    inorder(root.right)


if __name__ == "__main__":
    three = TreeNode(3)
    one = TreeNode(1)
    two = TreeNode(2)

    one.left = three
    three.right = two

    inorder(one)

    print("-----------")
    Solution().recoverTree(one)
    print("-----------")

    inorder(one)
