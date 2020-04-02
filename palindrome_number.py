# Question: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Restate Question: Given an integer, check whether the integer reads the same if it's reversed

# Clarifying Questions: Is the return value going to be True or False? Can the integer be a negative?

# Assumptions: Return True or False. Integer can be a negative.

# Brainstorming Solutions:

        # Solution 1:
        
        #       Reverse the given integer.
        #       Check if the given integer equals to reversed integer.
        #       Return True if above is yes, otherwise return False

        # Runtime is 0(log(n)). Space complexity is 0(1) or constant

        #Improvements: Can't really think of any improvements because this is a pretty simple problem


# Example: 

    #   Input: 232

    #   Output: True       Rationale: 232 reversed == 232


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        reversed = str(x)[::-1]
        return str(x) == reversed
