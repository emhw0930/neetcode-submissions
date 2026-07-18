class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        directions = [[1, 0], [0, -1], [-1, 0]]
        dx, dy = [0, 1]
        x, y = [0, 0]
        count = 1
        while count <= n * n:
            result[x][y] = count
            tempx, tempy = x, y
            x, y = x + dx, y + dy
            if not(0 <= x < n and 0 <= y < n and result[x][y] == 0):
                directions.append([dx, dy])
                dx, dy = directions.pop(0)
                x, y = tempx + dx, tempy + dy
            count += 1
        return result
            
