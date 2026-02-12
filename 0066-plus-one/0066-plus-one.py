class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        v=0
        arr = []
        for i in digits:
            v=v*10+i
        v=v+1
        while v != 0:
            arr.append(v % 10)
            v /=10
        return arr[::-1]
        