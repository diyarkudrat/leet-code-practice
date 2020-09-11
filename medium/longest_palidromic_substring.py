"""
Problem: Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 100.


Example 1:

    Input: "babad"
    Output: "bab"   /   Note: "aba" is also a valid answer.

Example 2:

    Input: "cbbd"
    Output: "bb"

"""

"""

Solution Thought:
    - palindrome: phrase that reads the same backwards and forwards

    - have empty string variable set to max_string(max length of palin. string)
    - At each iteration, add letter to stored variable(st)
        - if the reverse of the variable == variable
            - if the length of mx_str < st:
                - max_str = st
        - go onto next iteration
    return max_str

    - Above has a runtime of O(n)^2


"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_str = ""
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                string = s[i:j]
                if string == string[::-1]:
                    if len(max_str) < len(string):
                        max_string = string

        return max_str


