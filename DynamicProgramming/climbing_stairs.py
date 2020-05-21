class Solution:
    def __init__(self):
        self.memo = []
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if len(self.memo) <= n:
            tmp = [None for _ in range(n-len(self.memo))]
            self.memo = self.memo + tmp
        if not self.memo[n-1]:
            self.memo[n-1] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n-1]
            