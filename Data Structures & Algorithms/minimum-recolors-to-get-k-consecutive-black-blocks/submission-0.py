class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        result = count
        curr = 0
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                count += 1
            if blocks[curr] == 'W':
                count -= 1
            curr += 1
            result = min(result, count)
        return result


        