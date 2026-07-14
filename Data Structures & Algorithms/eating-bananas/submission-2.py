class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # when speed decreases, less hour left
        # when speed increases, more hour left
        # find the least speed  

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = l + ((r - l) // 2)
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / m)
            if totalHours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res