class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use for loop to loop for every new char
        # if found duplicate char:
        #   use while loop to pop from the left until the duplicate
        # update length of return length 
        #   max(curr, len(new subset))

        l = 0
        max_length = 0
        substring = set()

        for right_char in s:
            while right_char in substring:
                substring.remove(s[l])
                l += 1

            substring.add(right_char)
            
            if substring:
                max_length = max(max_length, len(substring))
        
        return max_length
