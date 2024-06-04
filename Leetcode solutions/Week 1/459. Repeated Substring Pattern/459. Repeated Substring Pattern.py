class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Concatenate the string with itself
        doubled_s = s + s

        # Remove the first and last characters
        modified_s = doubled_s[1:-1]

        # Check if the original string appears in the modified string
        return s in modified_s
        