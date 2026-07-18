class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        TO = n + 1
        for i in range(1, TO):
            n -= i
            if n < 0:
                return i - 1