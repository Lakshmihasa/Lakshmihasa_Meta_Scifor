class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_increasing = False
        is_decreasing = False
        n = len(nums)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                is_decreasing = True
            elif nums[i] < nums[i+1]:
                is_increasing = True

            if(is_increasing and is_decreasing):
                return False

        return True
        