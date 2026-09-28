class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        maxRes = 0
        for c in s:
            if c == "(":
                res += 1
            elif c == ")":
                res -= 1
            maxRes = max(maxRes,res)

        return maxRes

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna