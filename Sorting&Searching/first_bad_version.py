# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left = 0
        right = n-1
        while left+1 != right:
            print(left, right)
            length = left + right + 1
            mid = length // 2
            if isBadVersion(mid) == True:
                right = mid
            if isBadVersion(mid) == False:
                left = mid
        out = right if isBadVersion(right) else right+1
        return out
            
        