from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for v in nums:
            if not v in hash_table:
                hash_table[v] = 1
            else:
                hash_table[v] += 1
                return True
        return False