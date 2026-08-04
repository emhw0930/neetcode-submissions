class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digit(num):
            result = 0
            while num:
                result += (num % 10) ** 2
                num = num // 10
            return result
        visited = set()
        while n not in visited:
            visited.add(n)
            if n == 1:
                return True
            n = square_digit(n)
        return False

        