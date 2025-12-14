class Solution(object):
    def romanToInt(self, s):
        s=s.lower()
         roman = {
            'i': 1,'v': 5,'x': 10,'l': 50,'c': 100,'d': 500,'m': 1000
        }
        total = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]  
            else:
                total += roman[s[i]]  
        return total