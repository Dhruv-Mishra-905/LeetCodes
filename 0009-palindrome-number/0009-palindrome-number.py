class Solution(object):
    def isPalindrome(self, x):
        org=str(x)
        rev=str(x)[::-1]
        bool=False
        if(rev==org):
            bool=True
        return bool
