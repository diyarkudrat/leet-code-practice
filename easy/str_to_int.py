"""
# Problem: Converts string to an integer

# discards all whitespaces in begining until the first non-whitespace character is found.
# Starting from the non-whitespace character, interprets as many numerical digits as possible as numerical value after a +/- sign.

# whitespace = ' '

# String can contain additional characters after number is formed. These characters are ignored.
"""

"""
    Edge cases: 
        - If str starts with letter or first non-whitespace character is letter, return 0,
        - If str is empty or only contains white spaces, return 0
        - If number is larger than 32-bit, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

"""

# Example Input: " -42"
# Ouput: -42

# Example Input: "4193 with words"
# Output: "4193"

# Example Input: "words and 987"
# Output: "0"

"""

        - variable to hold numbers
        - index value
        - sign value if str includes negative sign

        - variable to hold skipped over whitespace str

        - if str[0] contains neg/pos sign, check if index value is a neg sign
            - if str[0] is negative, change sign variable to negative

            - drop the pos/neg sign
            - if first index is not in nums variable, return 0
        
        - loop through str
            - if the index you are at is not in nums variable,
                - set index equal to the index value
                - break out of loop
        
        - if index != 0:
            - change initial str variable to contain values between 0 and the index variable

        - convert str to int and apply the sign variable

        - check if int is out of range of a 32-bit signed integer

"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        nums = '0123456789'
        index = 0
        sign = 1
        
        try:
            
            x = str.split()[0]  # skips over whitespace in begining of str
            
            # checks if first value is positive or negative. 
            if x[0] in '-+':
                if x[0] == '-':
                    sign = -1
                    
                # drop neg/pos sign
                x = x[1:]
                
                # return 0 if first index is not a number
                if x[0] not in nums:
                    return 0
                
            # find first non-number
            for i in range(len(x)):
                if x[i] not in nums:
                    index = i
                    break
                    
            # shorten if nonnumber is found
            if index != 0:
                x = x[:index]
            
            #convert str to int and apply sign
            y = int(float(x)) * sign
            
            # check if int is out of range of a 32-bit signed integer
            if y > 2**31 - 1:
                return 2**31 - 1
            elif y < -2**31:
                return -2**31
            else:
                return y

        except:
            return 0
