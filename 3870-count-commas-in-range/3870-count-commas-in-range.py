class Solution:
    def countCommas(self, n: int) -> int:
        m = len(str(n))
        return (m - 1)//3 * (n - 999)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna