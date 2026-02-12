class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        pref=strs[1:]
        for ele in strs:
            while ele.find(pref) != 0:
                pref= pref[:-1]
                if pref == "":
                    return ""
        return pref

        