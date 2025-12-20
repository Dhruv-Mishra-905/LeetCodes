class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch = set()
        lft = 0
        lens = 0

        for rgt in range(len(s)):
            while s[rgt] in ch:
                ch.remove(s[lft])
                lft += 1
            ch.add(s[rgt])
            lens = max(lens, rgt - lft + 1)

        return lens