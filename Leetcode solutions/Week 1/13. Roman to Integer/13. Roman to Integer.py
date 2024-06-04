class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }

        n = len(s)
        ans = 0
        for i in range(n):
            if i < n-1 and mp[s[i]] < mp[s[i+1]]:
                ans-=mp[s[i]]
            else:
                ans += mp[s[i]]

        return ans
        