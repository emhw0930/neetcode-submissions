class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) < 3:
            if n == 0:
                return True
            elif n == 1 and sum(flowerbed) == 0:
                return True
            return False
        if flowerbed[1] == 0 and flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1
            if n == 0:
                return True 
        for i in range(1, len(flowerbed) - 1):
            prev, nex = i - 1, i + 1
            if flowerbed[prev] + flowerbed[i] + flowerbed[nex] == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            if n == 0:
                return True 
        return False

        