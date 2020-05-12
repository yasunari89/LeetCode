from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in memo:
                return [memo[num2], i]
            else:
                memo[num1] = i