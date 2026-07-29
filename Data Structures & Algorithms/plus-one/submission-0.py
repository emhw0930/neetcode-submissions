class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        curr_digit = len(digits) - 1
        while digits[curr_digit] == 9:
            if curr_digit == 0:
                digits[curr_digit] = 1
                digits.append(0)
                return digits
            digits[curr_digit] = 0
            curr_digit -= 1
            if digits[curr_digit] < 9:
                digits[curr_digit] += 1
                return digits