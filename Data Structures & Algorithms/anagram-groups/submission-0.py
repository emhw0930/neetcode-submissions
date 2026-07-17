class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary: key = sorted string | value = list of words
        dic = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            dic[tuple(sorted_word)].append(word)
        result = []
        for key, value in dic.items():
            result.append(value)
        return result


        