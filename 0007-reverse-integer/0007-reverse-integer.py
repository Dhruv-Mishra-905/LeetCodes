class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n=str(x)
        rev = n[::-1]
        if rev[-1]=="-":
            rev=rev[-1] + rev[:-1]
        rev = int(rev)
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        return rev

        