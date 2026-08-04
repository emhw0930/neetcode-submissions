class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        remain = 0
        while n > 1:
            remain = n % 2
            n = n // 2
            if remain:
                return False
        return True