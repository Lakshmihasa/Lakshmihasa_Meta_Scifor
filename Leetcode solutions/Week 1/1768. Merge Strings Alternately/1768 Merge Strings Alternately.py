class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ''
        i = 0
        while i < len(word1) and i < len(word2):
            merged += word1[i] + word2[i]
            i += 1
        merged += word1[i:] + word2[i:]
        return merged