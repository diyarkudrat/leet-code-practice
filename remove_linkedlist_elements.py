"""

Problem: Remove all elements from a linked list of integers that have value val.

Example:

    Input: 
        1->2->6->3->4->5->6, val = 6

    Output:
        1->2->3->4->5

"""

"""
Solution:
    - start at head node
    - loop through linked list
        - if current node's value equals to given value,
            have the current node's next pointer point to the next node's next pointer
            (current.next = current.next.next)
        - otherwise, set current node to next node

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head, head.next = ListNode(0), head
        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head.next