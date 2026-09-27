class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                curr = []
                while stack and stack[-1] != "(": curr.append(stack.pop())
                stack.pop()
                stack += curr
            else:
                stack.append(c)
        return "".join(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna