class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapi = defaultdict(int)
        l = 0
        result = 0
        for r in range(len(fruits)):
            mapi[fruits[r]] += 1
            while len(mapi) > 2:
                mapi[fruits[l]] -= 1
                if mapi[fruits[l]] == 0:
                    del mapi[fruits[l]]
                l += 1
            result = max(result, r - l + 1)
        return result