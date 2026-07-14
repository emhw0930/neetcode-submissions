class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        dicSorted = dict(sorted(dic.items(), reverse=True, key=lambda item: item[1]))
        
        sortedList = list(dicSorted.keys())

        returnList = []

        for i in range(k):
            returnList.append(sortedList[i])
        
        return returnList
        
        