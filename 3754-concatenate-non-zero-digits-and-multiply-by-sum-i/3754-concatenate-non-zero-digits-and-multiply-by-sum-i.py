class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum = 0
        t = str(n)
        l1 = []
        for e in t:
            if e != "0":
                l1.append(e)
        if not l1:
            return 0
        for w in l1:
            digit_sum += int(w)
        res = int("".join(l1)) * digit_sum
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna