class Solution:
    def isPalindrome(self, x: int) -> bool:
        def helper(word):
            r = len(word) - 1
            l = 0
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        if x < 0:
            return False
        else:
            return helper(str(x))
        
        