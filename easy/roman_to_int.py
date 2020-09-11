"""

Problem: Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

"""

"""
Examples:

    Input: "III"
    Output: 3

    Input: "IV"
    Output: 4

    Input: "LVIII"
    Output: 58
    Explanation: L = 50, V = 5, III = 3 

"""

"""
Solution:
    - Create dictionary of roman to integer values
    - initialize two variables, one for previous value and another for the total sum
    - loop through given string in reverse order
        - set a variable for the value at current index
        - if previous is greater than current index value,
            - subtract current from the total sum
        - otherwise, add current to total sum
        - set previous equal to current
    - return total sum
"""


def romanToInt(self, s):
    """
    Time complexity analysis: O(n) because you are looping through given string for one iteration. 
                            The rest of the code is assigning values and math operations, which takes constant time.
    """
    val_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    previous = 0
    total = 0
    for i in s[::-1]:
        current = val_dict[i]
        if previous > current:
            total -= current
        else:
            total += current
        previous = current
    return total