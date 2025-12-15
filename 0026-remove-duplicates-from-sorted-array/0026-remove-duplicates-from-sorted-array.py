class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        c=1
        for i in range (1,l):
            if nums[i]!= nums[i-1]:
                nums[c]=nums[i]
                c +=1
        return c
        