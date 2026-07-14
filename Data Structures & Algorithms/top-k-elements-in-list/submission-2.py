class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valToNum = {}
        for n in nums:
            valToNum[n] = valToNum.get(n, 0) + 1
        
        sorted_item = sorted(valToNum.items(), key=lambda item: item[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(sorted_item[i][0])

        return ans