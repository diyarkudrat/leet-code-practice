"""
Problem: Given a 32-bit signed integer, reverse digits of an integer.

Can only store integers within 32-bit signed integer range: [-2^31, 2^31 - 1].

Example:

    Input: 123
    Output: 321

    Input: -123
    Output: -321

    Input: 120
    Output: 21

"""

"""
Solution #1: Int to str, reverse str, convert back to int

    - Create variable that'll hold the sign of the input number. Initial value will be 1, assuming positive
    - convert input int to str
    - check if beginning of str contains negative sign
        - If it does, change sign variable to -1
        - Drop the negative sign in the str
    - reverse the str
    - convert reversed str back into int and multiply by sign variable
    - if reversed_int is outside of 32-bit integer range, return 0
    - otherwise return the reversed_int

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        num_str = str(x)
        
        if num_str[0] in '-+':
            if num_str[0] == '-':
                sign = -1
            
            num_str = num_str[1::]
        
        reversed_num_str = num_str[::-1]
        reversed_num_int = int(reversed_num_str) * sign
        
        if reversed_num_int > 2**31 - 1:
                return 0
        elif reversed_num_int < -2**31:
            return 0
        else:
            return reversed_num_int
        