from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))  # Truncate toward zero
            else:
                stack.append(int(c))
        return stack[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna