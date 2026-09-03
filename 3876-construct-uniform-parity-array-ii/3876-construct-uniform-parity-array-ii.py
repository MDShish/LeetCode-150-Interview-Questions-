class Solution:
    def uniformArray(self, A: list[int]) -> bool:
        return not (min(A) ^ reduce(or_, A)) & 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna