class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in dic.items():
            freq[count].append(num)
        
        lst = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                lst.append(num)
                k -= 1
                if k == 0:
                    return lst
        
        