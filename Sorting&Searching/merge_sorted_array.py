from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return 
        for num2 in reversed(nums2):
            for i in range(m+n-1, -1, -1):
                if m <= i:
                    if nums1[m-1] <= num2:
                        nums1.insert(m, num2)
                        nums1.pop()
                        break
                if i <= m-1:
                    if nums1[m-1-i] >= num2:
                        nums1.insert(m-1-i, num2)
                        nums1.pop()
                        break
                    
                