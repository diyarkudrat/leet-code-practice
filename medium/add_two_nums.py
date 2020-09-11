# Question: You are given two non-empty linked lists representing two non-negative integers. 
#           The digits are stored in reverse order and each of their nodes contain a single digit. 
#           Add the two numbers and return it as a linked list.

#           You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Restate Question: Given two linked lists. Both are non-empty, contains positive integers, in reversed order,
                        # and each node contains a single digit. Add the two numbers and return it as linked list.

# Clarifying Questions: Are there any duplicates in the linked lists?

# State Assumptions: There can be duplicates in the linked lists given.

#Example: 
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

    #Output: 7 -> 0 -> 8


# BrainStorm Solutions: 

        # Solution #1: 

        #       For each node in each linked list,
        #       Add its value into a string. Reverse the string
        #       Convert the reversed string back into an integer.
        #       Add up the two integers.
        #       Reverse the order of the result, and then construct linked list from the reversed result.
            
        # Solution #2:

        #       Create a counter and set it equal to 0
        #       Start at head node for both linked lists and iterate through their pointers and the counter.
        #       At each pointer, add up the two values along with the counter, and create a new node for the result.
        #       If result is >= 10, subtract 10 from it, and add one to the counter. You add one so for the next iteration, you can add that leftover from the
        #       the previous one.

        # Even though both solutions have the same time complexity of O(n),
        # Solution #2 is better because solution #1 takes away from the idea of a linked list and solution #2 is cleaner.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node_val = ListNode(0)
        node_val_tail = node_val
        carry_counter = 0
        
        # Loop through value for each node in each linked list
        while l1 or l2 or carry_counter:
            # Extract the value for the node in each linked list
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            # Calculate total value
            total_val = val1 + val2

            # Add the total value and the carryover. If there is a remainder, the remainder will equal to the carryover
            carry_counter, next_node = divmod(total_val + carry_counter, 10)

            # Move on to the next iteration
            node_val_tail.next = ListNode(next_node)
            node_val_tail = node_val_tail.next

            # Return None if next value is None
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return node_val.next 