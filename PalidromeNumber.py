class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        Newstring = str(x)
        reversedstring = Newstring[::-1]
        
        return Newstring == reversedstring
        