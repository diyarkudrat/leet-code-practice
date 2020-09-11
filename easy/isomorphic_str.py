"""

Problem: Given two strings s and t, determine if they are isomorphic.

        Two strings are isomorphic if the characters in s can be replaced to get t.


Example:

    Input: s = "egg", t = "add"
    Output: True

    Input: s = "foo", t = "bar"
    Output: False

    Input: s = "paper", t = "title"
    Output: True



"""

"""
Solution:

    - base case
        - if length of both strings aren't the same, return False
    - initialize 2 empty dictionaries
    - compare each letter in each word to each other
        - i.e for the first example above, compare e and a, g and d
    - if the letter in the first string is in dictionary #1 
        and its value is the letter in the second string, return False
    - otherwise, add the two letters in the dictionary. Key is letter from first string, Value is letter from second string
    - Repeat the 2 steps above but for dictionary #2
        - if the letter in the second string is in dictionary #2 
        and its value is the letter in the first string, return False
        - otherwise, add the two letters in the dictionary. Key is letter from second string, Value is letter from first string
    - Return True at end of function


"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dic1 = {}
        dic2 = {}
        
        for i, j in zip(s, t):
            if i in dic1 and dic1[i] != j:
                return False
            else:
                dic1[i] = j
                
        for i,j in zip(s, t):
            if j in dic2 and dic2[j] != i:
                return False
            else:
                dic2[j] = i
                
        return True