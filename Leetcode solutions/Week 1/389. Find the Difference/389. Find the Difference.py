class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = [0] * 26  
        
        for char in s:
            counts[ord(char) - ord('a')] += 1
        
        for char in t:
            idx = ord(char) - ord('a')
            if counts[idx] == 0:
                return char
            counts[idx] -= 1
        
        return ""
        