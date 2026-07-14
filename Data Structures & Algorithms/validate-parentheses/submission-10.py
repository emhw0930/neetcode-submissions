class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            stack.append(char)
            if char not in dic.keys():
                if len(stack) <= 1:
                    return False
                curr = stack.pop(-1)
                prev = stack.pop(-1)
                if dic[prev] != curr:
                    return False
        
        if not stack:
            return True
        return False

        