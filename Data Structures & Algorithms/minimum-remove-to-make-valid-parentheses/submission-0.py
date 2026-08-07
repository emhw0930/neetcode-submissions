class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        result = []
        for i in range(len(s)):
            if s[i] == ')' and count == 0:
                continue
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
            result.append(s[i])
        count = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] == "(" and count == 0:
                result.pop(i)
                continue
            if result[i] == ")":
                count += 1
            elif result[i] == "(":
                count -= 1
        return "".join(result)