class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROW = len(mat)
        COL = len(mat[0])
        curr = [0] * ROW
        curri = [0] * ROW
        for i in range(ROW):
            curr[i] = mat[i][0]
        for _ in range(COL):
            maxi = max(curr)
            for row in range(ROW):
                while curri[row] < COL - 1 and curr[row] < maxi:
                    curri[row] += 1
                    curr[row] = mat[row][curri[row]]
            if min(curr) == max(curr):
                return curr[0]
        return -1
        