class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(s[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna