class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # both even number
        # 4 5 6 7 8 = 2 
        # difference = 4
        # one odd one even
        # 3 4 5 6 7 8 = 3
        # difference = 5
        # both odd number
        # 3 4 5 6 7 = 3
        # difference = 4
        first = low % 2 == 1
        second = high % 2 == 1
        # both even - must be even length
        if first + second == 0:
            return (high - low) // 2
        elif first + second == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2 + 1