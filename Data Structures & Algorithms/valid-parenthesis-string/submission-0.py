class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1 # let * be ")"
                leftMax += 1 # let * be "("
            if leftMax < 0: # meaning that there must be ")" before its "("
                return False
            if leftMin < 0: # if pass leftMax, meaning that we let too much * be ")"
                leftMin = 0
        
        return leftMin == 0