"""
Problem: Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example:

    Input: 3
    Output: "III"

    Input: 4
    Output: "IV"

    Input: 58
    Output: "LVIII"

"""

"""
Solution #1: 

    - 2 lists 
        - One list is of the number values. Add special case values in number value list for edge cases(900, 400, 40, 9, 4).
        - Second list is of the roman numerals corresponding with the number values list

    - Empty list for output

    - Loop through each index of the number values list
        - initialize variable to store number value at each index(coin)
        - Loop through each index until the initialized variable is less than the num input

        - While num input is >= coin,
            - Subtract coin from num input
            - add the index value of where the while loop started from the roman numeral list to empty list
    
    - return .join of output list


"""

"""
Variable Table:
    
    input: 3

        i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        num = 3, 2, 1
        track = 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        output = ["I"] ["I", "I"], ["I", "I", "I"]
        return value => "III"


"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        num_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        output = []

        for i in range(len(num_vals)):
            track = num_vals[i]

            while num >= track:
                num -= track

                output.append(roman_num[i])

        return "".join(output)