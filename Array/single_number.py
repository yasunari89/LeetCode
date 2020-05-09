from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for v in nums:
            if not v in hash_table:
                hash_table[v] = 1
            else:
                hash_table[v] += 1
        for num in hash_table:
            if hash_table[num] == 1:
                return num
        return None
        