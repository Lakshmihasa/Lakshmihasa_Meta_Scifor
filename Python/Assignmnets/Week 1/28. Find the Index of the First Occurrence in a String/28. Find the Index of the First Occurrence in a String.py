class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            n=len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+n]==needle:
                    return i