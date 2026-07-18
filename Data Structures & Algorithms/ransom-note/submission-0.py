class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCounter = Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magCounter:
                magCounter[ransomNote[i]] -= 1
                if magCounter[ransomNote[i]] == 0:
                    del magCounter[ransomNote[i]]
            else:
                return False
        return True