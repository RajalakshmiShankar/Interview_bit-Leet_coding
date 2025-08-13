class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        newstring = str(x)
        reversedstring = newstring[::-1]
        
        return newstring == reversedstring
        