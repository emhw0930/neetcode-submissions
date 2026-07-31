class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dmap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
                '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if digits == "":
            return []
        self.result = []
        def dfs(curr, index):
            if index == len(digits):
                self.result.append(curr)
                return
            for char in dmap[digits[index]]:
                dfs(curr + char, index + 1)
        dfs("", 0)
        return self.result
        