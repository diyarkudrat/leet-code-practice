"""
Problem: Given a string, find the length of the longest substring without repeating characters.

Example: 

    Input: "abcabcbb"
    Output: 3      longest substring is "abc",which has length of 3

    Input: "bbbbb"
    Output: 1       longest substring is "b", which has length of 1   

"""


"""
Brute Force Solution:
    
    - Examine each subtring in string with double for loop. 
    - Check if substring contains all unique characters by scanning subtring from left to right and keeping a map of visited characters.
    - return max length of subtring with unique characters.

    Time Complexity: 0(n^3)

Better Solution:

    - create empty dictionary and a max_length and start variable equal to 0
    - loop through each character in string
    - check if character is in dictionary and start value <= the value of character in the dictionary
        - if char is in dictionary, set the start variable equal to value of char in dictionary + 1
        - else, max_length equals to max value of max_length and (i - start + 1)
    - return max_length

    Time Complexity: O(n + d)


"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        map = {}
        max_length = start = 0
        
        # loop through each character in string
        for i in range(len(s)):
            # check if chracter is in map and start is <= value of chracter in dicitonary
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            map[s[i]] = i
            
        return max_length