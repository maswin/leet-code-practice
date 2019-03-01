# https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not head:
            return None

        # Check if list is of size k
        ptr = head
        k_counter = 0
        reached_len = False
        while ptr and (not reached_len):
            ptr = ptr.next
            k_counter += 1
            if k_counter == k:
                reached_len = True
        if not reached_len:
            return head

        # Reverse list
        prev = None
        curr = head
        next = None
        k_counter = 0
        while curr and k_counter < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            k_counter += 1

        head.next = self.reverseKGroup(curr, k)

        return prev
