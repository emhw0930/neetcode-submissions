class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue
            last, last_dir = stack[-1], stack[-1] > 0
            curr, curr_dir = asteroids[i], asteroids[i] > 0
            if last < 0 or curr > 0 or curr_dir == last_dir:
                stack.append(curr)
                continue
            while stack and stack[-1] > 0 and curr < 0:
                last = stack[-1]
                if abs(last) < abs(curr):
                    stack.pop(-1)
                    if not stack or stack[-1] < 0:
                        stack.append(curr)
                elif abs(last) == abs(curr):
                    stack.pop(-1)
                    break
                elif abs(last) > abs(curr):
                    break              
        return stack

        