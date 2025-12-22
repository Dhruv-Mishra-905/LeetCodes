class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        f =nums1+nums2
        f.sort()
        n= len(f)
        if n%2 == 0:
            return (f[n//2 - 1] + f[n//2]) / 2.0
        else:
            return f[n//2]