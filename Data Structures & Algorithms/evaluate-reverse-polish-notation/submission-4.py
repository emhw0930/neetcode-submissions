class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                back = stack.pop(-1)
                front = stack.pop(-1)
                stack.append(front + back)
            elif char == "-":
                back = stack.pop(-1)
                front = stack.pop(-1)
                stack.append(front - back)
            elif char == "*":
                back = stack.pop(-1)
                front = stack.pop(-1)
                stack.append(front * back)
            elif char == "/":
                back = stack.pop(-1)
                front = stack.pop(-1)
                stack.append(int(float(front) / back))
            else:
                stack.append(int(char))
        
        return stack[-1]