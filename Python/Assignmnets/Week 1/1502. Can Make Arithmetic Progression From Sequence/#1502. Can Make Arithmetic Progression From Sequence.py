class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Sort the array
        arr.sort()

        # Calculate the common difference
        common_diff = arr[1] - arr[0]

        # Check if all differences between consecutive elements are the same
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != common_diff:
                return False

        return True