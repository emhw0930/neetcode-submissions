class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:        # top is smaller -> it explodes
                    stack.pop()
                elif stack[-1] == -a:     # equal -> both explode
                    stack.pop()
                    alive = False
                else:                     # top is bigger -> a explodes
                    alive = False
            if alive:
                stack.append(a)
        return stack