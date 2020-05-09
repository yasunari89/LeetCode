from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in reversed(range(len(digits))):
            if carry:
                if digits[i] == 9:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0,1)
                else:
                    digits[i] += 1
                    carry = False
        return digits