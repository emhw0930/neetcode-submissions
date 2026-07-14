class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(word):
            l = 0 
            r = len(word) - 1
            while l <= r:
                if word[l] != word[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l + 1:r + 1])
            else:
                l += 1
                r -= 1
        return True