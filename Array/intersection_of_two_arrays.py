from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        hash_table = {}
        for v in nums2:
            if not v in hash_table:
                hash_table[v] = 1
            else:
                hash_table[v] += 1
        
        output = []
        for v in nums1:
            if v in hash_table:
                if hash_table[v] > 0:
                    output.append(v)
                    hash_table[v] -= 1
        return output