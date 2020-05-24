from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return None
        max_current = nums[0]
        max_global = nums[0]
        for i in range(1, len(nums)):
            if max_current > 0:
                max_current += nums[i]
            else:
                max_current = nums[i]
            if max_global < max_current:
                max_global = max_current
        return max_global
        